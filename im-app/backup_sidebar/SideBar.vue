<script>
import SidebarLink from './SidebarLink';
import { collapsed, toggleSidebar, sidebarWidth } from './DocState'

export default {
    props: {},
    components: {SidebarLink},
    setup(){
        return {collapsed,toggleSidebar,sidebarWidth}
    }
}
</script>

<template>
    <div class="SideBar" :style="{width: sidebarWidth}">
        <h1>
            <span v-if="collapsed">
                 <img class="ImLogo" src= @/assets/im_logo.png/>
            </span>
            <span v-else>Inductive Miner
                <img class="ImLogo" src= @/assets/im_logo.png/>
            </span>
        </h1>

         <SidebarLink to="/" icon="fas fa-home">Home</SidebarLink>
         <SidebarLink to="/studenteducation" icon="fas fa-chalkboard-user">Education</SidebarLink>
         <SidebarLink to="/projectdoc" icon="fas fa-book">Documentation</SidebarLink>
         <SidebarLink to="/test" icon="fas fa-book">test</SidebarLink>

        <span 
            class="collapse-icon"
            :class="{ 'rotate-180' : collapsed }"
            @click="toggleSidebar"
            >
            <i class="fas fa-angle-double-left" />
        </span>
    </div>
</template>

<style>
:root {
    --sidebar-bg-color: #516D82; 
    --sidebar-item-hover: #0091ff;  
    --sidebar-item-active: #919690; 
}
</style>

<style scoped>
.SideBar {
    color: rgb(255, 255, 255);
    background-color: var(--sidebar-bg-color);

    float: left;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    bottom: 0;
    padding: 0.5em;
    
    transition: 0.3s ease;
    
    display: flex;
    flex-direction: column;
}
.SideBar h1 {
    height: 2.5em;
}
.collapse-icon {
    position: absolute;
    bottom: 0;
    padding: 0.75em;
    color: rgb(255, 255, 255);
    transition: 0.2s linear;
}
.rotate-180 {
    transform: rotate(180deg);
    transition: 0.2s linear;
}
.ImLogo{
  contain: content;
  border-radius: 10px;
  width: 45px;
  height: 50px;
  position: absolute;
  left: 5px;
  top: 65px;
}
</style>
