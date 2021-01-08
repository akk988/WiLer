import Vue from 'vue'
import Vuex from 'vuex'
import MessuringData from '@/services/messuring/messuring';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    messuringData: {},
  },
  getters: {
    getMessuringData: (state) => {
      return state.messuringData;
    }
  },
  mutations: {
    UPDATING_MESSURING_DATA: (state, payload) => {
      state.messuringData = payload;
    },
  },


  actions: {

    async allMessuringData(context, payload){
      console.log('Receiving Products: ');
      return await MessuringData.getAllData().then(response => {
        context.commit('UPDATING_MESSURING_DATA', response.data);
      });
    },

    
  },
  modules: {
  }
})
