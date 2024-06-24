import './assets/main.css'

import { createApp } from 'vue/dist/vue.esm-bundler';
import App from './App.vue'



// const index = createApp({
//     data() {
//       return {
//         count: 0
//       }
//     }
//   }).mount('#app');

import router from './router'

createApp(App).use(router).mount('#app')
