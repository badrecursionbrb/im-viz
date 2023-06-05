<template>
  <v-container id="conte">
    <v-row>
      <v-col id="processTreeColumn" cols="12" xs="12" sm="12" md="12" lg="5" xl="5" >
        <v-sheet color="white" :elevation="24" rounded="lg" id="processTreeSheet"  >
          <v-card-title id="v-card-title_pt"  :class="{ highlighted: highlightedPTNode }">

            <v-row align-items="end">
              <v-col class="d-none d-sm-flex" cols="3">
                <div id="v-card-title-text">PROCESS TREE</div>
              </v-col>
              <v-col cols="6">
                <v-select class="actionButton" rounded="lg" bg-color="black" id="algorithmSelector"
                  v-model="select_algorithm_button" :items="select_algorithm_vals" item-title="algorithm_descr"
                  item-value="algorithm_id" label="Algorithm Selection" style="height:2.5vh"
                  :disabled="this.algorithmIsRunning"></v-select>
              </v-col>
              <v-col cols="3">

                <v-text-field v-model="inductiveThreshold" :disabled="!useThresholdRule(this.select_algorithm_button)"
                  type="number" style=" z-index: 1;color: white;" hide-details variant="outlined">
                </v-text-field>

              </v-col>
            </v-row>
          </v-card-title>
          
          <ProcessTree id="processTreeElem" ref="ptChild" :triggerChange="imDataPTNode "
            @errorEventTree="showErrorBox(message)" @zoomIn="handleZoomIn" @zoomOut="handleZoomOut"
            @restoreZoom="handleRestoreZoom"></ProcessTree>
          <!-- <div id="btn_group" color="black" multiple
            style="position: flex;display: center;"> </div>-->
          <v-card-actions style="position: flex; display display">
            <v-row>
              <v-col cols="12">
                <v-btn class="btn" color="black" @click="handleZoomIn">+</v-btn>
                <v-btn class="btn" color="black" @click="handleZoomOut">-</v-btn>
                <v-btn class="btn" color="black" @click="handleRestoreZoom">1:1</v-btn>

                <v-btn id="back" class="actionButton btn" color="black" @click="stepBackward"><v-icon start
                    icon="mdi-chevron-left"></v-icon>Back</v-btn>
                <v-btn class="actionButton btn" :disabled="!this.algorithmIsRunning" id="ResetBtn" color="black"
                  @click="resetData">Reset</v-btn>
                <v-btn class="actionButton btn" :disabled="!this.inputIsCorrect" id="StringToLog" color="black"
                  @click="handleRunClick">Go!</v-btn>
                <v-btn id="next" class="actionButton btn" color="black" @click="stepForward"
                  :disabled="currentStep >= maxSteps || updating"><v-icon start icon="mdi-chevron-right"></v-icon>Next</v-btn>
                <v-btn class="btn" color="black" @click="downloadPicture"><v-icon icon="mdi-camera"></v-icon></v-btn>
              </v-col></v-row>
          </v-card-actions>
        </v-sheet>
        <v-combobox class="inputElems" bg-color="grey-lighten-2" rounded="lg" v-model="logString" clearable
          :rules="[inputRule]" required label="Please put in your log according the following format: <a,b,c,d>3;"
          style="margin-top:2vh;"
          :items="['<a,b,c,d>3;', '<a,b,c,d>2; <d,a,b>3; <a,d,c>4; <b,c,d>5;', '<a,b,c>2; <a,c,c,b>3; <b,a,c>5; <b,b,c,a>6; <c,a,a,a>1;<c,b>4;', '<a,c,d>5; <c,a,b>4; <e,f,a>4;', '<a,c,d>4;<c,a,a,d>5;',]">
        </v-combobox>   
        <v-row> <v-card id="example_selected_card"><v-card-text>{{ selected_exam() }}</v-card-text></v-card></v-row>
      </v-col>
      <v-col cols="12" xs="12" sm="12" md="12" lg="7" xl="7">
        <v-sheet id="DFGSheet" color="white" :elevation="24" rounded="lg" height="44.5vh" style="margin-bottom: 3vh;">
          <v-card id="vCardDFGWrapper" style="width: 100%; height: 100%" >
            <v-tabs id="tabsBarDFG" v-model="tab" bg-color="primary" @update:modelValue="tabChanged()">
              <v-tab value="one" :class="{ highlighted: highlightedDFG }">Directly Follows Graph (DFG)</v-tab>
              <v-tab value="two" :class="{ highlighted: highlightedTable }">Traces Table</v-tab>
            </v-tabs>

            <v-card id="vCardDFGContent">
              <v-window id="vWindowDFGContent" v-model="tab">
                <v-window-item value="one">
                  <PackDFGComp title="dfg comp svg" ref="dfgChild" id="dfgGraph" :triggerChange="imDataDFG" />
                </v-window-item>
                <v-window-item value="two" class="scrollable">
                  <TableComp title="tableComp" ref="tableChild" id="tableTab" :tableDataChild="imDataTable"
                    :triggerChange="imDataTable"/>
                </v-window-item>
              </v-window>
            </v-card>
          </v-card>
        </v-sheet>

        <v-row>
          <v-col cols="12" xs="12" sm="6" md="6" lg="6" xl="6">
            <v-card id="algorithmDisplay" color="white" :elevation="24" rounded="lg">
              <v-card-text class="v-card-text-algoexpl" :class="{ highlighted: highlightedOperator }"> 
                <v-card-title class="cur_step_card v-card-text-algoexpl">{{ infoTextHeading }}</v-card-title>
                {{ infoText }}
                <v-card-title class="cur_step_card v-card-text-algoexpl">{{ algo_step }}</v-card-title> 
              </v-card-text>
            </v-card>

            <v-row>
              <v-col cols="12" xs="12" sm="12" md="12" lg="12" xl="12">
                <div class="inputElems" id="fileInput">
                  <v-file-input v-model="currentFile" label="Select Excel/XES" hide-details="False"
                    accept=".xlsx,.xls,.xslx,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,.xes"
                    clearable variant="filled" bg-color="grey-lighten-2" @change="onFileSelected"></v-file-input>
                </div>
              </v-col>
            </v-row>

          </v-col>
          <v-col cols="12" xs="12" sm="6" md="6" lg="6" xl="6">
            <v-list height="34.3vh" rounded="lg" color="white" bg-color="black" dense>
              <v-list-item bg-color="black" :border="true" class="algorithm-lineitem"
                v-for="(item, index) in algorithmItems" :key="index"
                :class="{ 'highlight': highlightedIndices.includes(index) }"
                :style="{ marginLeft: indentationLevel(item.tabs) }">
                <v-list-item-title class="algorithm-line-title">{{ item.text }}</v-list-item-title>
              </v-list-item></v-list>

          </v-col>

        </v-row>
      
      </v-col>
    </v-row>

    <div class="center-screen">
      <v-alert v-model="errorMessagePopUp" type="error" close-label="Close Alert" color="deep-purple-accent-4"
        title="Error!" :elevation="24" :text="this.errorMessageText" closable>
      </v-alert>
    </div>
    <div class="vld-parent">
      <loading v-model:active="isLoading" :can-cancel="true" :on-cancel="onCancel" :is-full-page="fullPage">
      </loading>
    </div>
  </v-container>
