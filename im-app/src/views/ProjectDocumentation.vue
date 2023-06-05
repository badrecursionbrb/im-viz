<template>
 
  <v-container id="container">
    <h2>Documentation</h2>
    <br />
    <h3>Introduction</h3>
    <hr id="hr-edge-weak">
    <br />
    <p>The Inductive miner visualizer is an interactive, user-friendly and intuitive platform developed by a group
            of process mining lovers from University of Mannheim in 2023. </p>
    <p>The whole project is under the guidance and support of chair of Process Analytics. With the given
            functionalities from our visualization tool, intermediate and final results of the inductive miner algorithm
            shall be displayed in an easily understandable way. The application ought to be stable, easy to access and to
            navigate. Extensions are also possible.</p>
    <br />
    <br />
    <h3>How it works</h3>
    <hr id="hr-edge-weak">
    <br />
    <p>This web application is powered by <strong>Vue.js</strong> and <strong>Flask Python</strong>. The algorithm
        visualization is realized through <strong>D3</strong>, which stands for Data-Driven Documents. Additionally,
    <strong>cola.js</strong> is built on D3, making it easy to integrate with other data visualization libraries
            and frameworks. </p>
    <br />
    <p>The standard Inductive mining algorithm is implemented in this application by utilizing the latest PM4PY
            library (March 2023). </p>
    <br />
    <img id="architecture_png" src="@/assets/architecture.png" >
    <br />
    <br />
    <h3>Getting started</h3>
    <hr id="hr-edge-weak">
    <br />
    <h3>- Home </h3>
    <p>The Home screen is an intutive and interactive panel comprised by the process tree pane, the real-time DFG
              and trace pane and the algorithm detection pane, which shows the algorithm on the left hand side and the describtion to the current step on the right hand side.</p>
    <br />
    <p>There are 2 ways of providing event logs:
    <li>Upload the existing event log in CSV/XES format by clicking the File-Input field at the bottom of the page </li>
    <li>Enter the trace&nbsp; <mark> &nbsp; (e.g. &lt;a, b, c&gt;3; &lt;a, b, d&gt;2;) </mark>&nbsp; in the
                textbox underneath the process tree pane. </li>
    </p>
    <p>Once the event log is received, all panes will display the corresponding information. The "back" and "next"
              buttons on the process tree pane enable the control over the step-by-step visulization of process trees. The
              present status of the prcess tree, DFG and traces are updated synchronously. In the meantime, the related
              algorithm part will be highlighted. DFGs and process trees visualization support drag operations. </p>
    <br />
    <h3>- Education </h3>
    <p>In the section "Education", different keywords and concepts such as DFG, process tree, flower model, etc.
              are explicitly explained in detail in reference of all available resources. To get more information, please
              read reference. </p>
    <br />
    <br />

      <h3>Reference</h3>
          <hr id="hr-edge-weak">
          <br/>
          <ul>
            <li> [1] PM4PY Documentation:<a
                href="https://pm4py.fit.fraunhofer.de/documentation">https://pm4py.fit.fraunhofer.de/documentation</a>​
            </li>
            <li> [2] An Inductive Miner Implementation for the PM4PY Framework: <a
                href="https://www.pads.rwth-aachen.de/global/show_document.asp?id=aaaaaaaaajqshho&download=1">https://www.pads.rwth-aachen.de/global/show_document.asp?id=aaaaaaaaajqshho&download=1</a>(page 10,
              12)</li>
            <li> [3] Process and Data Science Group - RWTH Aachen University: <a
                href="https://www.processmining.org/home.html">https://www.processmining.org/home.html</a>​</li>
            <li> [4] Process Mining Handbook: <a
                href="https://link.springer.com/book/10.1007/978-3-031-08848-3">https://link.springer.com/book/10.1007/978-3-031-08848-3</a>
              ​(pages 129, 189, 224, 226, 228)</li>
            <li> [5] Robust Process Mining with Guarantees: <a
                href="https://link.springer.com/book/10.1007/978-3-030-96655-3">https://link.springer.com/book/10.1007/978-3-030-96655-3</a>​
              (pages 125-126/188-190)​</li>
          </ul>
    
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
 
</v-container>  
</template> 
<style>
#hr-edge-weak {
  border: 0;
  padding-top: 1px;
  background: linear-gradient(to right, transparent, #d0d0d5, transparent);
}

#container {
  max-width: 90vw !important;
  margin-left: 4vw ;
  margin-right: 4vw ;
  color: #fcfcff;
  text-align: left ;
  align-self: center;
  contain: content;
}

#architecture_png {
  width: 70% !important;
 }

@media (max-width: 600px){
 #architecture_png {
  width: 100% !important;
 }
}


</style>

