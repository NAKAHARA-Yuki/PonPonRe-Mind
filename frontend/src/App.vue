<template>
  <div id="app">
    <h1>Hello from Vue.js!</h1>
    <button @click="fetchUsers">Get Users</button>
    <ul>
      <li v-for="user in users" :key="user.id">{{ user.name }}</li>
    </ul>
    <input v-model="newUser" placeholder="Enter user name">
    <button @click="addUser">Add User</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [],
      newUser: ''
    }
  },
  methods: {
    fetchUsers() {
      this.$http.get('/users').then(response => {
        this.users = response.data;
      })
    },
    addUser() {
      this.$http.post('/users', { name: this.newUser }).then(() => {
        this.fetchUsers();
        this.newUser = '';
      })
    }
  }
}
</script>
