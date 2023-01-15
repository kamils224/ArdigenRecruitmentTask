import { createApp } from "vue";
import { createWebHistory, createRouter } from "vue-router";
import Antd from "ant-design-vue";
import App from "./App.vue";
import "ant-design-vue/dist/antd.css";
import routes from "./routers.js";

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);
app.use(router);

app.mount("#app");

app.config.productionTip = false;

app.use(Antd);