</template>

<script>

import { Buffer } from 'buffer';
import axios, { isCancel, AxiosError } from 'axios';
// const http = require('http');
// const https = require('node:https');


import Loading from 'vue-loading-overlay'
import '@/css/vue-loading.css'

import ProcessTree from '@/components/ProcessTree.vue';
import PackDFGComp from '@/components/PackDFG.vue';
import TableComp from '@/components/TableComp.vue';

import algorithm_data_im_standard from '@/assets/inductive_miner_standard.json';
import algorithm_data_im_infrequent from '@/assets/inductive_miner_infrequent.json';
import { MainConstants, BuildConstants } from '@/assets/constants.js';



export default {
  components: {
    ProcessTree,
    PackDFGComp,
    TableComp,
    Loading
  },
  mounted() {
    this.select_algorithm_button = this.select_algorithm_vals[0].algorithm_id;
    this.set_algorithm_data();

    this.picBuffer = Buffer.alloc(5000000, 'utf-8'); // creating a buffer for the picture of size 
  },
  watch: {
    select_algorithm_button() {
      this.set_algorithm_data();
    },
    isLoading() {
      this.renderLoadingAnimation();
    },
    logString() {
      this.selected_exam();
  },
},
  data() {
    return {
      updating: false,
      highlightedPTNode: false,
      highlightedDFG: false,
      highlightedOperator: false,
      highlightedTable: false,
      example_selected: "",
      algo_step: '',
      indentSize: 30,
      updateIndex: 0,
      select_algorithm_vals: [
        { algorithm_descr: 'Inductive Miner Standard', algorithm_id: 'im_standard' },
        { algorithm_descr: 'Inductive Miner Infrequent', algorithm_id: 'im_infrequent' },
      ],
      select_algorithm_button: null,
      algorithmItems: null,
      highlightedIndices: [],
      currentStep: 0,
      maxSteps: 0,
      logString: '',
      dialog: false,
      infoText: '',
      infoTextHeading: '',

      imData: null,
      imDataAtCurrentStep: null,
      imDataPTNode: null,
      imDataDFG: null,
      imDataTable: null,
      imDataPetriNet: null,
      downloadEnabled: false,

      tab: null,

      algorithm_data: null,

      currentFile: null,

      inductiveThreshold: 0.1,

      errorMessagePopUp: false,
      errorMessageText: "",
      inputIsCorrect: false,
      algorithmIsRunning: false,
      isLoading: false,
      fullPage: true,

      useThresholdRule: algorithm_id => {
        if (algorithm_id === 'im_infrequent') {
          return true;
        }
        else {
          return false;
        }
      },
      inputRule: logString => {
        if (MainConstants.LOGSTRING_VALIDATION.test(logString)) {
          console.log("string does match");
          this.inputIsCorrect = true;
          return true;
        }
        else {
          let message = "string does not match";
          this.inputIsCorrect = false;
          console.log(message);
          return message;
        }
      }
    };
  },
  computed: {
    indentationLevel() {
      return index => `${index * this.indentSize}px`;
    }
  },
  methods: {
    selected_exam(){ 
        if (this.logString ==='<a,b,c,d>3;') {
          this.example_selected = "Example Selected: Sequence Cut";
        }  
        else if (this.logString ==='<a,b,c,d>2; <d,a,b>3; <a,d,c>4; <b,c,d>5;') {
          this.example_selected = "Example Selected: Tau Loop ";
        }  
        else if (this.logString ==="<a,b,c>2; <a,c,c,b>3; <b,a,c>5; <b,b,c,a>6; <c,a,a,a>1;<c,b>4;") {
          this.example_selected = "Example Selected: Fall Through";
        }  
        else if (this.logString ==="<a,c,d>5; <c,a,b>4; <e,f,a>4;") {
          this.example_selected = "Example Selected: Activity once per Trace";
        }  
        else if (this.logString ==="<a,c,d>4;<c,a,a,d>5;") {
          this.example_selected = "Example Selected: Loop Cut";
        } else { this.example_selected = "";}
        return this.example_selected
      },
    handleZoomIn() {
      this.$refs.ptChild.controlScale('bigger');
    },
    handleZoomOut() {
      this.$refs.ptChild.controlScale('smaller');
    },
    handleRestoreZoom() {
      this.$refs.ptChild.controlScale('restore');
    },

    async downloadPicture() {
      // method for downloading a picture to svg (designed for downloading a petri net image)

      console.log("trying to download");
      if (this.downloadEnabled) {
        console.log("downloading picture");
        var hiddenElement = document.createElement('a');

        hiddenElement.href = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(this.imDataPetriNet);
        hiddenElement.target = '_blank';
        hiddenElement.download = 'petri_net.svg';
        hiddenElement.click();
      }

    },
    stepForward() {
      // FOR STEP FORWARD BUTTON
      if (this.currentStep < this.maxSteps)
        this.currentStep++;
      this.runUpdate(this.currentStep);
    },

    stepBackward() {
      // FOR STEP BACKWARD BUTTON
      if (this.currentStep >= 1) {
        this.currentStep--;
        this.runUpdate(this.currentStep);
      }
    },
    onFileSelected(file) {
      // Method that gets triggered when a file is selected, then checks if actually one was 
      // selected

      if (!this.currentFile) {
        this.showErrorBox("Please select a file!");
      }
      else {
        // Handle the selected file
        console.log("Selected file: " + this.currentFile);
        let isFileInput = true;
        this.runMinerRequest(this.currentFile, isFileInput)
      }
    },
    handleRunClick() {
      // method for handling the button to trigger the request and thereby running the inductive miner
      // checks first if the logstring conforms to the regex rule 
      // only run if logstring not for logfile 

      console.log("clicked run/Go button");
      var isFileInput = false;
      if (this.inputRule(this.logString)) {
        this.runMinerRequest(this.logString, isFileInput);
      }
      else {
        var errorMessage = "logstring does not conform regex rule"
        console.log(errorMessage);
        // TODO display error message box
        this.showErrorBox(errorMessage);
      }
    },
    runMinerRequest(logstringOrFile, isFileInput = false) {
      /**
       * 
       */
      this.updateIndex = 0;
      console.log("sending request " + (new Date).toLocaleTimeString());
      this.algorithmIsRunning = true;
      console.log("logstring or file is: " + logstringOrFile);
      // const logstring = { logstring: "<a,b,c,e,f>10;<a,d,b,c,d,e,f>10;<a,d,c,e,c,e,f>10;<a,d,e,c,d,e,f>10;<a,d,c,d,e,f>10" }
      //const requestAdr = "http://127.0.0.1:5000/get_visualization_data_get_test"
      console.log(MainConstants);
      const requestAdrBase = BuildConstants.REQUESTADRESSBASE;
      const requestAdrAlgo = "?algorithm=" + this.select_algorithm_button;
      var parameters = ""
      if (this.select_algorithm_button === "im_infrequent") {
        parameters = "&threshold=" + this.inductiveThreshold;
      }
      const requestPostfix = requestAdrAlgo + parameters;

      if (isFileInput) {
        console.log("sending a file request");
        var formData = new FormData();
        // take first element of files array pointer
        formData.append("logfile", logstringOrFile[0]);

        const requestAdr = requestAdrBase + "/get_visualization_data_file" + requestPostfix;
        console.log("sending request: " + requestAdr);
        this.isLoading = true;
        axios.post(requestAdr, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }).then(response => this.handleRequestResponse(response))
          .catch(error => this.handleAxiosError(error));
      }
      else {
        console.log("logstring request sent; logstring to send is: " + logstringOrFile);
        var logstring_json = { 'logstring': logstringOrFile };

        const requestAdr = requestAdrBase + "/get_visualization_data_logstring" + requestPostfix;
        console.log("sending request: " + requestAdr);

        axios
          .post(requestAdr, logstring_json, {
            headers: {
              'Content-Type': 'application/json'
            }
          })
          .then(response => this.handleRequestResponse(response))
          .catch(error => this.handleAxiosError(error))
          .finally(() => { this.isLoading = false; });
        //.catch(error => console.error(error));
        console.log("ran miner request finished " + (new Date).toLocaleTimeString());
      }
    },
    handleAxiosError(error) {
      var message = error.message;
      if (error.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx
        console.log(error.response.data);
        console.log(error.response.status);
        console.log(error.response.headers);
        message = message + ` ${error.response.data}`;
      } else if (error.request) {
        // The request was made but no response was received
        // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
        // http.ClientRequest in node.js
        console.log(error.request);
      } else {
        // Something happened in setting up the request that triggered an Error
        console.log('Error', error.message);
      }
      this.showErrorBox(message);
      console.log(error.config);
    },
    handleRequestResponse(response) {
      if (response.status === 200) {
        console.log("got request back with 200 code " + (new Date).toLocaleTimeString());
        this.imData = response.data["all_steps_list"];
        console.log(this.imData);
        this.maxSteps = this.imData[Object.keys(this.imData).length - 1].step;
        this.imDataPetriNet = Buffer.from(response.data["process_tree_image"], 'base64').toString('utf8');
        this.downloadEnabled = true;
        // console.log(this.imDataPetriNet);
        this.currentStep = 0;
        this.isLoading = false;
        this.runUpdate(this.currentStep);
      }
      else if (response.status === 400) {
        console.log("request 400 result")
        let errorMessage = 'Error: ' + response.data.message;
        this.showErrorBox(errorMessage);
        this.downloadEnabled = false;
      }
      else {
        this.downloadEnabled = false;
        let errorMessage = "got other request back, status: " + response.status
        console.log(errorMessage);
        console.log(response.data);
        this.showErrorBox(errorMessage);
      }
      console.log("miner response handling finished " + (new Date).toLocaleTimeString());
    },
    async runUpdate(stepNo) {
  console.log("runUpdate - stepNo: " + stepNo + " start: " + (new Date).toLocaleTimeString());

  if (this.imData !== null) {
    this.imDataAtCurrentStep = this.imData[stepNo];
    console.log("IM Data at current step: " + this.imDataAtCurrentStep);

    this.highlightedPTNode = false;
    this.highlightedDFG = false;
    this.highlightedOperator = false;
    this.highlightedTable = false;
    this.updating=true;

    this.imDataDFG = this.imDataAtCurrentStep.cur_dfg;
    console.log("Updated DFG: " + this.imDataDFG);  
    this.algo_step="Current Step: Update DFG"
    this.highlightedDFG = true;

    this.tab="one"
    await this.waitAndUpdateInfo();

    this.imDataTable = this.imDataAtCurrentStep.cur_traces;
    console.log("Updated Table: " + this.imDataTable);
    this.algo_step="Current Step: Update Trace Table"
    this.highlightedTable = true;
    this.highlightedDFG = false;
    this.tab="two"  
    await this.waitAndUpdateInfo();

    this.highlightAndChangeInfoText();
    this.tab="two"
    this.imDataOperator = this.imDataAtCurrentStep.label;
    console.log("Updated Operator: " + this.imDataOperator);
    this.algo_step="Current Step: Update Algorithm"
  
    this.highlightedOperator = true;
    this.highlightedTable = false;
    await this.waitAndUpdateInfo();

   
    this.imDataPTNode = this.imDataAtCurrentStep.cur_tree;
    console.log("Updated PTNode: " + this.imDataPTNode);
    this.algo_step="Current Step: Update Process Tree"
    this.highlightedPTNode = true;
    this.highlightedOperator = false;
    this.tab="one"
    this.updating=false;
    await this.waitAndUpdateInfo();

  } else {
    console.log("Resetting data with imData == null ");
    this.imData = null;
    this.imDataAtCurrentStep = null;
    this.imDataPTNode = null;
    this.imDataDFG = null;
    this.imDataOperator = null;
    this.imDataTable = null;
  }
},

waitAndUpdateInfo() {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve();
    }, 2000); 
  });
},


