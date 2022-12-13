<script>
import NewOrderDialog from "../components/NewOrderDialog.vue";
import NewRoundDialog from "../components/NewRoundDialog.vue";
import FruitRounds from "../components/FruitRounds.vue";
import FruitDetails from "../components/FruitDetails.vue";

export default {
  data() {
    return {
      fruits: null,
      fruitDetailsDialog: false,
      fruitRoundsDialog: false,
      newRound: false,
      newOrder: false,
      selectedOrder: {
        fruitRounds: null,
        number: null,
        fruitDetails: null
      },
      orders: []
    };
  },
  components: {
    NewOrderDialog,
    NewRoundDialog,
    FruitRounds,
    FruitDetails
  },
  mounted() {
    this.axios
      .get(this.$api.ACTIONS.FRUITS)
      .then(response => (this.fruits = response.data));
    this.getOrders();
  },
  methods: {
    getOrders() {
      this.axios
        .get(this.$api.ACTIONS.ORDERS)
        .then(response => (this.orders = response.data));
    }
  }
};
</script>

<template>
  <main>
    <div class="d-flex flex-row mb-6 nav">
      <v-btn class="ma-2" color="warning" @click="newOrder = true">
        <div class="text-white">
          <v-icon icon="mdi-filter-variant-plus pr-3" />New Order
        </div>
      </v-btn>
      <v-btn class="ma-2" color="light" @click="newRound = true">
        <v-icon icon="mdi-cart-plus pr-3" />Add Fuits
      </v-btn>
    </div>

    <v-table fixed-header>
      <thead>
        <tr>
          <th class="text-left text-subtitle-1 text-warning">Action</th>
          <th class="text-left text-subtitle-1 text-warning">Order Number</th>
          <th class="text-left text-subtitle-1 text-warning">Order Date</th>
          <th class="text-left text-subtitle-1 text-warning">Collected/All</th>
          <th class="text-left text-subtitle-1 text-warning">Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in orders" :key="item.name">
          <td>
            <v-btn flat icon @click="(selectedOrder = item, fruitDetailsDialog = true)">
              <i class="material-icons small">keyboard_arrow_right</i>
            </v-btn>
          </td>
          <td
            class="pointer"
            @click="(selectedOrder = item, fruitRoundsDialog = true)"
          >{{ item.id }}</td>
          <td>{{ item.created }}</td>
          <td>{{ item.collected }} / {{ item.rest + item.collected }}</td>
          <td>{{ item.status }}</td>
        </tr>
      </tbody>
    </v-table>

    <FruitDetails
      :dialog="fruitDetailsDialog"
      :orderNumber="selectedOrder.number"
      :fruit-details="selectedOrder.fruitDetails"
      v-on:closeFruitDetails="fruitDetailsDialog = false"
    />

    <FruitRound
      :dialog="fruitRoundDialog"
      :orderNumber="selectedOrder.number"
      :fruit-rounds="selectedOrder.fruitRounds"
      v-on:closeFruitRound="fruitRoundsDialog = false"
    />

    <NewOrderDialog :dialog="newOrder" :fruits="fruits" v-on:closeNewOrder="newOrder = false" />
    <NewRoundDialog :dialog="newRound" :fruits="fruits" v-on:closeNewRound="newRound = false" />
  </main>
</template>


<style scoped>
.nav {
  min-width: 1100px;
  margin: 0 auto;
}

.pointer {
  cursor: pointer;
}

.small {
  font-size: 16px;
}
</style>