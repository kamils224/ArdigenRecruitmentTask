<template>
  <a-input-search
    v-model="username"
    placeholder="GitHub Username"
    :loading="loading"
    enter-button
    :search="handleSearch"
  />
</template>

<script>
export default {
  name: "SearchInput",
  props: {
    loading: {
      type: Boolean,
      default: false,
    },
    initialValue: {
      type: String,
      default: "",
    },
  },
  data: () => ({
    username: "",
  }),
  methods: {
    handleSearch(value, event) {
      this.$emit("search", value, event);
    },
  },
  beforeMount() {
    this.username = this.initialValue;
  },
};
</script>

<style scoped></style>
