<template>
  <div class="buttons">
    <p v-if="!isLog">
      <button class="btn" @click="toogleModal(false)">
        Se Connecter
      </button>
      <button class="btn" @click="toogleModal(true)">
        S'inscrire
      </button>
    </p>
    <p v-else>
      <button class="btn" @click="disconnect">
       Se Déconnecter
      </button>
    </p>
    <modal-co v-bind:inscription="inscription" v-show="showModal" v-on:close="showModal=false"/>
  </div>
</template>

<script>
/* eslint-disable */
import { store } from '../store/store';
import {HTTP} from '../api';
import ModalCo from './modal_connection'
export default {
  name: "buttons",
  store,
  components:{ModalCo},
  props:['isLog','user'],
  data() {
    return {
      inscription : false,
      showModal:false
    };
  },
  methods:{
    toogleModal(value){
      this.inscription = value
      this.showModal = true
    },
    disconnect(){
      this.$store.commit('freeUser')
      this.$store.commit('changeLog')
    }
  }
}
</script>

<style scoped>
.buttons{
  display: flex;
  margin-right: 1rem;
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
}

.btn:active{
  color: forestgreen;
  background-color: white;
  border: 2px solid white;
  border-radius: 4px;
}
</style>
