<template>
  <div class="card">{{ item.name }}</div>
</template>

<script>
export default {
  name: "RepoCard",
  props: {
    item: {
      required: true
    }
  }
}
</script>

<style scoped>
.card {
  width: 100%;
  margin: 10px;
  background-color: white;
}
</style>