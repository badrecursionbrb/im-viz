import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import '@fortawesome/fontawesome-free/js/all'
import "@ssthouse/vue3-tree-chart/dist/vue3-tree-chart.css";
import '@mdi/font/css/materialdesignicons.css'
// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@/Fallback.js';
const vuetify = createVuetify({
  ssr: true,
  components,
  directives,
})


createApp(App).use(vuetify).use(router).mount('#app')

