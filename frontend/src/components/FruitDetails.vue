<script>
export default {
    data() {
        return {
            fruitDetailsDialog: false,

        }
    },
    props: {
        dialog: Boolean,
        fruitDetails: Object,
        orderId: Number | null
    },

    watch: {
        dialog: function () {
            this.fruitDetailsDialog = this.dialog;
        }
    }
}
</script>

<template>
    <div class="text-center bg-dark">
        <v-dialog v-model="fruitDetailsDialog" persistent width="360px">
            <v-card>
                <h3 class="px-3 py-3">Order #{{ orderId }} Fruit Details:</h3>
                <v-table>
                    <thead>
                        <tr>
                            <th class="text-left text-subtitle-1 text-center text-primary">
                                Fruit
                            </th>
                            <th class="text-left text-subtitle-1 text-center text-primary">
                                Collected
                            </th>
                            <th class="text-left text-subtitle-1 text-center text-primary">
                                Requested
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in fruitDetails" :key="item.id">
                            <td class="text-center">{{ item.name }}</td>
                            <td class="text-center">{{ item.collected }}</td>
                            <td class="text-center">{{ item.collected + item.rest }}</td>
                        </tr>
                    </tbody>
                </v-table>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue-darken-1" variant="text"
                        @click="fruitDetailsDialog = false, this.$emit('closeFruitDetails')">
                        Close
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>