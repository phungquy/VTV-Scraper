<script setup>
import {onMounted, onUnmounted, ref} from "vue";

let intervalId
const currentTime = ref((new Date()).toISOString().slice(0, 19).replace(/-g/, "/").replace("T", " "))
const site_title = import.meta.env.VITE_PROJECT_TITLE
onMounted(() =>{
  intervalId = setInterval(() => {
    // update time & date
    currentTime.value = (new Date()).toISOString().slice(0, 19).replace(/-g/, "/").replace("T", " ")
  }, 1000)
})
onUnmounted(() => {
  clearInterval(intervalId)
})
</script>

<template>
  <!-- Topbar Start -->
  <div class="container-fluid">
    <div class="row align-items-center bg-light px-lg-5">
      <div class="col-12 col-md-8">
        <div class="d-flex justify-content-between">
          <div class="bg-primary text-white text-center py-2" style="width: 100px;">Trending</div>
        </div>
      </div>
      <div class="col-md-4 text-right d-none d-md-block">
        {{ currentTime }}
      </div>
    </div>
    <div class="row align-items-center py-2 px-lg-5">
      <div class="col-lg-4">
        <a href="/" class="navbar-brand d-none d-lg-block">
          <h1 class="m-0 display-5 text-uppercase"><span class="text-primary">{{ site_title }}</span></h1>
        </a>
      </div>
      <div class="col-lg-8 text-center text-lg-right">
        <img class="img-fluid" src="/assets/img/ads-700x70.jpg" alt="">
      </div>
    </div>
  </div>
  <!-- Topbar End -->
</template>

<style scoped>

</style>