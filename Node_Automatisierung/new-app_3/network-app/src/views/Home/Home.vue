<template>
  <div>
    <v-card color="grey lighten-1" class="ma-4 justify-center">
      <v-card-title class="justify-center">
        <h1>
          Hello User! 
        </h1>
      </v-card-title>
      <v-card-text class="mt-16">
        <v-row class="ma-5 justify-center">
          <v-btn class="green" dark  @click="$router.push('/measuringtable')">
            <v-icon left>
              mdi-table
            </v-icon>
            <span>
              DataTable
            </span>
          </v-btn>
        </v-row>
        <v-row class="ma-5 justify-center">
          <p>
            Adding new features for testing...
          </p>
        </v-row>


        <v-col>
          <v-row class="ma-2" cols="12" lg="4" sm="6" v-for="(item,idx) in textfields" :key="idx">
            <v-text-field clearable v-model="item.input" :label="item.name"/>
          </v-row>

          <v-row cols="12">
            <v-btn color="primary" class="ma-2" @click="getPlaceHolder()">
              GET Placeholder
            </v-btn>
            <v-btn color="primary" class="ma-2" @click="getRestApi()">
              Get own API
            </v-btn>
            <v-spacer></v-spacer>

            <v-btn color="primary" class="ma-2" @click="postDataIntoDB()">
              Post to DB
            </v-btn>
            <v-btn color="primary" class="ma-2" @click="getDataFromDB()">
              get from db
            </v-btn>
          </v-row>

          <v-row cols="12" class="ma-4">
            <p class="display-1">All Data:</p>
            <p></p>
          </v-row>
        </v-col>
        <v-col>
          <p>{{ getAllData }}</p>
<!--          <p>id: {{ getAllData.id }}</p>-->
<!--          <p>name: {{ getAllData.name }}</p>-->
          <!--          <p v-if="getAllData.length >= 0"> {{ getAllData.id }} </p>-->
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
        {name: 'name', input: ''},
        // {name: 'Number', input: ''},
        {name: 'description', input: ''},
      ],
    }
  },
  methods: {
    getPlaceHolder(){
      this.$store.dispatch('allMeasuringData');
    },
    getRestApi (){
      this.$store.dispatch('allRestData');
    },
    getDataFromDB (){
      this.$store.dispatch('getFromDataBase');
    },
    postDataIntoDB (){
      this.$store.dispatch('postIntoDataBase', this.textfields);
    },
  },

  computed: {
    ...mapGetters(['getMeasuringData']),
    getAllData(){
      return this.getMeasuringData;
  }
  }

}
</script>
