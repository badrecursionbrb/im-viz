import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/HomeScreen.vue';
import ProjectDoc from '../views/ProjectDocumentation.vue';
import Education_LandingPageVue from '../views/Education_LandingPage.vue';
import Education_DFGVue from '../views/Education_DFG.vue';
import Education_ProcessDiscoveryVue from '../views/Education_ProcessDiscovery.vue';
import Education_FlowerModelVue from '../views/Education_FlowerModel.vue';
import Education_ProcessTreeVue from '../views/Education_ProcessTree.vue';
import Education_CutsVue from '../views/Education_Cuts.vue';
import Education_InductiveMiningVue from '../views/Education_InductiveMining.vue';
import ProjectDocumentationVue from '../views/ProjectDocumentation.vue';

const routes = [
    {
        path: '/',
        name: 'HomeScreen',
        component: Home
    },
    {
        path: '/studenteducation',
        name: 'StudentEducation',
        component: Education_LandingPageVue
    },
    {
        path: '/projectdoc',
        name: 'projectdoc',
        component: ProjectDoc
    },
    {
        path: '/processdiscovery',
        name: 'discovery',
        component: Education_ProcessDiscoveryVue
    },
    {
        path: '/dfg',
        name: 'dfg',
        component: Education_DFGVue
    },
    {
        path: '/flower',
        name: 'flower',
        component: Education_FlowerModelVue
    },
    {
        path: '/indumining',
        name: 'indumining',
        component: Education_InductiveMiningVue
    },
    {
        path: '/cuts',
        name: 'cuts',
        component: Education_CutsVue
    },
    {
        path: '/processtree',
        name: 'processtree',
        component: Education_ProcessTreeVue
    },
    ,
    {
        path: '/ProjectDoc',
        name: 'documentation',
        component: ProjectDocumentationVue
    },

]




const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router

