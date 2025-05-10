<template>
  <div id="app">
    <nav>
      <router-link to="/login">Login</router-link> |
      <router-link to="/register">Cadastro</router-link> |
      <router-link to="/Home">Menu</router-link>
    </nav>
    <router-view />
  </div>
</template>

<style>
nav {
  padding: 1rem;
  background: #f3f3f3;
}
nav a {
  margin-right: 10px;
  text-decoration: none;
}
</style>  