const { defineConfig } = require("cypress");

module.exports = defineConfig({

  reporter: 'cypress-mochawesome-reporter',
  
  e2e: {
    //baseUrl: 'http://192.168.1.56:5000',
    baseUrl: 'http://localhost:5000',

    setupNodeEvents(on, config) {
      require('cypress-mochawesome-reporter/plugin')(on);
      return config;
    },

    reporter: 'cypress-mochawesome-reporter',
    reporterOptions: {
      reportDir: 'cypress/reports/html',
      overwrite: true,
      html: true,
      json: true,
      reportFilename: 'index',
      charts: true,
      embeddedScreenshots: true,
      inlineAssets: true,
      saveHtml: true,
      saveJson: true
    }
  }
});
