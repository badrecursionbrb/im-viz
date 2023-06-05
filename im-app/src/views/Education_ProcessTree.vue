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
      <h2>Process Tree</h2>
      <br />
      <h3>What is a process tree?</h3>
      
      <br />
      <p style="font-size: large;"> <strong>A process tree </strong>is a hierarchical process model where
          the (inner) nodes are operators such
          as sequence and choice and the leaves are activities. </p>
      <br />
      <p style="font-size: large;">By using process trees, discovery algorithms and conformance checking techniques need
          not to worry about soundness, as soundness is guaranteed by
          construction, while both Petri nets and BPMN models might suffer from soundness issues.</p>
      <br />
      <hr id="hr-edge-weak">
      <br />
      <h3>How are process trees related to dfg?</h3>
      <br />
        <p style="font-size: large;"> The language of a process tree operator is a combination of the
          languages of its children, namely activities. Our application serves exactly as a tool to help you better
          understand the whole process of generating process trees from dfgs. The following example may could give you
          some hints <a href="/ProjectDoc">[2]</a>.</p>

      <br />

  
          <img id="dfgPT" src='@/assets/processtreedfg.png'/>
       

     

      <p style="font-size: large;">Here is an example of a dfg and the corresponding process tree.</p>
   
      <br />
      
          <img id="ptDFG" src='@/assets/dfgtoprpcesstree.jpg'/>
          <br />
          <img id="PT2" src='@/assets/processtree2.jpg'/>
          

 </v-container>
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          
</template>
    
<style>
#btngroup{
  background-color:rgb(208, 208, 0,0);
  color:white;
  text-align: center !important;
}
#content {
  max-width: 90vw;
  align-self: center;
  color: white;
  text-align: left;
  margin-left: 5vw ;
  margin-right: 5vw;
  
}
#dfgPT{

  width: 40%;
}
#ptDFG{

 width: 40%;
}
#PT2{

 width: 30%;
}

@media (max-width: 600px){
  #dfgPT{

width: 80%;
}
#ptDFG{

width: 80%;
}
#PT2{

width: 80%;
}
}

#hr-edge-weak {
  border: 0;
  padding-top: 0.5vh;
  background: linear-gradient(to right, transparent, #d0d0d5, transparent);
}
</style>