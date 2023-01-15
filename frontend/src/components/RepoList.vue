<template>
  <div>
    <RepoCard v-for="item in repositories" :key="item.id" :item="item" />
  </div>
</template>

<script>
import RepoCard from "@/components/RepoCard.vue";

export default {
  name: "RepoList",
  components: { RepoCard },
  props: {
    repositories: {
      required: true,
    },
  },
};
</script>

<style scoped></style>
