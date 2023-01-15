<template>
  <a-card headStyle="font-weight: bold;" :title="item.name" class="main-card">
    <template #extra
      ><a :href="item.htmlUrl" target="_blank">source</a></template
    >
    <a-card-grid class="card-grid">
      <p class="language">Language: {{ item.language }}</p>
      <p v-if="item.description">{{ item.description }}</p>
      <p v-else class="no-description">No description</p>
    </a-card-grid>
    <a-card-grid class="card-grid">
      <p>Created at: {{ new Date(item.createdAt).toDateString() }}</p>
      <p>Updated at: {{ new Date(item.updatedAt).toDateString() }}</p>
    </a-card-grid>
    <a-card-grid class="card-grid">
      <a-collapse accordion>
        <a-collapse-panel :key="item.id" header="Details">
          <a-space class="details-section" :size="10">
            <div v-for="detail in getDetailsDisplay(item)" :key="detail.title">
              <component :is="detail.icon" />
              {{ detail.title }}: {{ detail.text }}
            </div>
          </a-space>
        </a-collapse-panel>
      </a-collapse>
    </a-card-grid>
  </a-card>
</template>

<script>
import {
  StarOutlined,
  EyeOutlined,
  BranchesOutlined,
  WarningOutlined,
  DatabaseOutlined,
} from "@ant-design/icons-vue";

export default {
  name: "RepoCard",
  components: {
    StarOutlined,
    EyeOutlined,
    BranchesOutlined,
  },
  props: {
    item: {
      required: true,
    },
  },
  methods: {
    getDetailsDisplay(item) {
      return [
        {
          title: "Stargazers",
          text: item.stargazersCount,
          icon: StarOutlined,
        },
        {
          title: "Watchers",
          text: item.watchersCount,
          icon: EyeOutlined,
        },
        {
          title: "Forks",
          text: item.forksCount,
          icon: BranchesOutlined,
        },
        {
          title: "Open issues",
          text: item.openIssues,
          icon: WarningOutlined,
        },
        {
          title: "Size",
          text: `${item.size} kB`,
          icon: DatabaseOutlined,
        },
      ];
    },
  },
};
</script>

<style scoped>
.main-card {
  width: 50vw;
  margin: 10px;
  background-color: white;
}
.details-section {
  display: flex;
}
@media (max-width: 900px) {
  .main-card {
    width: 90vw;
  }
}
@media (max-width: 1200px) {
  .main-card {
    width: 75vw;
  }
}
@media (max-width: 600px) {
  .details-section {
    display: block;
  }
}
.language {
  font-weight: 600;
}
.card-grid {
  width: 100%;
}
.card-grid:nth-child(1) {
  width: 50%;
  text-align: left;
}
.card-grid:nth-child(2) {
  width: 50%;
  text-align: right;
}
.main-card .no-description {
  font-style: italic;
  font-weight: 300;
  opacity: 0.6;
}
</style>
