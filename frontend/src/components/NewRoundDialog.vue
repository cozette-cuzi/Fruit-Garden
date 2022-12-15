<script>
export default {
  data() {
    return {
      newRound: false,
      round: null,
      maxRoundRules: [
        v =>
          (v && v <= 50) ||
          null ||
          "Fruit number must be less than 50 in the Round"
      ]
    };
  },
  props: {
    dialog: Boolean,
    fruits: Array
  },
  methods: {
    postRound() {
      this.axios
        .post(this.$api.ACTIONS.ROUNDS, { round_entries: this.round })
        .then(response => {
          console.log(response.data);
          this.newRound = false;
          this.emitter.emit(this.$events.SHOW_SNACKBAR, "Data Saved!");
          this.$emit("closeNewRound");
        })
        .catch(() =>
          this.emitter.emit(this.$events.SHOW_SNACKBAR, "Something Wrong!")
        )
        .finally(
          () =>
            (this.round = this.fruits.map(s => ({
              fruit_id: s.id,
              number: null
            })))
        );
    }
  },
  mounted() {
    this.round = this.fruits.map(s => ({ fruit_id: s.id, number: null }));
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
        <v-form ref="form" class="px-6" lazy-validation>
          <div v-for="(fruit, key) in fruits" :key="key">
            <v-text-field
              v-model.number="round[key].number"
              :rules="maxRoundRules"
              :label="fruit.name"
            ></v-text-field>
          </div>
        </v-form>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue-darken-1"
            variant="text"
            @click="newRound = false, this.$emit('closeNewRound')"
          >Cancel</v-btn>
          <v-btn color="blue-darken-1" variant="text" @click="postRound">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>