highlightAndChangeInfoText() {
      let highlightedIndices = [];
      if (this.imDataAtCurrentStep.case_type === "CUT") {
        this.infoTextHeading = this.imDataAtCurrentStep.label
        this.infoText = this.algorithm_data.explanations[this.imDataAtCurrentStep.label];
      }
      else {
        this.infoTextHeading = this.imDataAtCurrentStep.case_type
        this.infoText = this.algorithm_data.explanations[this.imDataAtCurrentStep.case_type];
      }
      highlightedIndices = this.algorithm_data.hightlighting_map[this.imDataAtCurrentStep.case_type];
      console.log("Current operation (symbol) is: " + this.imDataAtCurrentStep.label +
        " case type: " + this.imDataAtCurrentStep.case_type +
        " info Text is: " + this.infoText);
      this.highlightedIndices = highlightedIndices;
    },
tabChanged() {
      console.log("tabChanged function call testing log here");
      if (this.tab === "one") {
        console.log("tabChanged one");
      }
      else if (this.tab === "two") {
        console.log("tabChanged two");
      }
    },
set_algorithm_data() {
      console.log("setting algorithm data ...");
      if (this.select_algorithm_button === "im_standard") {
        console.log("taking algorithm data im_standard");
        this.algorithm_data = algorithm_data_im_standard.algorithm_data;
      }
      else if (this.select_algorithm_button === "im_infrequent") {
        console.log("taking algorithm data im_infrequent");
        this.algorithm_data = algorithm_data_im_infrequent.algorithm_data;
      }
      else {
        console.log("taking algorithm data im_standard");
        this.algorithm_data = algorithm_data_im_standard.algorithm_data;
      }
      this.algorithmItems = this.algorithm_data.algorithm_lines;
      console.log("set algorithm data to: " + this.algorithm_data);
    },
    showErrorBox(errorMessage) {
      this.errorMessageText = errorMessage;
      this.errorMessagePopUp = true;
    },
    renderLoadingAnimation() {
      console.log("triggering loading animation")


    },
    resetData() {
      this.isLoading = false;
      this.algorithmIsRunning = false;
      this.runUpdate(0, false);

    },
    onCancel() {
      console.log('User cancelled the loader.')
    },
  }
}
</script>
<style>
.algorithm-lineitem {
  padding-top: 0px !important;
  padding-bottom: 0px !important;
  white-space: pre;
  min-height: 0px !important;
}

