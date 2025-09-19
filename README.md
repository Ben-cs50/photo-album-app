# Photo Album App

A web application for managing photo albums and subscribing to updates, with automated end-to-end testing using **Cypress** and **Mochawesome** for detailed test reports.


The application uses **Cypress** for end-to-end testing to ensure reliability, and **Mochawesome** for generating interactive test reports.


## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Ben-cs50/photo-album-app.git
cd photo-album-app
npm install
```

---

## Running the App

Start your local server (Node.js or Flask):

```bash
npm start
```

Open the application in your preferred browser:

```
http://localhost:5000
```

---

## Testing

### Open Cypress Test Runner (GUI)

```bash
npx cypress open
```

This launches the interactive Cypress Test Runner for running tests visually.

### Run Cypress Tests Headless (Faster)

```bash
npx cypress run --browser chrome --headless
```

You can replace `chrome` with `firefox`, `edge`, or any installed browser.



### Steps to generate and view a report

1. Run Cypress tests:

```bash
npx cypress run
```

2. Open the generated report in any browser:

* Report path: `cypress/reports/html/index.html`
* You can double-click the file or use `Ctrl+O` in a browser to open it.

> The report includes:

> * Detailed test results
> * Screenshots for failures
> * Interactive charts




