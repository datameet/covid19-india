<template>
  <a-layout id="components-layout-demo-top-side">
    <a-layout-header class="header">
      <div class="logo" />
      <a-menu
        theme="dark"
        mode="horizontal"
        :defaultSelectedKeys="['2']"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item key="1">Covid19 Explorer</a-menu-item>
      </a-menu>
    </a-layout-header>

    <a-layout-content :style="{ padding: '0 30px', marginTop: '44px' }">    
      <div class="content">
        <h1> Number of COVID-19 Cases in India</h1>

        <div>
          <p>This is a small attempt to visualize the growth of number of cases in India.</p>

          <p>Inspired by <a href="https://ourworldindata.org/coronavirus">Our World in Data</a>.
            Some of the styles on this page are also taken from there. 
          </p> 

          <p>Data Source: Data published by 
            <a href="https://www.mohfw.gov.in/">Minstry of Health and Family Welfare</a>, 
            compiled by <a href="https://projects.datameet.org/covid19/">DataMeet</a> 
            and published as an API by <a href="https://twitter.com/anandology">@anandology</a>.
          </p>

          <p>Github Repo: <a href="https://github.com/anandology/covid19">https://github.com/anandology/covid19</a></p>
        </div>

        <table class="covid-table">
          <tr>
            <th class="location">Location</th>
            <th class="doubling-days">How long did it take for the number of total confirmed cases to double?</th>
            <th class="cases">Total confirmed cases</th>
          </tr>
          <tr v-for="stat in stats" v-bind:key="stat.state">
              <td class="location">{{getLocationName(stat.state)}}</td>
              <td class="doubling-days">
                <div v-if="stat.doubled_in">
                  <span class="label">doubled in</span>
                  <br>
                  <span class="days">{{stat.doubled_in}} days</span>
                </div>
              <td class="plot-cell">
                <div class="trend">
                  <div class="plot" style="padding-bottom: 10px;">
                    <bar-chart :data="prepareChartData(stat)" />
                  </div>
                  <div class="value">
                    <div class="time-series-value current">
                      <span class="count">{{stat.current}} total</span>
                      <span class="date current">{{getDate(stat)}}</span>
                    </div>
                  </div>
                </div>
              </td>
          </tr>
        </table>
      </div>
    </a-layout-content>
  </a-layout>
</template>

<script>
import axios from 'axios';
import BarChart from './BarChart.vue';
import states from "../states.js";
import moment from 'moment';

export default {
  name: 'Dashboard',
  props: {
    msg: String
  },
  components: {
    BarChart
  },
  data() {
    return {
      stats: []
    }
  },  
  created() {
    var API_URL = process.env.VUE_APP_API_URL;
    axios.get(API_URL + '/cases/growth')
    .then(response => {
         this.stats = response.data
    })
    .catch(error => {
      console.log(error);
    })
  },
  methods: {
    prepareChartData: function(stat) {
      var cases = stat.cases.map(x => x);
      cases.reverse();
      return cases;
    },
    getLocationName: function(code) {
      if (code == "india") {
        return "India"
      }
      else {
        return states[code];
      }
    },
    getDate: function(stat) {
      return moment(stat.cases[0].date).format("MMMM D");      
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
div.content {
  background-color: #fff;
  padding: 24px;
  minHeight: 380px;
}

td.doubling-days .label {
  font-size: 14px;
  font-weight: 700;
  opacity: 0.7;
}

td.doubling-days .days {
  background-color: rgb(222, 137, 165); 
  color: white;  
  font-size: 20px;
    font-weight: 700;
    display: inline-block;
    margin-top: 3px;
    margin-bottom: 5px;
    white-space: nowrap;
    padding: 3px 9px 3px 10px;
    margin: 4px -9px 0 -10px;
    line-height: 1.5rem;
    border-radius: 2rem;  
}

td.location, th.location {
    max-width: 150px;
}

td.doubling-days, th.doubling-days {
    max-width: 100px;
}

table.covid-table td, table.covid-table th {
  padding: 20px 10px;
}

table.covid-table th {
  vertical-align: bottom;
}

.covid-table .trend .value {
    flex: 1;
    align-self: center;
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 6px;

}
.covid-table .time-series-value {
    line-height: 1.3;
    white-space: nowrap;
}

.time-series-value.current .count {
    color: #ca3a77;
    font-size: 16px;
    font-weight: 700;
    display: block;
    margin-bottom: 1px;
}

.covid-table .time-series-value .date.latest {
    font-size: 12px;
    font-weight: 400;
    opacity: 0.65;
    display: block;    
}

.covid-table .trend {

    display: flex;
    height: 100%;

}
.covid-table .trend .plot {
    flex: 0;
    margin-bottom: -1px;
    align-self: flex-end;
}
.covid-table .trend .value {

    flex: 1;
    align-self: center;
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 6px;

}

.covid-table .time-series-value .date.latest {

    font-size: 12px;
    font-weight: 400;
    opacity: 0.65;

}
</style>
