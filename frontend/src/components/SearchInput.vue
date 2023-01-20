<template>
  <div>
    <a-input-search
      v-model="username"
      :defaultValue="defaultValue"
      placeholder="GitHub Username"
      :loading="loading"
      enter-button
      :onSearch="handleSearch"
    />
    <p class="error" v-if="error">{{ error }}</p>
  </div>
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
    error: String,
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

<style scoped>
.error {
  color: red;
  margin-left: 10px;
}
</style>
