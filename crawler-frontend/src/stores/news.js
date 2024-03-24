import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { backend_api } from "@/support/httpCommon.js";
import { saveNewsToStorage } from "@/support/storageHelper.js";
import { getRandomSubArray } from "@/support/generalHelper.js";

export const useNewsStore = defineStore('news', () => {
    const newsList = ref([])
    const singleNews = ref({})
    const getAllNews = computed(() => {
        return newsList.value
    })
    const getBigNews = computed(() => {
        return getRandomSubArray(newsList.value, 4)
    })
    const getTrendingNews = computed(() => {
        return getRandomSubArray(newsList.value, 5)
    })
    const getNormalNews = computed(() => {
        return getRandomSubArray(newsList.value, 10)
    })
    async function loadNews() {
        await backend_api.get("/news/")
            .then((resp) => {
                newsList.value = resp.data
                saveNewsToStorage(newsList.value)
            })
    }
    async function retrieveNews(news_id) {
        await backend_api.get(`/news/${news_id}`)
            .then((resp) => {
                singleNews.value = resp.data
            })
    }

    return { newsList, singleNews,
        getAllNews, getBigNews, getTrendingNews, getNormalNews,
        loadNews, retrieveNews }
})
