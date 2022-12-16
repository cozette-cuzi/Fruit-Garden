<script>
export default {
  data() {
    return {
      newOrder: false,
      order: null,
      maxOrderRules: [
        v =>
          (v && v <= 100 && v > 0) ||
          null ||
          "Fruit must be a number and less than 100 in the order"
      ]
    };
  },
  props: {
    fruits: Array
  },
  methods: {
    postOrder() {
      this.axios
        .post(this.$api.ACTIONS.ORDERS, { order_entries: this.order })
        .then(response => {
          this.newOrder = false;
          this.emitter.emit(this.$events.SHOW_SNACKBAR, "Data Saved!");
          this.$emit("closeNewOrder");
        })
        .catch(err => {
          this.emitter.emit(this.$events.SHOW_SNACKBAR, "Something Wrong!");
        })
        .finally(() => {
          this.initializeOrder();
        });
    },
    cancel() {
      this.newOrder = false;
      this.$emit("closeNewOrder");
      this.initializeOrder();
    },
    initializeOrder() {
      this.order = this.fruits.map(s => ({ fruit_id: s.id, number: null }));
    }
  },
  mounted() {
    this.initializeOrder();
    this.emitter.on(this.$events.NEW_ORDER_DIALOG, () => {
      this.newOrder = true;
    });
  }
};
</script>

<template>
  <v-row justify="center">
    <v-dialog persistent v-model="newOrder" transition="dialog-bottom-transition" width="600px">
      <v-card>
        <v-card-text class="header">New Order</v-card-text>
        <v-form ref="form" class="px-6" lazy-validation>
          <div v-for="(fruit, key) in fruits" :key="key">
            <v-text-field
              v-model.number="order[key].number"
              :rules="maxOrderRules"
              :label="fruit.name"
            ></v-text-field>
          </div>
        </v-form>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue-darken-1" variant="text" @click="cancel">Cancel</v-btn>
          <v-btn color="blue-darken-1" variant="text" @click="postOrder">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<style scoped>
</style>
