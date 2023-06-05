<template>
    <v-sheet id="btngroup">
    <v-btn id="btngroup" bg-color="grey-lighten-3" :rounded="0" variant="flat" href="/processtree">Process Tree</v-btn>
    <v-btn id="btngroup" bg-color="grey-lighten-3" :rounded="0" variant="flat" href="/dfg">DFG</v-btn>
    <v-btn id="btngroup" bg-color="grey-lighten-3" :rounded="0" variant="flat" href="/flower">FlowerModel</v-btn>
    <v-btn id="btngroup" bg-color="grey-lighten-3" :rounded="0" variant="flat" href="/cuts">Cuts</v-btn>
    <v-btn id="btngroup" bg-color="grey-lighten-3" :rounded="0" variant="flat" href="/processdiscovery">Process Discovery</v-btn>
    <v-btn id="btngroup" bg-color="grey-lighten-3" :rounded="0" variant="flat" href="/indumining">Inductive Mining</v-btn>
  </v-sheet>

    <v-container id="cont">
        <h2>Cuts</h2> 
      <br/>  
      <h3>What are cuts in Inductive Miner?</h3>
      <br/>
      <p style="font-size: large;">The basic idea of Inductive Miner is about detecting a <strong>'cut'</strong>  in the log and then recur on sublogs, which were found applying the cut, until a base case is found. </p>
        There are in total 4 types of cuts in the context of Inductive Mining. The following picture is taken from Process Mining Handbook<a href="/ProjectDoc"> [4] </a>, which simply illustrates differences between different cuts.
        <br/>
        <br/>
        
        <img src="@/assets/cut.png" id="resized">
        <br/>
        <br/>
          
        
        Now let's dive deeper into some pseudo codes to know how these functions realize everything<a href="/ProjectDoc"> [5]</a> :
          <br/>
          <br/>
        <img src="@/assets/sequence.png" id="icon"> &nbsp;<strong>The original function of A Sequence Cut:</strong> <br/>
          <img src="@/assets/sequencecut.png" id="image1"><br/>
          <img src="@/assets/sequentialcutfootprint.png" id="image2"><br/>
          <fieldset id="test"> 
           
            <div> For any two nodes a ∈ ∑ 𝑖, b ∈ ∑ 𝑗, i ≤ j, there is a path from a to b, but not vice versa​</div>
          </fieldset>
          <br/>
          <br/>
        <img src="@/assets/XOR.png" id="icon">&nbsp; <strong>The original function of An Exclusive Cut:</strong> 
        <br/>
          <img src="@/assets/exclusivecut.png" id="image3"><br/>
          <img src="@/assets/exclusivecutfootprint.png" id="image4"><br/>
          <fieldset id="test"> 
            
            <div> No two nodes a ∈ ∑ 𝑖, b ∈ ∑ 𝑗, i ≠ j are connected.</div>
          </fieldset>
          <br/>
          <br/>
          <img src="@/assets/AND.png" id="icon">&nbsp; <strong>The original function of A Parallel Cut:</strong> 
          <br/>
          <img src="@/assets/concurrent.png" id="image5"><br/>
          <img src="@/assets/concurrentcutfootprint.png" id="image6"><br/>
          <fieldset id="test"> 
           
            <div>Each ∑ 𝑖 has a start and an end node, and any two nodes a ∈ ∑ 𝑖, b ∈ ∑ 𝑗, i ≠ j are connected by edges (𝑎, 𝑏) and (𝑏, 𝑎).​</div>
          </fieldset>
          <br/>
          <br/>
          
          <img src="@/assets/loop.png" id="icon">&nbsp; <strong>The original function of A Loop Cut:</strong> 
          <br/>
          <img src="@/assets/loopcut.png" id="image7"><br/>
          <img src="@/assets/Loopcutfootprint.png" id="image8"><br/>
          <fieldset id="test"> 
            <div>Each ∑ 𝑖 has a start and an end node, and no two nodes a ∈ ∑ 𝑖, b ∈ ∑ 𝑗, i, j > 1 are connected, and any edge between ∑₁ and ∑𝑖, i > 1 either leaves an end node of ∑₁ or reaches a start node of ∑₁​.</div>
          </fieldset>
          <br/>
      Now you are well prepared to read more about <a href="processtree">Process Tree</a>.

      <br/>
      <br/> 
      <br/>
      <br/>
      <br/>
    </v-container>   
</template>
<style>
#btngroup{
  background-color:rgb(208, 208, 0,0);
  color:white;
  text-align: center !important;
}
#cont {
  max-width: 90vw;
  margin-left: 5vw;
  margin-right: 5vw;
  font-size: 3vh;
  color: white;
  text-align: left;
}

#icon {
      width: 2vw;
      height: 3vh;
      
    }

#resized {
      width: 40vw;
      
    }

#image1 {
      width: 40vw;
     
     
    }

#image2 {
     width: 40vw;
   
     
    }
#image3 {
      width: 30vw;
      
    
    }
 #image4 {
  width: 40vw;
    
      
    }
#image5 {
  width: 40vw;
   
    }
#image6 {
  width: 40vw;
  
    }
#image7 {
  width: 40vw;
   
      
    }
#image8 {
  width: 40vw;
     
  }
  @media (max-width: 600px){
    #icon {
      width: 5vw;
      height: 3vh;
      
    }

#resized {
      width: 80vw;
      
    }

#image1 {
      width: 80vw;
     
     
    }

#image2 {
     width: 80vw;
   
     
    }
#image3 {
      width: 80vw;
      
    
    }
 #image4 {
  width: 80vw;
    
      
    }
#image5 {
  width: 80vw;
   
    }
#image6 {
  width: 80vw;
  
    }
#image7 {
  width: 80vw;
   
      
    }
#image8 {
  width: 80vw;
     
  }
  }
</style>