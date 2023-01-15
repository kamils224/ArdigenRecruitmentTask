import axios from "@/api/axiosInstance";


class Owner {
    constructor(id, login, avatar_url) {
        this.id = id;
        this.login = login;
        this.avatar_url = avatar_url
    }

}

class Repository {
    constructor(id, name, description, avatarUrl, owner) {
        this.id=id;
        this.name = name;
        this.description = description;
        this.avatarUrl = avatarUrl;
        this.owner = owner;
    }
}

export async function getUserRepositories(username, page=1, perPage=10) {
    try {
        const { data } = await axios.get(`/users/${username}/repos?page=${page}&per_page=${perPage}`);
        return { data: data.map((item) => {
            return new Repository(
            item.id,
            item.name,
            item.description,
            item.avatar_url,
            new Owner(item.owner.id, item.owner.login, item.owner.avatar_url)
            )
        })
        }
    }
    catch (error) {
        return {error: "Not found"};
    }
}
