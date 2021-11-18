<template>
  <div>
    <div class="main">
      <div class="blank"></div>
      <search-bar v-bind:isLog="isLog" v-bind:annouces="announces"/>
      <buttons v-bind:isLog="isLog" v-bind:user="user"/>
    </div>
    <button class="btn" @click="toogleForm" v-show="isLog" >
      Ajouter une annonce
    </button>
    <modal_annonce v-show="showForm" @close="toogleForm"/>
  </div>
</template>

<script>
/* eslint-disable */
import searchBar from "./searchBar";
import buttons from "./buttons";
import modal_annonce from "./modal_annonce";
import {store} from '../store/store';

export default {
  name: 'home',
  components : {searchBar, buttons, modal_annonce},
  store,
  computed: {
    isLog(){
      return this.$store.getters.isLog;
    },
    user(){
      return this.$store.getters.user
    },
   announces(){
      return this.$store.getters.announces
    },
  },
  data() {
    return {
      showForm:false
    };
  },
  methods:{
    toogleForm(){
      this.showForm = !this.showForm
    }
  }
}
</script>

<style scoped>
.main{
  display: flex;
  justify-content: space-between;
}
.blank{
margin-left: 1rem;
}
.btn{
  cursor: pointer;
  padding: 0.5rem;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  font-size: 0.8rem;
  color: white;
  background-color: forestgreen;
  border: 2px solid forestgreen;
  border-radius: 4px;
  margin-bottom: 4rem;
  margin-top: 3rem;
}

.btn:active{
  color: forestgreen;
  background-color: white;
  border: 2px solid white;
  border-radius: 4px;
}
</style>
