<template>
  <v-footer
    color="primary lighten-1"
    padless
  >
    <v-row
      justify="center"
      no-gutters
    >
      <v-btn
        v-for="link in links"
        :key="link.link"
        color="white"
        text
        rounded
        class="my-2"
        :to="link.route"
      >
        {{ link.link }}
      </v-btn>
      <v-col
        class="primary lighten-2 py-4 text-center white--text"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>Fraunhofer-IPA</strong>
      </v-col>
    </v-row>
  </v-footer>
</template>

<script>
  export default {
    data: () => ({
      links: [
        {link:'Home' , route:'/'},
        {link:'About', route:'/about'},
        {link:'Team', route:'/team'},
        {link:'Contact', route:'/contact'},
      ],
    }),
  }
</script>