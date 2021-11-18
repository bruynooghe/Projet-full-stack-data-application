<template>
  <div class="bar">
    <input v-model="searchQuery" class="search_bar" placeholder="Chercher une annonce">
    <div v-show="annouces.length === 0">
      Aucune annonce publiée
    </div>
    <div class="overflow">
      <div v-for="r of resultQuery" :key="r.id" class="card_list" v-show="annouces.length !== 0">
        <div class="card">
          <p>
            Titre annonce: {{r.name}}
          </p>
          <p>
            Adresse : {{r.adress}}
          </p>
          <p>
            Ville : {{r.country}}
          </p>
          <p>
            Date de publication : {{r.day}}
          </p>
          <p>
            Prix : {{r.price}}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import { store } from '../store/store';
import {HTTP} from '../api';
export default {
  name: "SearchBar",
  store,
  props: ['isLog', 'annouces'],
  computed: {
    resultQuery(){
      if(this.searchQuery){
        return this.annouces.filter((item)=>{
          return this.searchQuery.toLowerCase().split(' ').every(v =>
            item.country.toLowerCase().includes(v) || item.adress.toLowerCase().includes(v)
            ||item.day.toLowerCase().includes(v) || item.price.toLowerCase().includes(v)
          )
        })
      }else{
        return this.annouces;
      }
    }
  },
  data() {
    return {
      searchQuery: null,
      annoucesLoad : false
    };
  },
  async mounted() {
      let result = await HTTP.get('/api/getAllAnnounces');
      this.$store.commit('updateAnnouces', result.data.data)
      this.annouces = true

  }

};
</script>

<style scoped>
input{
  border: 2px solid grey;
  outline: none;
}
input:focus{
  border: 2px solid forestgreen;
}

.bar{
  width: 82%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.overflow{
  display: flex;
  flex-wrap: wrap;
  overflow-y: auto;
  height: 100%;
}
.search_bar{
  border-radius: 10px;
  margin-bottom: 2rem;
  width: 15rem;
}
.card_list{
  align-items: center;
  margin: 0.5rem;
  overflow-y: scroll;
}
.card{
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  border: 2px solid forestgreen;
  border-radius: 5px;
  padding: 2rem;
  width: 100%;
;
}
</style>