.algorithm-line-title {
  text-align: left;
  font-size: 1.9vh !important;
}

/* .algorithm-lineitem > .v-list-item-title{

} */
#example_selected_card{
 color: rgb(255, 255, 255) ;
 background-color: transparent !important ;
 box-shadow: none !important; 
 font-size: 1rem !important;
}

.cur_step_card{
 color: rgb(17, 174, 106);
 padding: 0px !important;
}

#algorithmSelector {
  max-width: 20vw !important;
  align-self: right !important;
  padding: 0rem !important;
  margin: 0rem !important;
}

@media (min-width: 451px) {
  .v-btn__content {
    font-weight: 401 !important;
    font-size: 1.7vh !important;
  }

  #conte {
    max-width: 96vw !important;
    max-height: 90vh !important;
    height: 90vh !important;
    width: 96vw !important;
    vertical-align: middle !important;
    align-items: center !important;
    /* padding-top: 3vh !important; */
    padding: 1vh !important;
  }

  .v-card-actions {
    background-color: #E0E0E0;
  }
}

@media (max-width: 450px) {
  .v-btn__content {
    font-size: 11px !important;
  }

  .btn {
    /* border: solid black; */
  }

  #conte {
    max-width: 96vw !important;
    width: 96vw !important;
    align-items: center;
    position: flex;
    padding-bottom: 20vh !important;
  }

  #v-card-title-text {
    font-size: 0.5vh !important;
  }

  .mdi-menu-down {
    position: absolute !important;
    align-items: top !important;
    top: 0% !important;
    right: 0%;
  }

}

