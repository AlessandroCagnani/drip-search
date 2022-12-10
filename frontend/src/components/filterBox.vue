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
                id="brand"
                :value="brand"
                v-model="filteredBrands"
                @click="filterBrand"
              />
            </div>
          </div>
        </template>
      </vue-collapsible-panel>
      <vue-collapsible-panel :expanded="false">
        <template #title> Category </template>
        <template #content>
            <div class="brand-box">
                <div class="brand-check" v-for="category in categories">
                    <label :for="category">{{ category }}</label>
                    <input
                        type="checkbox"
                        id="category"
                        :value="category"
                        v-model="filteredCategories"
                        @click="filterCategories"
                    />
                </div>
            </div>
        </template>
      </vue-collapsible-panel>
      <vue-collapsible-panel :expanded="false">
        <template #title> Price </template>
        <template #content> 
          <p>Price range</p>
          <Slider v-model="value" :lazy="false" :min="0" :max="2000" @change="filterPrice"/>
        </template>
      </vue-collapsible-panel>
    </vue-collapsible-panel-group>
    <h5 @click="reset">reset</h5>
  </div>

</template>

<script>
import Slider from '@vueform/slider'

export default {
  name: "filterBox",
  components: {
    Slider
  },
    props: {
        brands : null,
        categories : { type: Array, required: false },
        priceRange: { type: Array, required: false }

    },
  data() {
    return {
      value: [0, 2000],

        filteredBrands: [],
        filteredCategories: [],

    };
  },
    methods: {
    filterBrand: function(event) {

        let value = event.target.value

        let toAdd = event.target.checked

        let query = this.$route.query;

        if (toAdd) {
            this.filteredBrands.push(value)
        } else {
            this.filteredBrands = this.filteredBrands.filter((item) => item !== value)
        }
        let brandQuery = this.filteredBrands.join(" ")

        console.log("//// brand query ", brandQuery)

        if (brandQuery) {
            if (query.categories) {
                this.$router.replace({
                    query: {
                        q: query.q,
                        brand: brandQuery,
                        categories: query.categories
                    }
                })
            } else {
                this.$router.replace({
                    query: {
                        q: query.q,
                        brand: brandQuery
                    }
                })
            }
        } else {
            if (query.categories) {
                this.$router.replace({
                    query: {
                        q: query.q,
                        categories: query.categories,
                    }
                })
            } else {
                this.$router.replace({
                    query: {
                        q: query.q,
                    }
                })
            }
        }

    },
    filterCategories: function (event) {

        let value = event.target.value

        console.log("//// id; ", event.target.id)

        let toAdd = event.target.checked

        let query = this.$route.query;

        if (toAdd) {
            this.filteredCategories.push(value)
        } else {
            this.filteredCategories = this.filteredCategories.filter((item) => item !== value)
        }
        let categoryQuery = this.filteredCategories.join(" ")

        console.log("//// category query ", categoryQuery)

        if (categoryQuery) {

            if (query.brand) {
                this.$router.push({
                    name: "search",
                    query: {
                        q: query.q,
                        brand: query.brand,
                        categories: categoryQuery
                    }
                })
            } else {
                this.$router.push({
                    name: "search",
                    query: {
                        q: query.q,
                        categories: categoryQuery,
                    }
                })
            }
        } else {
            if (query.brand) {
                this.$router.push({
                    name: "search",
                    query: {
                        q: query.q,
                        brand: query.brand,
                    }
                })
            } else {
                this.$router.push({
                    name: "search",
                    query: {
                        q: query.q,
                    }
                })
            }
        }
    },
        filterPrice: function (event) {
            this.$emit('filterPrice', event)
        },
    reset: function() {
        this.filteredBrands = []
        this.filteredCategories = []
        this.value = [0,2000]
        this.$emit('filterPrice', this.value)
    }
    },
};



</script>

<style scoped>
@import '@dafcoe/vue-collapsible-panel/dist/vue-collapsible-panel.css';
@import "@vueform/slider/themes/default.css";

.brand-box {
  min-height: 20vh;
  max-height: 30vh;
  overflow: scroll;
  text-align: left;
    font-size: 1.5rem;
}

.container {
  width: 100%;
}

.brand-check {
    display: block;
}

.brand-check label {
    min-width: 80%;
}
</style>