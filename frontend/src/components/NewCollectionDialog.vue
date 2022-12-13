<script>
export default {
    data() {
        return {
            newCollection: false,
            collection: {
                apple: null,
                peach: null,
                pear: null
            },
            maxCollectionRules: [
                v => ((v && v <= 50) || null) || "Fruit number must be less than 50 in the collection",
            ],
        }
    },
    props: {
        dialog: Boolean,
    },

    watch: {
        dialog: function () {
            this.newCollection = this.dialog;
        }
    }
}
</script>

<template>
    <v-row justify="center">
        <v-dialog v-model="newCollection" persistent transition="dialog-bottom-transition" width="600px">
            <v-card>
                <v-card-text class="header">Add Fruits</v-card-text>
                <v-form ref="form" class="px-6" lazy-validation>
                    <v-text-field v-model="collection.apple" :rules="maxCollectionRules" label="Apple"></v-text-field>
                    <v-text-field v-model="collection.peach" :rules="maxCollectionRules" label="Peach"></v-text-field>
                    <v-text-field v-model="collection.pear" :rules="maxCollectionRules" label="Pear"></v-text-field>
                </v-form>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue-darken-1" variant="text" @click="newCollection = false, this.$emit('closeNewCollection')">
                        Cancel
                    </v-btn>
                    <v-btn color="blue-darken-1" variant="text" @click="newCollection = false, this.$emit('closeNewCollection')">
                        Save
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>