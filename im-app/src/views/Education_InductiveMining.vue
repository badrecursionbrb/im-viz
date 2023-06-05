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

    <h2>Inductive Mining</h2>
  <br />
      <h3>What is Inductive Mining?</h3>
      <br />

    

        <p style="font-size: large;"><strong>Inductive Mining </strong>refers to a group of process
          discovery algorithms (IM, IMF, IMC, IMD, IMFD, IMCD,
          etc.), which provide high flexibility, formal guarantees, and are scalable. It is a a common go-to technique in
          research. The standard Inductive Miner as well as the infrequent variant can be used in this application.</p>

        <br />
          <p style="font-size: large;"></p> The central idea of Inductive Mining is to discover processes in a
          <strong>divide-and-conquer manner</strong>, by iteratively
          splitting an event log into smaller parts. It uses a intermediary representation <a href="processtree">(process
            trees)</a>, which ensures soundness and
          neatly aligns with the nature of the inductive mining approach.
          <br /><br />
          <hr id="hr-edge-weak">
          <br />
   
   

      <h4>How is divide-and-conquer embodied in Inductive Mining?</h4>
      <br />
     

        <p style="font-size: large;"> The inductive miner aims to split
          the event log recursively into sublogs. Examples are given as follows <a href="ProjectDoc">[4]</a>:</p>
      
      <br />
     
        <img id="dnc1" src=@/assets/dnc1.png />
        <img id="dnc2" src=@/assets/dnc2.png/>
    </v-container>

</template>

<style>
#btngroup{
  background-color:rgb(208, 208, 0,0);
  color:white;
  text-align: center !important;
}
#dnc1 {
  width: 80% ;
  height:80% ;
}
#dnc2 {
  width: 80% ;
  height: 80% ;
}

@media (max-width: 600px){
#dnc1 {
  width: 100% ;

}
#dnc2 {
  width: 100% ;

}
}
#hr-edge-weak {
  border: 0;
  padding-top: 0.5vh;
  background: linear-gradient(to right, transparent, #d0d0d5, transparent);
}

#content {
  max-width: 90vw;
  margin-left: 5vw ;
  margin-right: 5vw;
  margin-bottom: 20vh;
  align-self: center;
  font-size: 3vh;
  color: white;
  text-align: left;
}
</style>