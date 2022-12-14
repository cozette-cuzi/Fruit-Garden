<script>
import NewOrderDialog from "../components/NewOrderDialog.vue";
import NewRoundDialog from "../components/NewRoundDialog.vue";
import FruitRounds from "../components/FruitRounds.vue";
import FruitDetails from "../components/FruitDetails.vue";
import LoadingComponent from "../components/LoadingComponent.vue";

export default {
  data() {
    return {
      loading: true,
      fruits: null,
      fruitDetailsDialog: false,
      fruitRoundsDialog: false,
      newRound: false,
      newOrder: false,
      selectedOrder: {
        fruitRounds: null,
        id: null,
        fruitDetails: null
      },
      orders: []
    };
  },
  components: {
    NewOrderDialog,
    NewRoundDialog,
    FruitRounds,
    FruitDetails,
    LoadingComponent,
  },
  mounted() {
    this.axios
      .get(this.$api.ACTIONS.FRUITS)
      .then(
        response => ((this.fruits = response.data), (this.loading = false))
      );
    this.getOrders();
  },
  methods: {
    reload() {
      this.newOrder = false;
      this.newRound = false;
      console.log("reloaded");
      this.getOrders();
    },
    getOrders() {
      this.loading = true;
      this.axios
        .get(this.$api.ACTIONS.ORDERS)
        .then(
          response => ((this.orders = response.data), (this.loading = false))
        );
    },
    getFruitDetails(item) {
      this.selectedOrder = item;
      this.fruitDetailsDialog = true;
      this.axios
        .get(this.$api.ACTIONS.ORDERS + "/" + this.selectedOrder.id)
        .then(response => {
          this.selectedOrder.fruitDetails = response.data.fruit_details;
          console.log(this.selectedOrder);
        })
        .catch(err => console.log(err.error));
    }
  }
};
</script>

<template>
  <main>
    <div class="d-flex flex-row mb-6 nav">
      <v-btn class="ma-2" color="primary" @click="newOrder = true">
        <div class="text-white font-weight-bold">
          <v-icon icon="mdi-filter-variant-plus pr-3" />New Order
        </div>
      </v-btn>
      <v-btn class="ma-2" color="light" @click="newRound = true">
        <div class="font-weight-bold">
          <v-icon icon="mdi-cart-plus pr-3" />Add Fuits
        </div>
      </v-btn>
    </div>

    <v-table fixed-header>
      <thead>
        <tr>
          <th class="text-left text-subtitle-1 text-button text-center text-primary">Action</th>
          <th class="text-left text-subtitle-1 text-button text-center text-primary">Order Number</th>
          <th class="text-left text-subtitle-1 text-button text-center text-primary">Order Date</th>
          <th class="text-left text-subtitle-1 text-button text-center text-primary">Collected/All</th>
          <th class="text-left text-subtitle-1 text-button text-center text-primary">Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in orders" :key="item.name">
          <td class="text-center">
            <v-btn flat icon @click="getFruitDetails(item)">
              <i class="material-icons small">keyboard_arrow_right</i>
            </v-btn>
          </td>
          <td
            class="pointer text-center"
            @click="(selectedOrder = item, fruitRoundsDialog = true)"
          >{{ item.id }}</td>
          <td class="text-center">{{ item.created }}</td>
          <td class="text-center">{{ item.collected }} / {{ item.rest + item.collected }}</td>
          <td class="text-center">
            <p
              class="font-weight-bold"
              :class="{
                'text-grey': item.status == 'new',
                'text-warning': item.status == 'collecting',
                'text-success': item.status == 'done'
              }"
            >{{ item.status }}</p>
          </td>
        </tr>
      </tbody>
    </v-table>
    <LoadingComponent :value="loading" />
    <FruitDetails
      :dialog="fruitDetailsDialog"
      :orderId="selectedOrder.id"
      :fruit-details="selectedOrder.fruitDetails"
      v-on:closeFruitDetails="fruitDetailsDialog = false"
    />

    <FruitRound
      :dialog="fruitRoundDialog"
      :orderId="selectedOrder.id"
      :fruit-rounds="selectedOrder.fruitRounds"
      v-on:closeFruitRound="fruitRoundsDialog = false"
    />

    <NewOrderDialog v-if="fruits" :dialog="newOrder" :fruits="fruits" v-on:closeNewOrder="reload" />
    <NewRoundDialog v-if="fruits" :dialog="newRound" :fruits="fruits" v-on:closeNewRound="reload" />
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