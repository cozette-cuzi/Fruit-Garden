<script>
export default {
    data() {
        return {
            fruitRoundsDialog: false,

        }
    },
    props: {
        dialog: Boolean,
        fruitRounds: Object,
        orderNumber: Number | null
    },

    watch: {
        dialog: function () {
            this.fruitRoundsDialog = this.dialog;
        }
    }
}
</script>

<template>
    <div class="text-center bg-dark">
        <v-dialog v-model="fruitRoundsDialog" persistent width="600px">
            <v-card >
                <h3 class="pa-3">Order #{{ orderNumber }} Fruit Rounds:</h3>
                <v-table v-if="(this.fruitRounds )">
                    <thead>
                        <tr>
                            <th class="text-left text-subtitle-1 text-warning">
                                Round
                            </th>
                            <th class="text-left text-subtitle-1 text-warning">
                                Fruit
                            </th>
                            <th class="text-left text-subtitle-1 text-warning">
                                Number
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in fruitRounds" :key="item.id">
                            <td>{{ item.round }}</td>
                            <td>{{ item.fruit }}</td>
                            <td>{{ item.number }}</td>
                        </tr>
                    </tbody>
                </v-table>
                <h4 v-else class="pa-4">No Rounds Yet.</h4>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue-darken-1" variant="text"
                        @click="fruitRoundsDialog = false, this.$emit('closeFruitRound')">
                        Cancel
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>