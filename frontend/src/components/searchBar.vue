<template>
    <div class="container">
        <div class="bar">
            <input class="searchbar" title="searchbar" type="text" placeholder="Aim to the drip">
        </div>
    </div>
</template>

<script>
export default {
    name: "searchBar"
}
</script>

<style scoped>
    .container {
        margin-top: 5%;
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
    }
    .bar:hover{
        box-shadow: 1px 1px 8px 1px #dcdcdc;
    }
    .bar:focus-within{
        box-shadow: 1px 1px 8px 1px #dcdcdc;
        outline:none;
    }
</style>