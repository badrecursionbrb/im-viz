<template>
  <v-row no-gutters>
    <v-col cols="12" xs="12" sm="12" md="12" lg="12" xl="12">
     
        <vue-tree class="tree-container" ref="tree" :dataset="PTNode" :config="treeConfig" linkStyle="straight"
            @wheel="WheelZoom">
          <template v-slot:node="{ node, collapsed }">
            <div class="PTNode" :style="{ border: collapsed ? '0px solid grey' : '' }">
              <img :src="node.avatar" style=" width:48px" />
              <span style=" font-weight: bold ; font-size: x-large;">{{ node.displayVal }}</span>

            </div>
     
        </template>

      </vue-tree>
    </v-col>
  </v-row>



</template>
  
  
<script>

import VueTree from "@ssthouse/vue3-tree-chart";
import "@ssthouse/vue3-tree-chart/dist/vue3-tree-chart.css";

export default {

  name: "ProcessTree",
  props: ['triggerChange'],
  components: { 'vue-tree': VueTree },
  watch: {
    triggerChange: function (ptData) {
      console.log("rendering ptData from child " + (new Date).toLocaleTimeString());
      try {
        this.handleData(ptData);
      } catch (error) {
        console.log(error)
        this.$emit('errorEventTree', error.message);
      }
    }

  },
 
  methods: {
    WheelZoom(event) {
      event.preventDefault();
      this.accumulatedDeltaY += event.deltaY;
      if (Math.abs(this.accumulatedDeltaY) >= this.wheelSensitivityThreshold) {
        const zoomDirection = this.accumulatedDeltaY > 0 ? 'smaller' : 'bigger';
        this.controlScale(zoomDirection);
        this.accumulatedDeltaY = 0;
    }},
    controlScale(command) {
      switch (command) {
        case 'bigger':
          this.$refs.tree.zoomIn()
          break
        case 'smaller':
          this.$refs.tree.zoomOut()
          break
        case 'restore':
          this.$refs.tree.restoreScale()
          break

      }
    },
    handleData(ptData) {
      // handling the data received from the main from InductiveMiner
      console.log("rendering Process Tree");
      if (!ptData || (ptData
        && Object.keys(ptData).length === 0
        && Object.getPrototypeOf(ptData) === Object.prototype)) {
        console.log("ptData is empty! Error ");
        throw new Error('Error: ptData is empty!');
      }
      else {
        this.PTNode = this.traversePTData(ptData);
        console.log(this.PTNode)
      }
    },
    traversePTData(ptData) {
      // traversing the tree to append avatar fields and collapse the list to string 
      if (Object.hasOwn(ptData, 'value')) {
        if (ptData.value === "->") {
          ptData.avatar = require('@/assets/sequence.png');
          ptData.displayVal = "";
        }
        else if (ptData.value === "X") {
          ptData.avatar = require('@/assets/XOR.png');
          ptData.displayVal = "";
        }
        else if (ptData.value === "+") {
          ptData.avatar = require('@/assets/AND.png');
          ptData.displayVal = "";
        }
        else if (ptData.value === "*") {
          ptData.avatar = require('@/assets/loop.png');
          ptData.displayVal = "";
        }
        else {
          ptData.avatar = require('@/assets/endpoint.png');
          ptData.displayVal = ptData.value;
        }
      }
      else{
        console.log("ptNode has no value elem" + ptData);
        // ptData.avatar = require('@/assets/endpoint.png');
        // ptData.displayVal = ptData.toString();
      }
      if (Object.hasOwn(ptData, 'children')) {
        for (let i = 0; i < ptData.children.length; i++) {
          var child = ptData.children[i]
          if (typeof(child) === 'string') {
            ptData.children[i] = { displayVal: child.toString(), avatar: require('@/assets/endpoint.png') };
          }
          else {
            console.log("Calling child " + i)
            this.traversePTData(child)
          }
        }
      }
      console.log(ptData)
      return ptData;
    },
  },

  data() {
    return {
      wheelSensitivityThreshold: 50,
      accumulatedDeltaY: 0,
      PTNode: { //Pass TreeData
        // value: '',
        // avatar: require('@/assets/sequence.png'),
        // children: [
        //   {

        //     avatar: require('@/assets/XOR.png'),
        //     value: '',
        //     children: [
        //       {
        //         value: 'C',
        //         avatar: require('@/assets/endpoint.png'),
        //       },
        //       {
        //         value: 'D',
        //         avatar: require('@/assets/endpoint.png'),
        //       },
        //       {
        //         value: 'E',
        //         avatar: require('@/assets/endpoint.png'),
        //       },
        //     ],
        //   },
        //   {
        //     value: '',
        //     avatar: require('@/assets/loop.png'),
        //     children: [
        //       {
        //         value: 'G',
        //         avatar: require('@/assets/endpoint.png'),
        //       },
        //       {
        //         value: 'H',
        //         avatar: require('@/assets/endpoint.png'),
        //       },
        //     ],
        //   },
        //   {
        //     value: 'I',
        //     avatar: require('@/assets/endpoint.png'),
        //   },
        // ],
      },
      treeConfig: { nodeWidth: 100, nodeHeight: 60, levelHeight: 200 },
    };
  },
  }

</script>
  
<style>
/* .v-btn{
  font-size: 1vh !important;
  font-weight: 300 !important;
  
} */
.tree-container{
  display: flex !important;
  align-items: center !important;
  flex: 1 1 auto;
}

.tree-container .link {
  stroke-width: 5px !important;
  stroke: rgb(114, 114, 114) !important;

}


.PTNode {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: rgb(0, 0, 0);

}
</style>