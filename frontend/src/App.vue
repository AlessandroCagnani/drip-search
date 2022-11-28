<template>
  <router-view />
</template>

<script>

export default {
  components: {

  },
  watch: {
    $route: {
      immediate: true,
      handler(to) {
        // Sets the page title based on the  meta attribute 'title' inside the router.
        document.title = to.meta.title || 'Drip Search';
        // this.$store.dispatch('')
        // this.$store.dispatch('')
      }
    },
  },
  beforeMount() {
    // this.$store.dispatch('')
    // this.$store.dispatch('')
  }
};
</script>

<!-- eslint-disable vue-scoped-css/enforce-style-type -->
<style>

html, body, #app {
  margin: 0;
  height: 100%;
  width: 100%;
}

</style>
<!--eslint-enable-->