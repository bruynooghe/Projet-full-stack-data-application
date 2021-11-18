<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper" @click.self="close()">
        <div class="modal-container">
          <div class="modal-header header" >
            <slot  name="header">
              Créer une annonce
            </slot>
          </div>
          <div class="modal-body" >
            <div class="form">
              <p>Pays:</p>
              <input type="text" id="country" v-model="country" required>
            </div>
            <div class="form ">
              <p>Adresse:</p>
              <input type="text" id="adress" v-model="adress" required>
            </div>
            <div class="form">
              <p>Annonce:</p>
              <input type="text" id="annonce" v-model="name" required>
            </div>
            <div class="form">
              <p>Prix:</p>
              <input type="number" id="price" v-model="price" required>
            </div>
          </div>
          <div class="modal-footer">
            <button class="modal-default-button" @click="register()" >
              Valider
            </button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
/* eslint-disable */
import {HTTP} from '../api';
import { store } from '../store/store';
export default {
  name: "modalConnection",
  components: {},
  store,
  props: ['inscription'],
  data: function () {
    return {
      name : '',
      adress:'',
      country:'',
      price:0,
      pb : false,
    }
  },
  computed: {
    user(){
      return this.$store.getters.user
    },
  },
  methods: {
    close(){
      this.name = ""
      this.country = ""
      this.adress = ""
      this.$emit('close');
    },
    setError:function(){
      if(this.name === "" ||  this.country === "" || this.adress === "" || this.price === 0)
        this.pb = true
    },
    async register(){
      this.setError()
      if(this.pb)
        return
      let result = await HTTP.post('/api/postAnnounce',{
        name:this.name,
        coutry:this.country,
        adress:this.adress,
        owner: this.user.id,
        price : this.price
      })
      this.$store.commit('updateAnnouces', result.data.data)
      this.$emit('close')
    },
  },
}
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 22rem;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
}
.header{
  color: forestgreen;
  font-size: large;
}

.modal-body {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.error{
  color: red;
}
.errorInput{
  border-top: none;
  border-right: none;
  border-left: none;
  border-bottom: 1px solid red;
}
input{
  border-top: none;
  border-right: none;
  border-left: none;
  border-bottom: 1px solid forestgreen;
  height: 1rem;
  margin-left: 1rem;
  outline: none;
}
.form{
  display: flex;
  justify-content: space-around;
  align-items: baseline;
}
.modal-default-button {
  cursor: pointer;
  float: right;
  padding: 0.5rem 1rem;
  background-color: forestgreen;
  color: white;
  border: 2px solid forestgreen;
  border-radius: 10px;

}

.modal-footer{
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 1rem;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}



</style>
