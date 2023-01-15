<template>
<div>
  <input type="text" placeholder="Search.." name="search">
  <button type="submit">Search</button></div>
</template>

<script>
export default {
  name: "SearchInput",
  data: () => {
    return {
      search: ""
    }
  },
  methods: {
    onSearch() {
      console.log("search");
    }
  }
}
</script>

<style scoped>

</style>