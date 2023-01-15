<template>
  <a-space>
    <a-button @click="previousPage" :disabled="disablePreviousButton()"
      >Previous Page</a-button
    >
    <a-button @click="nextPage" type="primary" :disabled="disableNext"
      >Next Page</a-button
    >
  </a-space>
</template>

<script>
export default {
  name: "SimplePagination",
  props: {
    currentPage: {
      type: Number,
      required: true,
    },
    disableNext: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    nextPage() {
      this.$emit("nextPage", this.currentPage + 1);
    },
    previousPage() {
      if (!this.disablePreviousButton()) {
        this.$emit("previousPage", this.currentPage - 1);
      }
    },
    disablePreviousButton() {
      return this.currentPage <= 1;
    },
  },
};
</script>

<style scoped></style>
