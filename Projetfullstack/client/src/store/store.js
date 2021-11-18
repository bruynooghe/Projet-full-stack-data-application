/* eslint-disable */
import Vuex from 'vuex'
import Vue from 'vue'
import createPersistedState from 'vuex-persistedstate'
Vue.use(Vuex)

export const store = new Vuex.Store({
  plugins: [
    createPersistedState({ storage: window.sessionStorage })
  ],
  state: {
    isLog: false,
    user: {},
    announces:[]
  },
  mutations: {
    changeLog(state) {
      state.isLog = !state.isLog
    },
    updateUser(state, user){
      state.user = user
    },
    updateAnnouces(state, announce){
      state.announces = announce
    },
    freeUser(state){
      state.user = {}
    }
  },
  getters: {
    isLog: state => state.isLog,
    user: state => state.user,
    announces: state => state.announces
  }
})
