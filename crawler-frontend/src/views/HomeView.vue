<script setup>

import TopbarComponent from "@/components/Layout/TopbarComponent.vue";
import NavbarComponent from "@/components/Layout/NavbarComponent.vue";
import FooterComponent from "@/components/Layout/FooterComponent.vue";
import BreadcrumbComponent from "@/components/Layout/BreadcrumbComponent.vue";
import ListNewsComponent from "@/components/Page/ListNewsComponent.vue";
</script>

<template>
  <TopbarComponent />
  <NavbarComponent />
  <BreadcrumbComponent />

  <!-- ListNew Component -->
  <ListNewsComponent />

  <FooterComponent />
</template>
