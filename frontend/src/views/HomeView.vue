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
        fruit_details: null,
        id: null,
        round_details: null
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
      .then(response => {
        this.fruits = response.data;
        this.emitter.emit(this.$events.SHOW_LOADING);
      })
      .finally(() => {
        this.emitter.emit(this.$events.HIDE_LOADING);
      });
    this.getOrders();
  },
  methods: {
    reload() {
      this.newOrder = false;
      this.newRound = false;
      this.getOrders();
    },
    getOrders() {
      this.emitter.emit(this.$events.SHOW_LOADING);
      this.axios.get(this.$api.ACTIONS.ORDERS).then(response => {
        this.orders = response.data;
        this.emitter.emit(this.$events.HIDE_LOADING);
      });
    },
    getItemDetails(item) {
      this.selectedOrder = item;
      this.emitter.emit(this.$events.SHOW_LOADING);
      this.axios
        .get(this.$api.ACTIONS.ORDERS + "/" + this.selectedOrder.id)
        .then(response => {
          this.selectedOrder = response.data;
        })
        .catch(err => console.log(err.error))
        .finally(() => {
          this.emitter.emit(this.$events.HIDE_LOADING);
        });
    }
  }
};
</script>

<template>
  <main>
    <v-toolbar>
      <v-row class="m-6 nav">
      <v-col>
        <h1>Fruit Garden</h1>
      </v-col>
      <v-col class="text-right">
        <v-btn class="ma-2" color="primary" @click="newOrder = true">
          <div class="text-white font-weight-bold">
            <v-icon icon="mdi-filter-variant-plus pr-3" />New Order
          </div>
        </v-btn>
        <v-btn class="ma-2" color="light" @click="newRound = true">
          <div class="font-weight-bold">
            <v-icon icon="mdi-cart-plus pr-3" />Add Fruits
          </div>
        </v-btn>
      </v-col>

    </v-row>
    </v-toolbar>
    
    <v-divider class="mb-3"></v-divider>

    <!-- <div class="mb-6 nav">
      <div>
        <h1>Fruit Garden</h1>
        <v-divider></v-divider>
      </div>

      <v-btn class="ma-2" color="primary" @click="newOrder = true">
        <div class="text-white font-weight-bold">
          <v-icon icon="mdi-filter-variant-plus pr-3" />New Order
        </div>
      </v-btn>
      <v-btn class="ma-2" color="light" @click="newRound = true">
        <div class="font-weight-bold">
          <v-icon icon="mdi-cart-plus pr-3" />Add Fruits
        </div>
      </v-btn>
    </div> -->

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
            <v-btn flat icon @click="getItemDetails(item), fruitDetailsDialog = true">
              <v-tooltip location="bottom" text="Show Fruit Details">
                <template v-slot:activator="{ props }">
                  <i class="material-icons small" v-bind="props">keyboard_arrow_down</i>
                </template>
              </v-tooltip>
            </v-btn>
          </td>
          <td class="pointer text-center" @click="(getItemDetails(item), fruitRoundsDialog = true)">
            <v-tooltip location="bottom" text="Show Order Rounds">
              <template v-slot:activator="{ props }">
                <span v-bind="props">{{ item.id }}</span>
              </template>
            </v-tooltip>
          </td>
          <td class="text-center">{{ item.created }}</td>
          <td class="text-center">{{ item.collected }} / {{ item.rest + item.collected }}</td>
          <td class="text-center">
            <p
              class="font-weight-light text-button"
              :class="{
                'text-info': item.status == 'new',
                'text-warning': item.status == 'collecting',
                'text-green': item.status == 'done'
              }"
            >{{ item.status }}</p>
          </td>
        </tr>
      </tbody>
    </v-table>
    <FruitDetails
      :dialog="fruitDetailsDialog"
      :orderId="selectedOrder.id"
      :fruit-details="selectedOrder.fruit_details"
      v-on:closeFruitDetails="fruitDetailsDialog = false"
    />

    <FruitRounds
      :dialog="fruitRoundsDialog"
      :orderId="selectedOrder.id"
      :round-details="selectedOrder.round_details"
      v-on:closeFruitRound="fruitRoundsDialog = false"
    />

    <NewOrderDialog v-if="fruits" :dialog="newOrder" :fruits="fruits" v-on:closeNewOrder="reload" />
    <NewRoundDialog v-if="fruits" :dialog="newRound" :fruits="fruits" v-on:closeNewRound="reload" />
  </main>
</template>


<style scoped>
.nav {
  min-width: 900px;
  margin: 0 auto;
}

.container {
  justify-self: center;
  justify-content: center;
  display: flex;
}

.pointer {
  cursor: pointer;
}

.small {
  font-size: 16px;
}
</style>