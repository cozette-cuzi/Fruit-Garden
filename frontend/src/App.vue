<script>
import LoadingComponent from './components/LoadingComponent.vue';

export default {
    data() {
        return {
            message: true,
            snackbar: false,
            loading: false
        };
    },
    mounted() {
        this.emitter.on(this.$events.SHOW_SNACKBAR, message => {
            this.message = message;
            this.snackbar = true;
        });
        this.emitter.on(this.$events.SHOW_LOADING, () => {
            this.loading = true;
        });
        this.emitter.on(this.$events.HIDE_LOADING, () => {
            this.loading = false;
        });
    },
    components: { LoadingComponent }
};
</script>

<template>
  <v-app>
    <h1>Fruit Garden</h1>
    <v-divider></v-divider>
    <LoadingComponent :value="loading" />

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
