<template>
  <div v-if="error">{{errorMessage}}</div>
  <div v-else class="container">
    <SearchInput/>
    <RepoCard v-for="item in repositories" :key="item.id" :item="item"/>
  </div>

</template>

<script>
import RepoCard from "@/components/RepoCard.vue";
import {getUserRepositories} from "@/api/repositories";
import SearchInput from "@/components/SearchInput.vue";
export default {
  name: "HomePage",
  components: {
    SearchInput,
    RepoCard
  },
  data:() => {
    return {
      repositories: [],
      show: false,
      error: false,
      errorMessage: ""
    }
  },
  methods: {
    async handleSearchUser() {
      const result = await getUserRepositories("kamils224");
      if (result.error) {
        this.errorMessage = result.error;
      } else {
        this.repositories = result.data;
      }
    }
  },
  mounted() {
    this.handleSearchUser();
  }
}
</script>

<style scoped>
.container {
  margin: auto;
  width: 60%;
  padding: 10px;
  box-shadow: 0 3px 10px rgb(0 0 0 / 0.2);
  min-height: 90vh;
  background: white;
}

@media only screen and (max-width: 1000px) {
  .container {
    width: 90%;
  }
}
</style>