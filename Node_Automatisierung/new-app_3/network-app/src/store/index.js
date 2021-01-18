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
      console.log('(STORE)Receiving Products: ');
      return await MeasuringData.getAllData()
          .then(response => {
            console.log("allMeasuringData: ",response);
            context.commit('UPDATING_MEASURING_DATA', response.data);
      });
    },

    async allRestData(context, payload){
      console.log('(STORE)Receiving Data: ');
      return await MeasuringData.ownRestApi().then(response => {
        console.log("allRestData: ",response.data);
        context.commit('UPDATING_MEASURING_DATA', response.data);
      });
    },

    async getFromDataBase(context, payload){
      console.log('(STORE)Receiving Data: ');
      let thisData = await MeasuringData.getFromDB();
      console.log("getFromDataBase: ",thisData);
      context.commit('UPDATING_MEASURING_DATA', thisData);
       // return thisData;
    },

    async postIntoDataBase(context, payload){
      console.log('(STORE)Receiving Data: ', payload);
      let data = {
        name : payload[0].input,
        description: payload[1].input
      };
      return await MeasuringData.postIntoDB(data).then(response => {
        console.log("postIntoDataBase: ",response);
      });
    },

    
  },
  modules: {
  }
})
