<script>
export default {
    data() {
        return {
            fruitCollectionsDialog: false,

        }
    },
    props: {
        dialog: Boolean,
        fruitCollections: Object,
        orderNumber: Number | null
    },

    watch: {
        dialog: function () {
            this.fruitCollectionsDialog = this.dialog;
        }
    }
}
</script>

<template>
    <div class="text-center bg-dark">
        <v-dialog v-model="fruitCollectionsDialog" persistent width="600px">
            <v-card >
                <h3 class="pa-3">Order #{{ orderNumber }} Fruit Collections:</h3>
                <v-table v-if="(this.fruitCollections )">
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
                        <tr v-for="item in fruitCollections" :key="item.id">
                            <td>{{ item.round }}</td>
                            <td>{{ item.fruit }}</td>
                            <td>{{ item.number }}</td>
                        </tr>
                    </tbody>
                </v-table>
                <h4 v-else class="pa-4">No Collections Yet.</h4>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue-darken-1" variant="text"
                        @click="fruitCollectionsDialog = false, this.$emit('closeFruitCollection')">
                        Cancel
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>