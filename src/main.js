import { createApp } from 'vue';
import App from './App.vue';
import { createPinia } from 'pinia'
import 'vuetify/styles'
import '@mdi/font/css/materialdesignicons.css';
import { createVuetify } from 'vuetify'
import { VDateInput } from 'vuetify/labs/VDateInput'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components: {
    ...components,
    VDateInput,
  },
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
