<script setup>
import{ ref, onMounted, computed, watch, defineComponent, createApp } from 'vue'
import { createPinia,defineStore  } from 'pinia';
import App from './App.vue'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)

const clients = ref([])
const name = ref('')

const input_name = ref('')
const input_content = ref('')
const input_sum = ref('')
const input_auto = ref('')
const input_category = ref('name')

const username = ref('')


const addclient = () => {
    if(input_content.value.trim() === '' || input_name.value.trim() === ''  || input_auto.value.trim() === ''){ //Dodawanie klientów 
      return
    }
    clients.value.push({
      name: input_name.value,
      content: input_content.value,
      sum: Number(input_sum.value),
      auto: input_auto.value,
      category: input_category.value,
      done: false
     })

     console.log("addclient");
}
const remove = client => { // usuwanie klientów
  clients.value = clients.value.filter(t => t !== client)
}

const clients_sorted = computed(() => {//Sortowanie klientów po wybranej kategorii
  const category = input_category.value
  if (category === 'name') {
    return clients.value.sort((a, b) => a.name.localeCompare(b.name))
  } 
  else if (category === 'auto')
  {
    return clients.value.sort((a, b) => a.auto.localeCompare(b.auto))
  } 
  else if (category === 'sum')
  {
    return clients.value.sort((a, b) => a.sum - b.sum)
  } 
  
})




watch(clients, (newVaL) => {
  localStorage.setItem('clients', JSON.stringify(newVaL))
  console.log("test");
}, {deep: true}) // zapisywanie danych o kliencie w formacie JSON

watch(input_category, (newValue, oldValue) => {
  if (newValue !== oldValue) {
    clients_sorted.value // odświeżenie listy klientów na podstawie wybranej kategorii
  }
})

onMounted(() => {
  name.value = localStorage.getItem('name') || ''
  clients.value = JSON.parse(localStorage.getItem('clients'))  || []
}) 

//FRAGMENT KODU ZADANIE VUE fragment kodu

//rrA.filter(x => !arrB.includes(x)).concat(arrB.filter(x => !arrA.includes(x)))

// const uniqueInA = rrA.filter(x => !arrB.includes(x));  filtrowanie tablicy postanowiłem rozpisać na parę linijek zeby było to bardziej czytelne 
//const uniqueInB = arrB.filter(x => !arrA.includes(x));
//const result = uniqueInA.concat(uniqueInB);


</script>

<script>
const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    error: null,
    username: '',
    password: '',
  }),
  actions: {
    login({ state }, { username, password }) {
      // Tu możesz wprowadzić logikę logowania
      if (username === '1' && password === '1') {
        console.log("zalogowany")
        state.user = { username };
        state.error = null;
      } else {
        state.user = null;
        state.error = 'Invalid username or password';
        console.log("nie zalogowany")
      }
    },
    logout({ state }) {
      state.user = null;
      state.error = null;
    },
  },
});

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login() {
      const authStore = useAuthStore();
      console.log("logowanko")
      authStore.login({ 
        username: this.username, password: this.password });
      console.log("test login");
    }
  }
}
</script>
<template>
  <div class="login-popup">
    <form @submit.prevent="login">
      <h2>Logowanie</h2>
      <div class="form-group">
        <label for="username">Nazwa użytkownika:</label>
        <input type="text" v-model="username">
      </div>
      <div class="form-group">
        <label for="password">Hasło:</label>
        <input type="password"  v-model="password">
      </div>
      <button type="submit">Zaloguj</button>
    </form>
  </div>
  <main class="app">
    <section class="create-client">
      <h3>Dodaj nowego Użytkownika</h3>

      <form @submit.prevent="addclient">

      <input type="text" placeholder="Nazwa użytkownika" v-model="input_name">
      <input type="text" placeholder="Ostatnio kupione rzeczy " v-model="input_content">
      <input type="number" placeholder="Ile łącznie wydałeś? " v-model="input_sum">
      <input type="text" placeholder="Jaki samochód posiadasz? " v-model="input_auto">

        

        <input type="submit" value="Dodaj klienta">

      
      </form>

    </section>
    <select v-model="input_category">
  <option value="name">Nazwa</option>
  <option value="sum">Suma kosztów</option>
  <option value="auto">Samochód</option>
</select>
      <section class="lista">
        
        <h3>Lista kontaktów:</h3> 
        <div class="list">

          <div v-for="client in clients_sorted" :class="`item ${clients.done && 'done'}`">

            <div class="client-content">
              <p>Imie</p>
              <input type="text" v-model="client.name">
              <p>Lista Ostatnio kupionych rzeczy</p>
              <input type="text" v-model="client.content">
              <p>Suma kosztów</p>
              <input type="number" v-model="client.sum">
              <p>Auto</p>
              <input type="text" v-model="client.auto">
            </div>

            <div class="actions">
              <button @click="remove(client)">Delete</button>
            </div>

          </div>
          
        </div>
      </section>
  </main>
</template>

