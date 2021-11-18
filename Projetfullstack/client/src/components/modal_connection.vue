<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper" @click.self="close()">
        <div class="modal-container">
          <div class="modal-header header" >
            <slot  name="header" v-if="inscription">
              Formulaire d'inscription
            </slot>
            <slot name="header" v-else>
              Formulaire de connexion
            </slot>
          </div>

          <div class="modal-body" v-show="inscription">
            <div class="form">
              <p v-bind:class="{error: email_use}">Email:</p>
              <input type="text" id="ins_email" v-model="email" required v-bind:class="{errorInput:email_use}">
            </div>
            <div v-show="email_use" class="error">Email déjà associé à un compte</div>

            <div class="form ">
              <p>Prénom:</p>
              <input type="text" id="ins_name" v-model="name" required>
            </div>
            <div class="form">
              <p>Mot de passe:</p>
              <input type="password" id="ins_password" v-model="password" required>
            </div>
          </div>
          <div class="modal-body" v-show="!inscription">
            <div class="form">
              <p v-bind:class="{error: !email_exist}">Email:</p>
              <input type="text" id="co_email" v-model="email" required v-bind:class="{errorInput:!email_exist}">
            </div>
            <div v-show="!email_exist" class="error">Aucun compte n'existe pour cet email</div>
            <div class="form">
              <p v-bind:class="{error: wrong_pw}">Mot de passe:</p>
              <input type="password" id="co_password" v-model="password" required v-bind:class="{errorInput:wrong_pw}">
            </div>
            <div v-show="wrong_pw" class="error">Mauvais mot de passe</div>
          </div>
          <div class="modal-footer">
              <button class="modal-default-button" @click="login()" v-show="!inscription">
                Se Connecter
              </button>
              <button class="modal-default-button" @click="signUp()" v-show="inscription">
                S'inscrire
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
      email : '',
      password:'',
      name:'',
      pb_email : false,
      pb_pw : false,
      pb_name : false,
      email_use : false,
      email_exist:true,
      wrong_pw: false,
    }
  },
  mounted(){

  },
  methods: {
    close(){
      this.email = ""
      this.password = ""
      this.name = ""
      this.$emit('close');
    },
    setPbName:function(){
      this.pb_name = this.name === "";
    },
    setPbEmail:function(){
      this.pb_email = this.email === "";
    },
    setPbPw:function(){
      this.pb_pw = this.password === "";
    },
    async login(){
      this.setPbEmail()
      this.setPbPw()
      if(this.pb_email && this.pb_name && this.pb_pw)
        return
      let result = await HTTP.get('/api/login?email=' + this.email +"&password=" + this.password)
      if (result.status === 203) {
        this.email_exist = !this.email_exist
        return
      }
      this.email_exist = true
      if(result.status === 202){
        this.wrong_pw = !this.wrong_pw
        return
      }
      this.wrong_pw = false
      this.$store.commit('changeLog')
      this.$store.commit('updateUser', result.data)
      this.$emit('close')
    },
    async signUp(){
      this.setPbName()
      this.setPbEmail()
      this.setPbPw()
      if(this.pb_email && this.pb_name && this.pb_pw)
        return
      let result = await HTTP.post('/api/signUp',{name:this.name, email:this.email, password:this.password})
      if (result.status === 205) {
        this.email_use = true
        return
      }
      this.email_use = false
      this.$store.commit('updateUser', {
        name : this.name,
        email : this.email,
        id : result.data.id
      })
      this.$store.commit('changeLog')
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
