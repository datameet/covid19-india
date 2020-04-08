<template>
    <div class="bar-chart">
        <div class="bar-wrapper" v-for="bar in bars" v-bind:key="bar.key">
            <div v-if="bar.current" class="bar current" :style="bar.style"></div>
            <div v-else class="bar" :style="bar.style"></div>
        </div>
    </div>
</template>
<script>
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
    .bar.current {
        background-color: #ab0000;
    }        
</style>