import axios from "@/api/axiosInstance";

class Repository {
  constructor(
    id,
    name,
    description,
    htmlUrl,
    stargazersCount,
    watchersCount,
    language,
    forksCount,
    size,
    openIssues,
    createdAt,
    updatedAt
  ) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.htmlUrl = htmlUrl;
    this.stargazersCount = stargazersCount;
    this.watchersCount = watchersCount;
    this.language = language;
    this.forksCount = forksCount;
    this.size = size;
    this.openIssues = openIssues;
    this.createdAt = createdAt;
    this.updatedAt = updatedAt;
  }
}

export async function getUserRepositories(username, page = 1) {
  try {
    const { data } = await axios.get(`/users/${username}/repos?page=${page}`);
    return {
      data: data.map(
        (item) =>
          new Repository(
            item.id,
            item.name,
            item.description,
            item.html_url,
            item.stargazers_count,
            item.watchers_count,
            item.language,
            item.forks_count,
            item.size,
            item.open_issues,
            item.created_at,
            item.updated_at
          )
      ),
    };
  } catch (error) {
    return { error: "Not found" };
  }
}
