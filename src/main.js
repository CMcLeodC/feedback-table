import { createApp } from 'vue';
import App from './App.vue';
// import {createBootstrap} from 'bootstrap-vue-next'
// import 'bootstrap/dist/css/bootstrap.css';
// import "bootstrap/dist/css/bootstrap.min.css"
// import "bootstrap"
// import 'bootstrap-icons/font/bootstrap-icons.css'
// import 'bootstrap-vue-next/dist/bootstrap-vue-next.css'
import { createPinia } from 'pinia'
import 'vuetify/styles'
import '@mdi/font/css/materialdesignicons.css';
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
    components,
    directives,
    icons: {
      defaultSet: 'mdi', // Ensure the default icon set is Material Design Icons
    },
  })
const pinia = createPinia()
const app = createApp(App);

// app.use(createBootstrap())
app.use(vuetify)
app.use(pinia)
// app.use(store)
app.mount('#app');
