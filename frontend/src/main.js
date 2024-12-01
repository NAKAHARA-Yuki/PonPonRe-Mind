import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'

Vue.prototype.$http = axios.create({
  baseURL: 'http://localhost:5001'
})

new Vue({
  render: h => h(App),
}).$mount('#app')
