<template>
  <div>
    <h1>{{ customer.name }}</h1>
    <p>Pracownik: {{ employee.name }}</p>
    <p>Ostatnie zamówienia:</p>
    <ul>
      <li v-for="order in orders" :key="order.id">{{ order.product }} - {{ order.price }}</li>
    </ul>
    <p>Łączna kwota wydana przez klienta: {{ totalSpent }}</p>
    <p>Samochód: {{ car.make }} {{ car.model }} ({{ car.year }})</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      customer: {},
      employee: {},
      orders: [],
      car: {}
    };
  },
  mounted() {
    const customerId = this.$route.params.id;

    // Pobierz dane klienta z API
    this.$http.get(`/api/customers/${customerId}`).then(response => {
      this.customer = response.data;
      this.employee = response.data.employee;
      this.orders = response.data.orders;
      this.car = response.data.car;
    });
  },
  computed: {
    totalSpent() {
      return this.orders.reduce((sum, order) => sum + order.price, 0);
    }
  }
};
</script>