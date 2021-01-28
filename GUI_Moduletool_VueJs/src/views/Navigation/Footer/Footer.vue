<template>
  <v-footer
    dark
    padless
  >
    <v-row
      justify="center"
      no-gutters
    >
      <v-btn
        v-for="link in links"
        :key="link"
        color="white"
        text
        rounded
        class="my-2"
        :to="link.route"
        small
      >
        {{ link.link }}
      </v-btn>
      <v-col class="text-center" cols="12">
        {{ new Date().getFullYear() }}  <strong> <v-icon>mdi-copyright</v-icon> Fraunhofer-IPA</strong>
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