.highlight {
  background-color: rgb(8, 69, 28) !important;
}

.actionButton {
  height: 3vh;
}

#DFGSheet {
  flex-direction: column;
  display: flex;
}

#vCardDFGWrapper {
  flex-direction: column;
  display: flex;
  flex-grow: 1;

}

#tabsBarDFG {
  flex-grow: 0;
  flex-shrink: 0;
}

#vCardDFGContent {
  flex-direction: column;
  display: flex;
  flex-grow: 1;
}

#vWindowDFGContent {
  flex-grow: 1;
  display: flex;
}

#vWindowDFGContent>.v-window__container {
  flex-direction: column;
  display: flex;
  flex-grow: 1;
}

#vWindowDFGContent>.v-window__container>.v-window-item {
  flex-direction: column;
  display: flex;
  flex-grow: 2;
}

#dfgGraph {
  width: 100%;
  height: 100%;
  display: flex;
  flex-grow: 1;
}

.scrollable {
  overflow-y: scroll;
}

.v-messages__message {
  color: rgb(188, 45, 45);
  font-weight: 500;
}

.v-field__input {
  font-size: 1.7vh !important;
}

.v-card .v-card-title {
  line-height: 6vh !important;
}

.v-card-text-algoexpl {
  padding: 0px 1rem  !important;
  font-size: 2.5vh !important;
  flex: 1 1 auto;
  line-height: 3vh !important;
}

