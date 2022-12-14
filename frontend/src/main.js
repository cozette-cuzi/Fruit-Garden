import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import "@mdi/font/css/materialdesignicons.css";
import axios from "axios";
import api from "@/constants/api";
import events from "./constants/events";
import VueAxios from "vue-axios";
import "./assets/main.css";
import mitt from 'mitt';


const myCustomLightTheme = {
  dark: false,
  colors: {
    background: "#FFFFFF",
    surface: "#FFFFFF",
    primary: "#008b00",
    "primary-darken-1": "#3700B3",
    secondary: "#03DAC6",
    "secondary-darken-1": "#018786",
    error: "#B00020",
    info: "#2196F3",
    success: "#90ee02",
    warning: "#FB8C00",
  },
};
const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: "myCustomLightTheme",
    themes: {
      myCustomLightTheme,
    },
  },
});

const showSnackbar = message => {
  EventBus.$emit(ACTIONS.SNACKBAR, message);
};


axios.defaults.timeout = 1000 * 300;
axios.defaults.baseURL = api.MAIN_URL;

const app = createApp(App);
const emitter = mitt();
app.config.globalProperties.$api = api;
app.config.globalProperties.$events = events
app.config.globalProperties.emitter = emitter;


app.use(VueAxios, axios);
app.use(router);
app.use(vuetify);
app.mount("#app");
