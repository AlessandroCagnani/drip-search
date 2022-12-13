import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import CoreuiVue from '@coreui/vue';
import VueCollapsiblePanel from '@dafcoe/vue-collapsible-panel'

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"




createApp(App).use(store).use(router).use(VueCollapsiblePanel).use(CoreuiVue).mount('#app')
