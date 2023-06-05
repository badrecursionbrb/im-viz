<template>
  <v-app>
    <v-main>
      <v-toolbar class="toolbarTop" color="black" app>
        <v-toolbar-title class="d-none d-sm-flex">
               IM-Viz
        </v-toolbar-title>

        <v-toolbar-items>
          <v-btn id="tool_btn" flat v-for="item in menuItems" :key="item.title" :to="item.path">
            <v-icon left dark>{{ item.icon }}</v-icon>
            {{ item.title }}
          </v-btn>
        </v-toolbar-items>
      </v-toolbar>
      <div>
        <router-view></router-view>
      </div>
    
    </v-main>

  </v-app>
  
</template>
<script>
export default {

  data() {
    return {
      
      appTitle: 'Inductive Miner',
      sidebar: false,
      menuItems: [
        { title: 'Home', path: '/', icon: 'mdi-home' },
        { title: 'Education', path: '/studenteducation', icon: 'mdi-school' },
        { title: 'Documentation', path: '/projectdoc', icon: 'mdi-file-document ' },
      ]
    }
  },
}
</script>
<style>
@media (min-width: 451px) {
  .v-toolbar-title {
    font-size: 3.5vh !important;
    font-weight: 401 !important;
    text-align: left !important;
    line-height: 4vh !important;
    display: flex !important;
    vertical-align: middle !important;
    align-items: center !important;
  }
  .v-btn{
    min-width: none !important;
  }
  
  .toolbarTop{
    height: 6vh;
  }

  .v-toolbar__content{
    flex: 1 1 auto !important;
  }

  .v-toolbar-items{
    height: auto !important;
  }
}
@media (max-width: 450px) {
  .v-toolbar-title {
    font-size: 3vh !important;
    font-weight: 401 !important;
    text-align: left !important;
    line-height: 4vh !important;
    vertical-align: middle !important;
    align-content: center  !important;  
  }
  .v-toolbar-items{

    padding-left: 4vw ;
    padding-right: 4vw ;
  }

  .toolbarTop{

  }

.v-toolbar__content{
    justify-content: center !important;
  }
  .v-btn__content {
   font-size: 0.75rem !important;
  }
  h2{
  color: #fcfcff;
  font-size: 4.7vh !important;
}

h3{
  color: #fcfcff;
  font-size: 3vh !important;
}
p{
font-size: 2.2vh !important;
}
}
@media (max-width: 400px) {
  
  .v-btn__content {
   font-size: 0.65rem !important;
  }
}

.v-main{
  background-image: radial-gradient(#000000, #343132) !important;
  background-size: cover !important;
  overflow: scroll;  
  width: 100vw !important; 
  height: 100vh !important;  
  position: fixed !important;
}
.v-btn.v-theme--light.text-black.v-btn--density-default.v-btn--size-default.v-btn--variant-text{
 margin: 0%;
}
#app {

  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  
  
}

body {
  font-family: "Helvetica Neue", Helvetica, sans-serif;
  width: 100vw !important; 
  /* height: 100vh !important;  */
  background-image: radial-gradient(#000000, #343132) !important;
 
  /* overflow: scroll;  */
  position: fixed;
  margin: 0 !important;
}

html {
  min-width: none !important;
  overflow: hidden !important;  
  font-size: 0.9rem !important;
}



i {
  margin-right: 0.2vw !important;
}

.v-icon--size-default {
  font-size: calc(var(--v-icon-size-multiplier) * 1.8em) !important;
}
@media (min-width: 401px) {
h2{
  color: #fcfcff;
  font-size: 5vh !important;
}

h3{
  color: #fcfcff;
  font-size: 4vh !important;
}
p{
font-size: 3vh !important;
}
}


ul {
  list-style: none; 
}
a {
  color: rgb(140, 181, 221);
  line-break:strict;
  font-size: medium !important;
}
li {
  margin-bottom: 1vh !important;
  max-width: 80vw !important;
  line-break:strict;
}
mark {
  background-color: black;
  color: white;
}
</style>

