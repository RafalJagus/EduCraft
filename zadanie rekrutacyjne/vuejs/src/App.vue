<script setup>
import{ ref, onMounted, computed, watch} from 'vue'

const clients = ref([])
const name = ref('')

const input_name = ref('')
const input_content = ref('')
const input_sum = ref('')
const input_auto = ref('')

const input_category = ref(null)

const clients_asc = computed(() => clients.value.sort((a, b) => {
  return b.createdAt - a.createdAt
}))

const addclient = () => {
    if(input_content.value.trim() === ''){
      return
    }
    clients.value.push({
      name: input_name.value,
      content: input_content.value,
      sum: input_sum.value,
      auto: input_auto.value,
      category: input_category.value,
      done: false,
      createdAt: new Date().getTime()
     })

     console.log("addclient");
}

const remove = client => {
  clients.value = clients.value.filter(t => t !== client)
}




watch(clients, (newVaL) => {
  localStorage.setItem('clients', JSON.stringify(newVaL))
  console.log("test");
}, {deep: true})


onMounted(() => {
  name.value = localStorage.getItem('name') || ''
  clients.value = JSON.parse(localStorage.getItem('clients'))  || []
})

</script>

<template>
  <main class="app">


    <section class="create-client">
      <h3>Dodaj nowego Użytkownika</h3>

      <form @submit.prevent="addclient">

      <input type="text" placeholder="Nazwa użytkownika" v-model="input_name">
      <input type="text" placeholder="Ostatnio kupione rzeczy " v-model="input_content">
      <input type="text" placeholder="Ile łącznie wydałeś? " v-model="input_sum">
      <input type="text" placeholder="Jaki samochód posiadasz? " v-model="input_auto">

        

        <input type="submit" value="Dodaj klienta">

      
      </form>

    </section>
      <section class="lista">
        
        <h3>Lista kontaktów:</h3> 
        <div class="list">

          <div v-for="client in clients_asc" :class="`item ${clients.done && 'done'}`">
            

            <div class="client-content">
              <p>Imie</p>
              <input type="text" v-model="client.name">
              <p>Lista</p>
              <input type="text" v-model="client.content">
              <p>Suma kosztów</p>
              <input type="text" v-model="client.sum">
              <p>Auto</p>
              <input type="text" v-model="client.auto">
            </div>

            <div class="actions">
              <button @click="remove(client)">Delete</button>
              <button @click="edit(client)">Edytuj</button>
            </div>

          </div>
          
        </div>
      </section>
  </main>
</template>