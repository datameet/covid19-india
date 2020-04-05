<template>
    <div class="bar-chart">
        <div class="bar-wrapper" v-for="bar in bars" v-bind:key="bar.key">
            <div class="bar" :style="bar.style"></div>
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
          function makeBar(row) {
              index++;
              var value = row.cases;
              var style = "height: XX%".replace("XX", (100.0*value)/max);
              return {
                  style: style,
                  key: index
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
        background-color: rgba(158,102,126,0.8);
    }
    
</style>