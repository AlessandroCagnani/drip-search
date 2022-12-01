import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import  CCard  from "@coreui/vue/";


createApp(App).use(store).use(router).use(CCard).mount('#app')
