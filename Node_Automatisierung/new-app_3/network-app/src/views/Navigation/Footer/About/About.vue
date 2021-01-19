<template>
  <div class="about">
    <h1>This is an about page</h1>
    <p>hallo</p>
    <v-row >
      <v-col cols="12" md="6" sm="12" class="justify-center" align="center" >
        <v-btn class="red" dark @click="test()">
          <v-icon left>
            mdi-heart
          </v-icon>
          hallo
        </v-btn>
      </v-col>
      <v-col cols="12" md="6" sm="12"  class="justify-center">
        <v-btn class="red" dark>
          <v-icon left>
            mdi-heart
          </v-icon>
          hallo
        </v-btn>
      </v-col>
    </v-row>

  </div>
</template>

<script>
export default {
  name: 'About',
  methods: {
    test() {
      console.log("hallo");
    }
  }
};

</script>
