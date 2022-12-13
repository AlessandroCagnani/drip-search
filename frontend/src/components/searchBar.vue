<template>
    <div class="container">
        <div class="bar">
            <input v-model="searchQuery" @keyup.enter="search" class="searchbar" title="searchbar" type="text" placeholder="drip your self">
        </div>
    </div>
</template>

<script>
export default {
    name: "searchBar",
    data() {
        return {
            searchQuery: ""
        }
    },
    beforeMount() {
        let url = new URL(window.location.href);
        let params = new URLSearchParams(url.search);
        if (params.has("q")) {
            this.searchQuery = params.get("q");
        }
    },
    methods: {
        search: function(event) {
            
            let query = event.target.value
            console.log("searching:  ", query);

            this.$router.push({
                name: "search",
                query: {
                    q: query,
                    // brands: '#',
                    // category: '#',
                    // price: '#',
                }
            });
            
        }
    }
}



</script>

<style scoped>
    .container {
        width: 100%;
        height: 100%;
    }

    .searchbar{
        height:45px;
        border: none;
        width:500px;
        font-size:16px;
        outline: none;
    }
    .bar{
        margin:0 auto;
        width:575px;
        border-radius:30px;
        border:1px solid #dcdcdc;
        background-color: white;
    }
    .bar:hover{
        box-shadow: 1px 1px 8px 1px #dcdcdc;
    }
    .bar:focus-within{
        box-shadow: 1px 1px 8px 1px #dcdcdc;
        outline:none;
    }
</style>