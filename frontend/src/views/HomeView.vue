<template>
  <div class="home">
    <img alt="Vue logo" style="z-index: 99" src="https://media.tenor.com/aq5K__vIxCEAAAAC/migos-offset.gif">
      <img class="img2" alt="Vue logo" src="https://media.tenor.com/-Wv6EYAsZeAAAAAM/she-belongs-to-the-streets-quote.gif">
    <img class="img3" src="https://media3.giphy.com/media/xUNemZ9kOGc3aaITL2/giphy.gif?cid=ecf05e47l6g27o8zuq6t8mshy5klpvejkterzths0byxrmoo&rid=giphy.gif&ct=g">
    <img class="img1" src="https://media1.giphy.com/media/zMCfqXkwjmTO8/giphy.webp?cid=ecf05e47ehk6xmmbyvuxvja1j8vez5gtb6arymox2drj668v&rid=giphy.webp&ct=g">
      <img class="img4" src="https://media1.giphy.com/media/1zkMcXq96o2PTyEI6P/200w.webp?cid=ecf05e474d8oypqnal7ib3iaza2d8qjrzxoqfnbt09e34hqg&rid=200w.webp&ct=g">
    <img class="img5" src="https://media2.giphy.com/media/L2NGCuEpVpaJTK0sT1/200w.webp?cid=ecf05e472sl7s6i53tfbo55g8wqmqndrn001srxgzwkmyxpp&rid=200w.webp&ct=s">
    <img class="img6" src="https://media0.giphy.com/media/29Ial6OEeJLNZbhBkE/200w.webp?cid=ecf05e473cd5oklhsqzh9z678y5cen09a3y5xgce5z063l6j&rid=200w.webp&ct=s">
      <img  class="img7" src="https://media4.giphy.com/media/w6MgSJYxkk45jMjs6p/giphy.webp?cid=ecf05e47po1ruqu6tuzdo1y3w3iax3ikg8x7f8py5nef7b3q&rid=giphy.webp&ct=s">
    <img class="img8" src="https://media2.giphy.com/media/8JZjgPr6Enkpfa40Kd/giphy.webp?cid=ecf05e474irvjcz2h0azcnnpt8rgvx9qkqd94d7h9l1nwvsl&rid=giphy.webp&ct=s">
      <img class="img9" src ="https://media1.giphy.com/media/39U3UkOawgxaS4Y1JD/200w.webp?cid=ecf05e47bnhvnvyg05vx5g6uu7s5bqojyelag4cxk9ij39rk&rid=200w.webp&ct=ts">
    <img class="img10" src="https://media1.giphy.com/media/ldHhiwBKxuUTkyQ5GB/200w.webp?cid=ecf05e479ppcagb8rtio74a3h7wfw5ds7b06zgc8o5uj6yp9&rid=200w.webp&ct=s">

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

<style scoped>

    .home {
        background-image: url("https://media.tenor.com/aq5K__vIxCEAAAAC/migos-offset.gif");
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center;
        height: 85.7vh;
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
        overflow: hidden;

    }


    img {
        position: absolute;
    }

    .img1 {
        top: 50%;
        left: 30%;
        z-index: 1;
    }

    .img2 {
        z-index: 1;
        bottom: 20px;
        right: 60px;
    }

    .img3 {
        height: 10rem;
        width: 10rem;
        top: 20px;
        left: 20px;
    }

    .img4 {
        height: 10rem;
        width: 30rem;
        top: 20%;
        right: 20%;
    }

    .img5 {
        z-index: 2;
        width: 25%;
        bottom: -20%;
        left: 10px;
    }

    .img6 {
        z-index: 1;
        bottom: 20px;
        left: 20px;
    }

    .img7 {
        z-index: 2;
        bottom: 30%;
        right: 5px;
        width: 10rem;
    }

    .img8 {
        z-index: 1;
        top: -50px;
        right: -20px;
        width: 18em;
    }

    .img10 {
        z-index: 100;
        top: -30px;
        left: 7%;
        width: 30rem;
    }

    .img9 {
        z-index: 100;
        bottom: 0px;
        right: 13%;
        width: 30rem;
    }



</style>