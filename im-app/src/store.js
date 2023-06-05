import { miserablesJson } from "./components/seedData";
import { tableData } from "./components/seedData";
import {reactive} from "vue";

const state = reactive({
    miserablesJson,
    tableData
});

const getters = {};

const mutations = {};

export default {
    state : state,
    getters, 
    mutations,
};





