import Vue from 'vue'
import Vuex from 'vuex'
import MeasuringData from '@/services/measuring/measuring';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    measuringData: {},
  },
  getters: {
    getMeasuringData: (state) => {
      return state.measuringData;
    }
  },
  mutations: {
    UPDATING_MEASURING_DATA: (state, payload) => {
      console.log("UPDATING_MEASURING_DATA", payload)
      state.measuringData = payload;
    },
  },


  actions: {

    async allMeasuringData(context, payload){
      console.log('Receiving Products: ');
      return await MeasuringData.getAllData().then(response => {
        console.log("....-",response);
        context.commit('UPDATING_MEASURING_DATA', response.data);
      });
    },

    async allRestData(context, payload){
      console.log('Receiving Data: ');
      return await MeasuringData.ownRestApi().then(response => {
        console.log("....-",response);
        context.commit('UPDATING_MEASURING_DATA', response.data);
      });
    },

    
  },
  modules: {
  }
})
