<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <v-app>
      <h1>Fruit Garden</h1>
      <v-divider></v-divider>
      <router-view :key="$route.fullPath"></router-view>
  </v-app>

  <!-- <RouterView /> -->
</template>

<style scoped>

</style>
