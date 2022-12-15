
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
    <v-card>
      <v-card-text class="white--text">
        {{message}}
        <v-progress-linear model-value="100" rounded height="7" striped color="primary" class="my-2"></v-progress-linear>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>


<style scoped>
</style>