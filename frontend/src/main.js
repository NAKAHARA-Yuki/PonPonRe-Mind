import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'

Vue.prototype.$http = axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL
})

new Vue({
  render: h => h(App),
}).$mount('#app')
