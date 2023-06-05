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

          <h2>Process Discovery</h2>
          <br />
          <h4>Could you shortly describe process discovery?</h4>
          <br />


          <p style="font-size: large;"><strong>Process discovery </strong>describes approaches to transform
            event data into a process model that reflects this data.</p>
          <br />

          <hr id=hr-edge-weak>
          <br />
          <h4>What are event data and event logs?</h4>
          <br />



          <p style="font-size: large;"><strong>Event data</strong> can be found and collected from a variety
            of sources such as a database system (e.g., customer data from CRM system), a comma-separated values (CSV) file
            and so on.
            Here is an examples you might see in real-life <a href="ProjectDoc">[3][4]:</a></p>

          <br />

          <img id="ev2" src='@/assets/eventdata2.png' />

          <br />


          An event log can be considered as a collection of cases. Each case can be seen as a trace, i.e., a sequence of
          events corresponding to the
          same case, e.g., &lt;e1, e2, e3&gt;.
          For an event log, we generally assume three basic requirements:
          <ul>
            <li> – Each event in a log refers to exactly one case. </li>
            <li>– Each event is associated with an activity, indicating its type (e.g., check request)</li>
            <li>– The order of events per case is known</li>
          </ul>
          Other aspects of event logs (lifecycles, timestamps, resources, data, etc.) are helpful or
          required for certain scenarios, but not generally assumed to be present.
          <br /><br />
          The follwing event log L can be noted as L = [&lt;a,b,d,e,h&gt;2, &lt;a,d,c,e,g&gt;2, &lt;a,c,d,e,f,b,d,e,g&gt;,
          &lt;a,c,d,e,f,d,c,e,f,c,d,e,h&gt;]. This trace format is also utilized in our application.
          <br /><br />

          <img id="ev" src="@/assets/eventlog.png">

          <br />






          <br />

          <hr id="hr-edge-weak">
          <br />
          <h4> What is a process discovery algorithm?</h4>
          <br />

          <p style="font-size: large;"><strong>A process discovery algorithm</strong> is a function that
            maps the event log onto a process model such that the model is “representative” for the behavior seen in the
            event log.</p>
          <br />
          There is a trade-off between the following four quality criteria while generating process models <a
            href="ProjectDoc">[3]</a>:
          <br />
          <ul>
            <li>Fitness: Can the model explain the observed behavior?</li>
            <li>Simplicity: Is the model as simple as possible ("Occam's razor")?</li>
            <li>Generalization: Does the discovered model overfit the event log?</li>
            <li>Precision: Is the model underfitting the event log?</li>
          </ul>
          <br />
          <p style="font-size: large;"> Some examples of process discovery algorithms include heuristics-based approaches,
            inductive miner, and genetic algorithms. </p>
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
           
    

          </v-container>
</template>

<style>
#btngroup{
  background-color:rgb(208, 208, 0,0);
  color:white;
  text-align: center !important;
}

  #content {
  max-width: 90vw;
  margin-left: 5vw;
  margin-right: 5vw;
  align-self: center;
  font-size: 3vh;
  color: white;
  text-align: left;
  }
  #ev {
    height: 65%;
    width: 50%;
  }

  #ev2 {
    height: 45%;
    width: 50%;
  }
@media (max-width: 600px) {
  #ev {
    width: 90%;
  }

  #ev2 {
    width: 90%;
  }
}
  #hr-edge-weak {
    border: 0;
    padding-top: 0.5vh;
    background: linear-gradient(to right, transparent, #d0d0d5, transparent);
  }

</style>