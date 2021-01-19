<template v-if="true">
  <div>
    <template class="ma-2">
      <v-card>
        <v-card-title>
          <v-row>
            <v-btn class="orange" @click="$router.back()">
              Back
            </v-btn>
            <v-btn class="yellow" @click="getDataFromDB">
              update!
            </v-btn>
          </v-row>
          <v-text-field
              v-model="search"
              append-icon="mdi-magnify"
              label="Search"
              single-line
              hide-details
          ></v-text-field>
        </v-card-title>
        <v-data-table
            :headers="headers"
            :items="entry"
            :search="search"
        ></v-data-table>
      </v-card>
    </template>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'MeasuringTable',

  data() {
    return {
      headers: [
        { text: 'id', value: '_id'},
        { text: 'Name', value: 'name' },
        { text: 'Description', value: 'description' },
        { text: 'Date', value: 'measuringDate' },
      ],
      entry: [],
      search: '',
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
      this.entry =this.$store.dispatch('getFromDataBase');
      console.log("ENTRY", this.entry);
    },
    /*postDataIntoDB (){
      this.$store.dispatch('postIntoDataBase', this.textfields);
    },*/
  },

  mounted() {
    console.log("mounted");
  },
  computed: {
    ...mapGetters(['getMeasuringData']),
    getAllData(){
      return this.getMeasuringData;
    }
  },

}
</script>