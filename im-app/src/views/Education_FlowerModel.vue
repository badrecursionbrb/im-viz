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
   <h2>Flower Model</h2>

    <br />
   <h3>What is a flower model?</h3>

        <br />
        <p style="font-size: large;"><strong>A flower model </strong>is an example of fall throughs, i.e.
          it allows for any behaviour
          (i.e. traces) of a, b, c, d, e, f, g and h (see the picture below). It is therefore perfectly fitting and
          general, but not log precise as it describes much more behaviour than seen in the event log <a
            href="/ProjectDoc">[4]</a>. </p>
      
            <br />
      <hr id="hr-edge-weak">
      <br />
      <img id="fm_png" src="@/assets/fm.png">

      <br />
      <br />
      <hr id="hr-edge-weak">

      <br />
      <h3>When a fall through will be returned?</h3>
      <br />
        <p style="font-size: large;">The IM framework defines four steps<a href="resources"> [5]: </a></p>
        <ul>
          <p style="font-size: large;">1. First, a cut is detected.</p>
          <p style="font-size: large;">2. Second, the event log is split into smaller sublogs.</p>
          <p style="font-size: large;">3. Third, the IM framework recurses on these
            sublogs until a base case (subprocesses consisting of a single activity executed once per case) is
            encountered.</p>
          <p style="font-size: large;">4. And fourth, if no cut can be found, <strong>a fall through</strong>
            is returned.</p>
        </ul>
        <p style="font-size: large;">Other than flower models, there are other types of fall throughs such as TAULoop, ActivityOncePerTrace,
        EmptyTraces, etc. You can find more information in the reference<a href="resources"> [5]</a>.</p>
        <br />
        <br />
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
  max-width: 90vw ;
  margin-left: 5vw ;
  margin-right: 5vw ;
  color: #fcfcff;
  text-align: left ;
  align-self: center; 
}

#hr-edge-weak {
  border: 0;
  padding-top: 1px;
  background: linear-gradient(to right, transparent, #d0d0d5, transparent);
}
#fm_png{
 width: 60%;
}
@media (max-width: 600px){
  #fm_png{
 width: 100%;
 
}
}

</style>