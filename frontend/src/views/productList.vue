<template>
  <div class="grid">
    <filterBox class="sidebar"
               :brands="this.brands"
               :categories="this.categories"
               @filterPrice="filterPrice"

    />

    <div class="row-box">
      <div class="row" v-for="(row, index) in finalList">
        <div class="drip-card" v-for="item in row">
          <div class="image-box">
            <img class="item-img" :src="item.image" />
          </div>
          <div class="title-box">
            <span class="item-title">{{ item.title[0] }}</span>
          </div>
          <div class="desc-box">
            <span class="item-desc">{{ item.description[0] }}</span>
          </div>
          <div class="centered">
            <a class="item-button button-6" :href="item.link" target="_blanck">
              See the sauce
            </a>
              <a class="item-button button-6" @click="moreLikeThis" target="_blanck" :id="item.id">
                  more like this
              </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import filterBox from "@/components/filterBox.vue";

export default {
  name: "productList",
  components: {
    filterBox,
  },
  data() {
    return {
      itemList: [],
        filteredList: [],
      finalList: [],
        brands: ["supreme", "bape"],
        categories: []
    };
  },
  watch: {
    $route(newUrl, oldUrl) {
      console.log("new query", newUrl.query);

        axios({
            method: "post",
            url: "http://localhost:8888/search",
            data: newUrl.query,
        })
            .then((response) => {
                console.log(response.data);
                return response.data;
            })
            .then((data) => {
                this.itemList = Object.freeze(data);
          // console.log("itemList ", this.itemList);
          let perGroup = 4;
          let numGroups = Math.floor(this.itemList.length / perGroup) + 1;
          // console.log(numGroups);
          this.finalList = new Array(numGroups)
            .fill("")
            .map((_, i) =>
              this.itemList.slice(i * perGroup, (i + 1) * perGroup)
            );
        });
    },
  },
  beforeCreate() {

    //   TODO: category not working properly, need list of possible filters to be chosen before

    console.log("beforeCreate ", this.$route.query);
      // let query = this.$route.query;
      // delete query.brand
      // delete query.categories

      axios({
          method: "post",
          url: "http://localhost:8888/info?info=brand+category",
          data: {info: "category brand"},
      })
          .then((response) => {
              return response.data;
          })
          .then((data) => {
              console.log("////////////", data);
              this.brands = data.brand.filter(function(el) {
                  return !Number.isInteger(el) && el.length >= 3;
              })

              this.categories = data.category.filter(function(el) {
                  return !Number.isInteger(el) && el.length >= 3;
              })

          });

      axios({
          method: "post",
          url: "http://localhost:8888/search",
          data: this.$route.query,
      })
      .then((response) => {
          console.log(response.data);
          return response.data;
      })
      .then((data) => {
        this.itemList = Object.freeze(data);
        console.log("itemList ", this.itemList);
        let perGroup = 4;
        let numGroups = Math.floor(this.itemList.length / perGroup) + 1;
        console.log(numGroups);
        this.finalList = new Array(numGroups)
          .fill("")
          .map((_, i) => this.itemList.slice(i * perGroup, (i + 1) * perGroup));

          // let brandList = [...new Set(this.itemList.map((item) => item.brand))]
          // console.log("////////////",brandList)
          // this.brands = brandList

          // this.categories = [...new Set(this.itemList.map((item) => item.category[0]))]

      });
  },
  beforeMount() {},
    methods: {
        filterPrice: function (event) {
            let perGroup = 4;
            let numGroups = Math.floor(this.itemList.length / perGroup) + 1;
            this.finalList = new Array(numGroups)
                .fill("")
                .map((_, i) =>
                    this.itemList.filter((item) => {
                        let itemPrice = parseInt(item.price[0].replace("€", ""))
                        return itemPrice <= event[1] && itemPrice >= event[0]
                    }).slice(i * perGroup, (i + 1) * perGroup)
                );
        },
        moreLikeThis: function (event) {
            let itemId = event.target.id;

            axios({
                method: "post",
                url: "http://localhost:8888/moreLikeThis",
                data: {id: itemId},
            })
                .then((response) => {
                    console.log(response.data);
                    return response.data;
                })
                .then((data) => {
                    this.itemList = Object.freeze(data);
                    console.log("itemList ", this.itemList);
                    let perGroup = 4;
                    let numGroups = Math.floor(this.itemList.length / perGroup) + 1;
                    console.log(numGroups);
                    this.finalList = new Array(numGroups)
                        .fill("")
                        .map((_, i) => this.itemList.slice(i * perGroup, (i + 1) * perGroup));
                })

        }
    }
};
</script>

<style scoped>
/* @import "@coreui/coreui/dist/css/coreui.min.css"; */

.sidebar {
  max-width: 20vw;
  min-width: 20vw;
  float: left;
}

.row-box {
  max-width: 80vw;
  min-width: 80vw;
  float: right;
}

.grid {
  display: flex;
  flex-direction: row;

}

.centered {
  display: flex;
  justify-content: center;
  align-items: center;
}

.row {
  padding-left: 2vw;
  padding-right: 2vw;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;
    grid-gap: 4rem;
  margin-bottom: 2rem;
  margin-left: 1vw;
  margin-right: 5vw;
}

.row > * {
  padding-right: 0;
  padding-left: 0;
}

.drip-card {
  width: 15vw;
  height: 35vh;
  max-height: 35vh;
  border-radius: 25px;
  display: grid;
  grid-template-areas:
    "image"
    "title"
    "descritpion"
    "button";
  grid-template-columns: 1fr;
  grid-template-rows: 4fr 2fr 2.5fr 1fr;
  grid-column-gap: 0px;
  grid-row-gap: 0px;

  box-shadow: 0 0 20px 8px #d0d0d0;
}

.item-img {
  width: 60%;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.image-box {
  border-top-left-radius: 25px;
  border-top-right-radius: 25px;
  grid-area: image;
  border-top: 25px;
  height: 100%;
  width: 100%;
}

.title-box {
  grid-area: title;
  width: 100%;
}

.item-title {
  font-weight: bold;
  font-size: 1rem;
}

.desc-box {
  grid-area: descritpion;
  /*background: #2c3e50;*/
  height: 100%;
  overflow: scroll;
  width: 100%;
  max-height: 100%;
}

.item-desc {
  font-size: 0.8rem;
  height: 100%;
  max-height: 100%;
}

.item-button {
  width: 60%;
  max-height: 70%;
  grid-area: button;
  border-radius: 25px;
  font-size: 0.8rem;
}

/* CSS */
.button-6 {
  align-items: center;
  background-color: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 0.25rem;
  box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0;
  box-sizing: border-box;
  color: rgba(0, 0, 0, 0.85);
  cursor: pointer;
  display: inline-flex;
  justify-content: center;
  line-height: 1.25;
  padding: calc(0.875rem - 1px) calc(1.5rem - 1px);
  position: relative;
  text-decoration: none;
  transition: all 250ms;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: baseline;
  width: auto;
}

.button-6:hover,
.button-6:focus {
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 12px;
  color: rgba(0, 0, 0, 0.65);
}

.button-6:hover {
  transform: translateY(-1px);
}

.button-6:active {
  background-color: #f0f0f1;
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.06) 0 2px 4px;
  color: rgba(0, 0, 0, 0.65);
  transform: translateY(0);
}
</style>