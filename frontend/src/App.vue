<script>
export default {
  data() {
    return {
      message: true,
      snackbar: false
    };
  },
  mounted() {
    this.emitter.on("SHOW_SNACKBAR", message => {
      this.message = message;
      this.snackbar = true;
    });
  }
};
</script>

<template>
  <v-app>
    <h1>Fruit Garden</h1>
    <v-divider></v-divider>
    <v-snackbar v-model="snackbar" timeout="2500">
      {{ message }}
      <template v-slot:actions>
        <v-btn color="red" variant="text" @click="snackbar = false">Close</v-btn>
      </template>
    </v-snackbar>
    <router-view :key="$route.fullPath"></router-view>
  </v-app>

  <!-- <RouterView /> -->
</template>

<style scoped>
</style>
