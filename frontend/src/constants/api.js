const hostName = window.location.hostname;
let MAIN_HOST = `http://${hostName}:8000`;

export default {
  MAIN_URL: MAIN_HOST,

  ACTIONS: {
    FRUITS: "fruits",
    ORDERS: "orders",
    ROUNDS: "rounds"
  },
};
