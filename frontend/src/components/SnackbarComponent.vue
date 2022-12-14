
<script>
export default {
  data() {
    return {
      snackbar: false,
      timeout: 1000
    };
  },
  props: {
    value: {
      type: Boolean,
      default: false
    },
    type: {
      type: String,
      default: "success"
    },
    message: {
      type: String,
      default: "Data Saved!"
    }
  },
  watch: {
    value: function() {
      this.snackbar = this.value;
    }
  }
};
</script>

<template>
  <v-snackbar v-model="snackbar" :timeout="timeout" :color="snackbarColor" top>{{ message }}</v-snackbar>
</template>


<style scoped>
</style>