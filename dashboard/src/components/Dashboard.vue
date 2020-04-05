<template>
  <div class="hello">
    <h1>{{ msg || "hello" }}</h1>

    <div v-for="stat in stats" v-bind:key="stat.state">
      <h2>{{stat.state}}</h2>
      <div>Doubled in: {{stat.doubled_in}} days</div>
      <div>Cases: {{stat.current}}</div>
      <bar-chart :data="prepareChartData(stat)" />

    </div>
  </div>
</template>

<script>
import axios from 'axios';
import BarChart from './BarChart.vue';

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
    axios.get('http://localhost:8000/cases/growth')
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
</style>
