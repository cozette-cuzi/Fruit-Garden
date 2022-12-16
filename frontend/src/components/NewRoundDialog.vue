<script>
export default {
  data() {
    return {
      isFormValid: false,
      newRound: false,
      round: null,
      maxRoundRules: [
        v =>
          (v && v <= 50 && v >= 0) ||
          null ||
          "Fruit must be a number and between 0 and 50 in the round"
      ]
    };
  },
  props: {
    fruits: Array
  },
  methods: {
    postRound() {
      this.axios
        .post(this.$api.ACTIONS.ROUNDS, { round_entries: this.round })
        .then(response => {
          this.newRound = false;
          this.emitter.emit(this.$events.SHOW_SNACKBAR, "Data Saved!");
          this.$emit("closeNewRound");
        })
        .catch(() =>
          this.emitter.emit(this.$events.SHOW_SNACKBAR, "Something Wrong!")
        )
        .finally(() => this.initializeRound());
    },

    cancel() {
      this.newRound = false;
      this.$emit("closeNewRound");
      this.initializeRound();
    },

    initializeRound() {
      this.round = this.fruits.map(s => ({ fruit_id: s.id, number: null }));
    }
  },
  mounted() {
    this.initializeRound();
    this.emitter.on(this.$events.NEW_ROUND_DIALOG, () => {
      this.newRound = true;
    });
  },

  watch: {
    dialog: function() {
      this.newRound = this.dialog;
    }
  }
};
</script>

<template>
  <v-row justify="center">
    <v-dialog v-model="newRound" persistent transition="dialog-bottom-transition" width="600px">
      <v-card>
        <v-card-text class="header">Add Fruits</v-card-text>
        <v-form ref="form" class="px-6" v-model="isFormValid" lazy-validation>
          <div v-for="(fruit, key) in fruits" :key="key">
            <v-text-field
              type="number"
              v-model.number="round[key].number"
              :rules="maxRoundRules"
              :label="fruit.name"
            ></v-text-field>
          </div>
        </v-form>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue-darken-1" variant="text" @click="cancel">Cancel</v-btn>
          <v-btn color="blue-darken-1" variant="text" @click="postRound">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>