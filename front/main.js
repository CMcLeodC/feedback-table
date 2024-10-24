import { createApp } from 'vue';
// import App from './App.vue';
import App from './blankpage.vue'

// Import Bootstrap and BootstrapVue 3 CSS files
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css';
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import 'bootstrap-icons/font/bootstrap-icons.css'

// Import BootstrapVue 3 components
import BootstrapVue3 from 'bootstrap-vue-3';
const app = createApp(App);


// Install BootstrapVue 3
app.use(BootstrapVue3);

app.mount('#app');
