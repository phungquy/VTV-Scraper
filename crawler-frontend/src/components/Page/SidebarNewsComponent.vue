<script setup>
import {useNewsStore} from "@/stores/news.js";
import {convertNewsDate} from "@/support/generalHelper.js";

const newsStore = useNewsStore()
</script>

<template>
  <!-- Popular News Start -->
  <div class="pb-3">
    <div class="bg-light py-2 px-4 mb-3">
      <h3 class="m-0">Trending</h3>
    </div>
    <div class="d-flex mb-3" v-for="(item,index) in newsStore.getTrendingNews" :key="index">
      <img :src="item.avatar ? item.avatar : '/assets/img/news-100x100-1.jpg'"
           :alt="item.avatar_desc ? item.avatar_desc : item.title"
           style="width: 100px; height: 100px; object-fit: cover;">
      <div class="w-100 d-flex flex-column justify-content-center bg-light px-3" style="height: 100px;">
        <div class="mb-1" style="font-size: 13px;">
          <a href="/">The Gioi</a>
          <span class="px-1">/</span>
          <span>{{ convertNewsDate(item.scraped_time) }}</span>
        </div>
        <a class="h6 m-0" :href="`/news/${item.news_id}`">{{ item.title }}</a>
      </div>
    </div>
  </div>
  <!-- Popular News End -->
</template>

<style scoped>

</style>