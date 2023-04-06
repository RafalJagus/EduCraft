<script setup>

</script>

<template>
  <div>
    <h1>Lista klientów:</h1>
    <ul>
      <li v-for="customer in customers" :key="customer.id">
        <router-link :to="{ name: 'customer', params: { id: customer.id } }">
          {{ customer.name }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      customers: []
    };
  },
  mounted() {
    // Pobierz dane klientów z API
    this.$http.get('/api/customers').then(response => {
      this.customers = response.data;
    });
  }
};
</script>