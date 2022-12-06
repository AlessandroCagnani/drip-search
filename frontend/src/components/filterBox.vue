<template>
  <div class="container">
    <h2>Filter</h2>

    <vue-collapsible-panel-group>
      <vue-collapsible-panel :expanded="false">
        <template #title> Brand </template>
        <template #content>
          <div class="brand-box">
            <div class="brand-check" v-for="brand in brands">
              <label :for="brand">{{ brand }}</label>
              <input
                type="checkbox"
                :id="brand"
                :value="brand"
                v-model="selectedBrands"
              />
            </div>
          </div>
        </template>
      </vue-collapsible-panel>
      <vue-collapsible-panel :expanded="false">
        <template #title> Category </template>
        <template #content> Panel B Content </template>
      </vue-collapsible-panel>
      <vue-collapsible-panel :expanded="false">
        <template #title> Price </template>
        <template #content> 
          ciao
        </template>
      </vue-collapsible-panel>
    </vue-collapsible-panel-group>
  </div>
</template>

<script>

export default {
  name: "filterBox",
  data() {
    return {
      brands: [
        "Supreme",
        "Nike",
        "Adidas",
        "Yeezy",
        "Supreme",
        "Nike",
        "Adidas",
        "Supreme",
        "Nike",
        "Adidas",
        "Supreme",
        "Nike",
        "Adidas",
      ],
    };
  },
};
</script>

<style scoped>
@import '@dafcoe/vue-collapsible-panel/dist/vue-collapsible-panel.css';

.brand-box {
  min-height: 20vh;
  max-height: 30vh;
  overflow: scroll;
  text-align: left;
}

.container {
  width: 100%;
}
</style>