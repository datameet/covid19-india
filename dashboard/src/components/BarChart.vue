<template>
    <div class="bar-chart">
      <a-tooltip placement="bottom" arrowPointAtCenter  v-for="bar in bars" v-bind:key="bar.key">            
        <template slot="title">
          <span class="tooltip-value">{{bar.value}}</span>
          <span class="tooltip-date">{{bar.date}}</span>
        </template>
        <div class="bar-wrapper">
          <div v-if="bar.current" class="bar current" :style="bar.style"></div>
          <div v-else class="bar" :style="bar.style"></div>
        </div>
      </a-tooltip>
    </div>
</template>
<script>
import moment from 'moment';

export default {
  props: ['data'],  
  computed: {
      bars: function() {
          var max = this.data[this.data.length-1].cases;
          var index = 0;
          var length = this.data.length;
          function makeBar(row) {
              index++;
              var value = row.cases;
              var style = "height: XX%".replace("XX", (100.0*value)/max);
              var current = (index == length)
              return {
                date: moment(row.date).format("MMMM D"),
                value: value,
                style: style,
                key: index,
                current: current
              }
          }
          return this.data.map(makeBar);
      }
  }
}
</script>

<style scoped>
    .bar-chart {
        width: 84px;
        height: 3em;
        display: flex;
        border-spacing: 0px;
    }
    .bar-wrapper {
        flex: 1;
        height: 100%;
        margin-right: 1px;
        position: relative;
    }

    .bar {
        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        min-height: 1px;    
        background-color: rgba(137,34,34,0.25)        
    }
    .bar.current, .bar-wrapper:hover .bar {
        background-color: #ab0000;
    }        


.tooltip-value {
    font-size: 16px;
    font-weight: 700;
    display: block;
    margin-bottom: 1px;
}

.tooltip-date {
    font-size: 12px;
    font-weight: 400;
    opacity: 0.65;
    display: block;    
}    
</style>