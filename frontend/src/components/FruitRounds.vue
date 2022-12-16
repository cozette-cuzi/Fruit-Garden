<script>
export default {
    data() {
        return {
            fruitRoundsDialog: false,
        }
    },
    props: {
        dialog: Boolean,
        roundDetails: Object,
        orderId: Number | null
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
        <v-dialog v-model="fruitRoundsDialog" persistent width="400px">
            <v-card >
                <h3 class="pa-3">Order #{{ orderId }} Rounds:</h3>
                <v-table v-if="this.roundDetails && this.roundDetails.length">
                    <thead>
                        <tr>
                            <th class="text-left text-subtitle-1 text-center text-primary">
                                Round
                            </th>
                            <th class="text-left text-subtitle-1 text-center text-primary">
                                Fruit
                            </th>
                            <th class="text-left text-subtitle-1 text-center text-primary">
                                Number
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in roundDetails" :key="item.id">
                            <td class="text-center">{{ item.round_id }}</td>
                            <td class="text-center">{{ item.fruit }}</td>
                            <td class="text-center">{{ item.number }}</td>
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