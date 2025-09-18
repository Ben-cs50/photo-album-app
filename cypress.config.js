const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {

    //baseUrl: 'http://192.168.1.56:5000',
    baseUrl: 'http://localhost:5000',

    setupNodeEvents(on, config) {

      experimentalSessionAndOrigin: true
  
      // implement node event listeners here
    },
  },
});
