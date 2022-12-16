<script>
import image from "../assets/logo.png";

export default {
  data() {
    return {
      image: image,
      newRound: false,
      newOrder: false
    };
  }
};
</script>
<template>
  <v-row class="m-6 nav">
    <v-col cols="1">
      <img class="logo" :src="image" />
    </v-col>
    <v-col class="pl-0 pt-4">
      <h1 class="pa-0 title text-green">Fruit Garden</h1>
    </v-col>
    <v-col class="text-right">
      <v-btn class="ma-2" color="primary" @click="this.emitter.emit(this.$events.NEW_ORDER_DIALOG)">
        <div class="text-white font-weight-bold">
          <v-icon icon="mdi-filter-variant-plus pr-3" />New Order
        </div>
      </v-btn>
      <v-btn class="ma-2" color="green" @click="this.emitter.emit(this.$events.NEW_ROUND_DIALOG)">
        <div class="font-weight-bold">
          <v-icon icon="mdi-cart-plus pr-3" />Add Fruits
        </div>
      </v-btn>
    </v-col>
  </v-row>
</template>

<style>
.logo {
  width: 58%;
  object-fit: cover;
  overflow: hidden;
  float: right;
  margin-top: 10px;
}
.title {
  font-family: "Luckiest Guy", Helvetica, Arial;
}
</style>
