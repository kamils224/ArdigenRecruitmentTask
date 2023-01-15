<template>
  <a-layout>
    <a-layout-header class="site-layout-header">
      <h2 class="header-title">List GitHub repositories by username</h2>
    </a-layout-header>
    <a-layout-content class="site-layout-content">
      <a-row justify="center">
        <a-col :span="24" :sm="12" :lg="8">
          <SearchInput
            :initial-value="username"
            @search="handleSearchUser"
            :loading="loading"
          />
        </a-col>
      </a-row>
      <a-row justify="center">
        <a-col>
          <RepoList :repositories="repositories" />
        </a-col>
      </a-row>
    </a-layout-content>
    <a-layout-footer class="site-layout-footer">
      <a-row justify="center">
        <a-col>
          <SimplePagination
            @previous-page="previousPage"
            @next-page="nextPage"
            :current-page="this.page"
          />
        </a-col>
      </a-row>
    </a-layout-footer>
  </a-layout>
</template>

<script>
import { getUserRepositories } from "@/api/repositories";
import SearchInput from "@/components/SearchInput.vue";
import SimplePagination from "@/components/SimplePagination.vue";
import RepoList from "@/components/RepoList.vue";

export default {
  name: "HomePage",
  components: {
    RepoList,
    SimplePagination,
    SearchInput,
  },
  data: () => ({
    repositories: [],
    currentPage: 1,
    loading: false,
    error: false,
    errorMessage: "",
    username: "",
    page: 1,
  }),
  methods: {
    async loadUserRepositories(username, page = 1) {
      if (!username) {
        return;
      }
      this.loading = true;
      const result = await getUserRepositories(username, page);
      if (result.error) {
        this.errorMessage = result.error;
      } else {
        this.repositories = result.data;
      }
      this.loading = false;
    },
    async handleSearchUser(username) {
      await this.$router.push({ name: "home", query: { username } });
    },
    async nextPage() {
      await this.$router.push({
        name: "home",
        query: {
          username: this.$route.query.username,
          page: +this.page + 1,
        },
      });
    },
    async previousPage() {
      await this.$router.push({
        name: "home",
        query: {
          username: this.$route.query.username,
          page: +this.page - 1,
        },
      });
    },
  },
  beforeMount() {
    this.username = this.$route.query.username;
    this.page = this.$route.query.page || 1;
  },
  async mounted() {
    await this.loadUserRepositories(this.username, +this.page);
  },
};
</script>

<style scoped>
.site-layout-header {
  min-height: 10vh;
}
.site-layout-header > h2 {
  color: white;
  font-weight: 600;
  text-align: center;
}
.site-layout-content {
  min-height: 80vh;
  padding: 24px;
}
.site-layout-footer {
  min-height: 10vh;
  padding: 24px;
}
</style>