.inputElems {
  background: #E0E0E0;
}

#fileInput {
  margin-top: 2vh;
}

#algorithmDisplay {
  height: 24.3vh;
  display: flex;
}

#processTreeColumn {}

#processTreeSheet {
  height: 72vh;
  display: flex;
  flex-direction: column;
}

#processTreeElem {
  display: flex;
}

#processTreeElem>div {
  display: flex;
}

#v-card-title_pt {
  color: white;
  background-color: black;
  letter-spacing: 0.0892857143em !important;
  font-weight: 400 !important;
  font-size: 1.5vh !important;
  /*height: 6vh;*/
  text-align: left !important;
  /*padding: 0% !important;*/
  margin: 0% !important;
}

#v-card-title-text {
  padding: 1vh !important;
  padding-bottom: 0%;
  font-size: 2vh !important;
  font-weight: 401;
  align-self: center !important;
  display: flex !important;
  vertical-align: middle !important;
}

.center-screen {
  /* display: flex;
  justify-content: center;
  align-items: center;
  text-align: center; */

  position: fixed;
  left: 50%;
  bottom: 50px;
  transform: translate(-50%, -50%);
  margin: 0 auto;
}
.highlighted {
 box-shadow: 0 0 5px rgb(8, 69, 28) !important;
 background: rgb(8, 69, 28) !important;;

}

</style>

