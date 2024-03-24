<script setup>
import {useNewsStore} from "@/stores/news.js";
import {convertNewsDate} from "@/support/generalHelper.js";
import SocialComponent from "@/components/Page/SocialComponent.vue";
import NewsletterComponent from "@/components/Page/NewsletterComponent.vue";
import SidebarAdsComponent from "@/components/Page/SidebarAdsComponent.vue";
import TagsComponent from "@/components/Page/TagsComponent.vue";
import SidebarNewsComponent from "@/components/Page/SidebarNewsComponent.vue";

const newsStore = useNewsStore()
</script>

<template>
  <!-- News With Sidebar Start -->
  <div class="container-fluid py-3">
    <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <div class="row">
            <div class="col-12">
              <div class="d-flex align-items-center justify-content-between bg-light py-2 px-4 mb-3">
                <h3 class="m-0">Technology</h3>
                <a class="text-secondary font-weight-medium text-decoration-none" href="">View All</a>
              </div>
            </div>
            <div class="col-lg-6" v-for="(item, index) in newsStore.getBigNews" :key="index">
              <div class="position-relative mb-3">
                <img class="img-fluid w-100"
                     :src="item.avatar ? item.avatar : '/assets/img/news-500x280-1.jpg'"
                     :alt="item.avatar_desc ? item.avatar_desc : item.title"
                     style="object-fit: cover;">
                <div class="overlay position-relative bg-light">
                  <div class="mb-2" style="font-size: 14px;">
                    <a href="/">The Gioi</a>
                    <span class="px-1">/</span>
                    <span>{{ convertNewsDate(item.scraped_time) }}</span>
                  </div>
                  <a class="h4" :href="`/news/${item.news_id}`">{{item.title}}</a>
                  <p class="m-0">{{item.sapo}}</p>
                </div>
              </div>
            </div>
          </div>

          <div class="mb-3">
            <a href=""><img class="img-fluid w-100" src="/assets/img/ads-700x70.jpg" alt=""></a>
          </div>

          <div class="row">
            <div class="col-lg-6" v-for="(item,index) in newsStore.getAllNews" :key="index">
              <div class="d-flex mb-3">
                <img
                    :src="item.avatar ? item.avatar : '/assets/img/news-100x100-1.jpg'"
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
          </div>
        </div>

        <div class="col-lg-4 pt-3 pt-lg-0">
          <SocialComponent />
          <NewsletterComponent />
          <SidebarAdsComponent />
          <SidebarNewsComponent />
          <TagsComponent />
        </div>
      </div>
    </div>
  </div>
  <!-- News With Sidebar End -->
</template>

<style scoped>

</style>