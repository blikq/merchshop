import './assets/main.css'

import { createApp } from 'vue/dist/vue.esm-bundler';
import App from './App.vue'
import store from './store';
import 'vuex';

// const index = createApp({
    //     data() {
        //       return {
//         count: 0
//       }
//     }
//   }).mount('#app');
import router from './router'
const app = createApp(App);
// app.config.globalProperties.$store = store;

app.use(router).use(store).mount('#app')
export default app;