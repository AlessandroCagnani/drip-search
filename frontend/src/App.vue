<template>
  <nav>
    <navBar class="sticky"/>
  </nav>
  <router-view/>
</template>

<script>
import navBar from '@/components/navBar.vue'

export default {
  name: 'App',
  components: {
    navBar
  }
}
</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&display=swap');

* {
    font-family: 'Oswald', sans-serif;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body {
  margin: 0;
  padding: 0;
}

nav a {
  font-weight: bold;
  color: Black;
    text-decoration: none;
}

a:hover {
  color: darkslateblue;
}

/*nav a.router-link-exact-active {*/
/*  color: #42b983;*/
/*}*/
</style>
