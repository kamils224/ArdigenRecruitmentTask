<template>
  <a-input-search
    v-model="username"
    :defaultValue="defaultValue"
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
    defaultValue: {
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
};
</script>

<style scoped></style>
