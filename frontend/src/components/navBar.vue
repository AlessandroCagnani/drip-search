<template>
  <div class="navbar grid">
    <router-link to="/" class="navbar-logo" >DRIPSTATION</router-link>
    <div class="filter-box"></div>
    <div class="searchbar">
      <searchBar />
    </div>
  </div>
</template>

<script>
import searchBar from "@/components/searchBar.vue";


export default {
  name: "navBar",
  components: {
    searchBar,
  },
  methods: {
    hide: function (event) {
      console.log("dropdown:  ", event);
    },
  },
};
</script>

<style scoped>
.navbar {
  width: 100%;
  height: 100%;
  background-color: #f5f5f5;
  margin-bottom: 2rem;
}

.navbar-logo {
  padding: 2%;
  text-align: left;
  font-size: 2rem;
  font-weight: bold;
}

.searchbar {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: end;
}

.grid {
  display: grid;
  grid-template-columns: 3fr 1fr 2fr;
  grid-template-rows: 0.2fr;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
}

</style>