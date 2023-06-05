<template>
    <v-sheet id="btngroup">
    <v-btn id="btngroup" bg-color="grey-lighten-3" :rounded="0" variant="flat" href="/processtree">Process Tree</v-btn>
    <v-btn id="btngroup" bg-color="grey-lighten-3" :rounded="0" variant="flat" href="/dfg">DFG</v-btn>
    <v-btn id="btngroup" bg-color="grey-lighten-3" :rounded="0" variant="flat" href="/flower">FlowerModel</v-btn>
    <v-btn id="btngroup" bg-color="grey-lighten-3" :rounded="0" variant="flat" href="/cuts">Cuts</v-btn>
    <v-btn id="btngroup" bg-color="grey-lighten-3" :rounded="0" variant="flat" href="/processdiscovery">Process Discovery</v-btn>
    <v-btn id="btngroup" bg-color="grey-lighten-3" :rounded="0" variant="flat" href="/indumining">Inductive Mining</v-btn>
  </v-sheet>

    <v-container id="content">

    <h2>Directly-Follows Graphs (DFGs)</h2>

  <br />
      <h3>What are exactly Directly-Follows Graphs?</h3>
      <hr class="hr-edge-weak">
      <br />
        <p style="font-size: large;"><strong>Directly-Follows Graphs</strong> as known as DFGs is one of
          the most used process models, which allows discovery based on the given event data. Petri nets, BPMN diagrams,
          and UML activity diagrams are other examplary formalisms for process models. </p>
        <br />
        Here are a few examples of DFG <a href="ProjectDoc">[2][4]</a>:
        <br />
        <br />
     
    
            <img id="img1" src='@/assets/dfg1.png'/>
            <br/>
            <img id="img2" src='@/assets/dfg2.png'/>
           

        <br />
        <br/>
          Currently, there are more than 30 commercial offerings of process mining software (e.g., Celonis, Disco,
          ProcessGold, myInvenio, PAFnow, Minit, QPR, Mehrwerk, Puzzledata, LanaLabs, StereoLogic, Everflow, TimelinePI,
          Signavio, and Logpickr). They all start from DFGs for discovery <a href="ProjectDoc">[3]</a>
    </v-container>
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
</template>
  
<script>
import VuePictureSwipe from 'vue3-picture-swipe';
export default {
  components: { VuePictureSwipe },
}
</script>
  
<style>
#btngroup{
  background-color:rgb(208, 208, 0,0);
  color:white;
  text-align: center !important;
}

#content {
  max-width: 90vw;
  margin-left: 5vw ;
  margin-right: 5vw;

  align-self: center;
  font-size: 3vh !important;
  color: white;
  text-align: left;
}
.hr-edge-weak {
  border: 0;
  padding-top: 0.5vh;
  background: linear-gradient(to right, transparent, #d0d0d5, transparent);
}

#img1 {
 
  width: 30%;
}
#img2 {
 
  width: 30%;
}

@media (max-width: 600px){
  #img1 {
 width: 90%;
}
#img2 {
 width: 90%;
}
}

</style>