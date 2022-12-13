import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css'
import axios from 'axios'
import api from '@/constants/api';
import VueAxios from 'vue-axios'

import './assets/main.css'

const vuetify = createVuetify({
  components,
  directives,
})
axios.defaults.timeout = 1000 * 300;
axios.defaults.baseURL = api.MAIN_URL;
// Vue.prototype.api = api 

const app = createApp(App)
app.config.globalProperties.$api = api;
app.use(VueAxios, axios)
app.use(router)
app.use(vuetify)
app.mount('#app')