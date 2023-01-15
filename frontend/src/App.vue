<template>
  <div>
  <HomePage />
  </div>
</template>

<script>
import HomePage from "@/pages/HomePage.vue";

export default {
  name: 'App',

  components: {
    HomePage
  },

  data: () => ({
  }),
}
</script>

<style lang="scss">
@import "./main.scss";
</style>