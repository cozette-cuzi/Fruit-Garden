<script>
export default {
    data() {
        return {
            newOrder: this.dialog,
            order: {
                apple: null,
                peach: null,
                pear: null
            },
            maxOrderRules: [
                v => ((v && v <= 100) || null) || 'Fruit number must be less than 100 in the order',
            ],
        }
    },
    props: {
        dialog: Boolean,
    },

    watch: {
        dialog: function () {
            this.newOrder = this.dialog;
        }
    }
}
</script>

<template>
    <v-row justify="center">
        <v-dialog persistent v-model="newOrder" transition="dialog-bottom-transition" width="600px">
            <v-card>
                <v-card-text class="header">New Order</v-card-text>
                <v-form ref="form" class="px-6" lazy-validation>
                    <v-text-field v-model="order.apple" :rules="maxOrderRules" label="Apple"></v-text-field>
                    <v-text-field v-model="order.peach" :rules="maxOrderRules" label="Peach"></v-text-field>
                    <v-text-field v-model="order.pear" :rules="maxOrderRules" label="Pear"></v-text-field>
                </v-form>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue-darken-1" variant="text" @click="newOrder = false, this.$emit('closeNewOrder')">
                        Cancel
                    </v-btn>
                    <v-btn color="blue-darken-1" variant="text" @click="newOrder = false, this.$emit('closeNewOrder')">
                        Save
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>

<style scoped>

</style>
