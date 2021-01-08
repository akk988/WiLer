<template>
  <div >

    <v-card color="grey lighten-1" class="ma-4 justify-center">
      <v-card-title class="justify-center">
        <h1>
          Hello User! 
        </h1>
      </v-card-title>
      <v-card-text class="mt-16 justify-center">
        <p>
          Adding new featurs for testing...
        </p>

        <v-col>
          <v-row class="ma-2" cols="12" lg="4" sm="6" v-for="(item,idx) in textfields" :key="idx">
            <v-text-field clearable v-model="item.input" :label="item.name"/>
          </v-row>

          <v-row cols="12">
            <v-btn color="primary" class="ma-2" @click="fetchData()">
              GET
            </v-btn>
            <v-btn color="warning" class="ma-2">
              POST
            </v-btn>
          </v-row>

          <v-row cols="12" class="ma-4">
            <p class="display-1">All Data:</p>
            <p></p>
          </v-row>
        </v-col>
        <v-col>
          <p> {{getAllData}} </p>
        </v-col>
      </v-card-text>
      <v-card-actions>
        

      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'Home',
  components: {
  },
  data() {
    return {
      textfields: [
        {name: 'Name', input: ''},
        {name: 'Number', input: ''},
        {name: 'Description', input: ''},
      ]
    }
  },
  methods: {
    fetchData(){
      this.$store.dispatch('allMessuringData');
    }
  },

  computed: {
    ...mapGetters(['getMessuringData']),
    getAllData(){
      return this.getMessuringData;
  }
  }

}
</script>
