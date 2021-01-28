<template>
  <v-app>
    <NavBar/>
    <v-main class="blue-grey darken-3">
      <router-view :key="$route.path" />
    </v-main>
    <Footer/>
  </v-app>
</template>

<script>
import Footer from './views/Navigation/Footer/Footer';
import NavBar from './views/Navigation/NavBar/NavBar';

export default {
  name: 'App',

  components: {
    Footer,NavBar,
  },

  data: () => ({
    //
  }),
};
</script>
