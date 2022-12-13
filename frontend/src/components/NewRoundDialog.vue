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
      this.newRound = false;
      this.$emit("closeNewRound");
      this.round.map(elem => {
        elem.fruit_id = elem.id;
        delete elem["id"];
        delete elem["name"];
      });
      console.log(this.round)
      this.axios
        .post(this.$api.ACTIONS.ROUNDS, { round_entries: this.round })
        .then(response => {
          console.log(response.data);
        });
    }
  },

  watch: {
    dialog: function() {
      this.newRound = this.dialog;
    },
    fruits: function() {
      this.round = this.fruits;
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
          <v-btn
            color="blue-darken-1"
            variant="text"
            @click="postRound"
          >Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>