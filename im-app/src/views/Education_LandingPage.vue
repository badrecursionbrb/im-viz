<template>
   <v-container id="con">
    <v-row justify="space-around">
      <v-col cols="7" xs="7" sm="7" md="4" lg="4" xl="4">
        
        <v-card id="edu_cards" href="/processtree" title="Process Tree" >
          <img  id="PT_card" src="@/assets/processtree2.jpg"/>
        </v-card>
       
        <v-card id="edu_cards" href="/dfg" title="DFG">
          <img id="dfg_card" src="@/assets/dfg2.png"/>
        </v-card>
        
        </v-col>
        <v-col cols="7" xs="7" sm="7" md="4" lg="4" xl="4">
        
          <v-card id="edu_cards" href="/flower" title="Flower Model">
          <img id="fm_card" src="@/assets/fm.png"/>
          </v-card>
       
        <v-card id="edu_cards" href="/cuts" title=" Cuts">
          <img id="cuts_card" width="220" src="@/assets/dnc1.png/">
        </v-card>

        </v-col>
        <v-col cols="7" xs="7" sm="7" md="4" lg="4" xl="4">

          <v-card id="edu_cards" href="/processdiscovery" title="Processdiscovery">
            <img  id="pd_card" src="@/assets/eventlog.png"/>
          </v-card>
       
        <v-card id="edu_cards" href="/indumining" title="Inductive Mining">
          <img id="IM_card" src="@/assets/im_viz_app.png"/>
        </v-card>
       
        
        </v-col>
    </v-row>
    <br />
    <br />
    <br />
    <br />
    <br />
  </v-container>
</template>
<style>
#con{
  align-items: center !important; 
  margin-top: 5%;
  margin-bottom: 5%;
}

#edu_cards{
  height:30vh;  
  margin-bottom: 3vh;
}
#edu_cards:hover {
  box-shadow: 0px 0px 10px 10px rgb(209, 215, 215) !important;
}
@media (min-width: 1905px) {
  #PT_card{
    width: 10vw; align-items: center !important;
    
  }
  #fm_card{
    width: 20vw; align-items: center !important;

  }
  #pd_card{
    width: 23vw; align-items: center !important;

  }
  #dfg_card{
    width: 15vw; align-items: center !important;

  }
  #cuts_card{
    width: 23vw; align-items: center !important;

  }
  #IM_card{
    height: 20vh; align-items: center !important;
  
  }
}


@media (min-width: 1265px) and (max-width: 1904px) {
  #PT_card{
    width: 10vw; align-items: center !important;
    
  }
  #fm_card{
    height: 20vh; align-items: center !important;

  }
  #pd_card{
    width: 23vw; align-items: center !important;

  }
  #dfg_card{
    width: 15vw; align-items: center !important;

  }
  #cuts_card{
    width: 22vw; align-items: center !important;

  }
  #IM_card{
    height: 20vh; align-items: center !important;
  
  }
}
@media (min-width: 601px) and (max-width: 1264px) {
  #PT_card{
    width: 55%; align-items: center !important; 
    
  }
  #fm_card{
    width: 95% !important; align-items: center !important;

  }
  #pd_card{
    width: 95% !important; align-items: center !important;

  }
  #dfg_card{
    width: 85% !important; align-items: center !important;

  }
  #cuts_card{
    width: 95% !important;align-items: center !important; 

  }
  #IM_card{
    height: 65% !important; align-items: center !important;
  
  }
}
  @media (max-width: 600px) {
  #PT_card{
    width: 80% !important; align-items: center !important; 
    
  }
  #fm_card{
    width: 95% !important; align-items: center !important;

  }
  #pd_card{
    width: 95% !important; align-items: center !important;

  }
  #dfg_card{
    width: 95% !important; align-items: center !important;

  }
  #cuts_card{
    width: 95% !important;align-items: center !important; 

  }
  #IM_card{
    height: 65% !important; align-items: center !important;
  
  }
}



</style>