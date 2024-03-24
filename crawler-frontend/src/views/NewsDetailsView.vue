<script setup>
import FooterComponent from "@/components/Layout/FooterComponent.vue";
import NavbarComponent from "@/components/Layout/NavbarComponent.vue";
import TopbarComponent from "@/components/Layout/TopbarComponent.vue";
import BreadcrumbComponent from "@/components/Layout/BreadcrumbComponent.vue";
import SocialComponent from "@/components/Page/SocialComponent.vue";
import NewsletterComponent from "@/components/Page/NewsletterComponent.vue";
import SidebarAdsComponent from "@/components/Page/SidebarAdsComponent.vue";
import SidebarNewsComponent from "@/components/Page/SidebarNewsComponent.vue";
import TagsComponent from "@/components/Page/TagsComponent.vue";

import {onBeforeMount} from "vue";

import {useNewsStore} from "@/stores/news.js";
import {convertNewsDate} from "@/support/generalHelper.js";
import {useRoute} from "vue-router";

const newsStore = useNewsStore()
const route = useRoute()

onBeforeMount(() => {
  newsStore.retrieveNews(route.params.news_id)
})
</script>

<template>
  <TopbarComponent />
  <NavbarComponent />
  <BreadcrumbComponent />

  <!-- News With Sidebar Start -->
  <div class="container-fluid py-3">
    <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <!-- News Detail Start -->
          <div class="position-relative mb-3">
            <img class="img-fluid w-100"
                 :src="newsStore.singleNews.avatar ? newsStore.singleNews.avatar : '/assets/img/news-700x435-2.jpg'"
                 :alt="newsStore.singleNews.avatar_desc ? newsStore.singleNews.avatar_desc : newsStore.singleNews.title"
                 style="object-fit: cover;">
            <div class="overlay position-relative bg-light">
              <div class="mb-3">
                <a href="/">The gioi</a>
                <span class="px-1">/</span>
                <span>{{ convertNewsDate(newsStore.singleNews.scraped_time) }}</span>
              </div>
              <h5>{{ newsStore.singleNews.sapo }}</h5>
              <div v-html="newsStore.singleNews.content">
              </div>
            </div>
          </div>
          <!-- News Detail End -->
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

  <FooterComponent />
</template>

<style scoped>

</style>