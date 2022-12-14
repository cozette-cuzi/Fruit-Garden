
<script>
export default {
  data() {
    return {
      dialog: false
    };
  },
  props: {
    value: {
      type: Boolean,
      default: false
    },
    message: {
      type: String,
      default: "Loading Data"
    }
  },
  watch: {
    value: function() {
      this.dialog = this.value;
    }
  }
};
</script>

<template>
  <v-dialog v-model="dialog" hide-overlay persistent width="300">
    <v-card color="primary">
      <v-card-text class="white--text">
        {{message}}
        <v-progress-linear indeterminate color="white" class="my-2"></v-progress-linear>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>


<style scoped>
</style>