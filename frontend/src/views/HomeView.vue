<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <searchBar/>
  </div>
</template>

<script>
// @ is an alias to /src
import searchBar from '@/components/searchBar.vue'

export default {
  name: 'HomeView',
  components: {
    searchBar
  }
}
</script>