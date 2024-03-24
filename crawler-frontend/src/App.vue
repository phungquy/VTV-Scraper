<script setup>
import { RouterLink, RouterView } from 'vue-router'
import {onMounted} from "vue";
import {useNewsStore} from "@/stores/news.js";

const newsStore = useNewsStore()
onMounted(() => {
  newsStore.loadNews()
  console.log(import.meta.env.MODE)
  console.log(import.meta.env.VITE_CRAWLER_BACKEND_URL)
})
</script>

<template>
  <RouterView />
</template>

<style scoped>

</style>
