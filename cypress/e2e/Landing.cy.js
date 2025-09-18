describe('Landing Page', () => {
  beforeEach(() => {
    cy.visit('/')
  });

  it('Landing Page exist', () => {
    cy.get('[data-test="Landing"]').should('exist')
    
  })
  
  it('Landing title exist', () => {
    cy.get('[data-test="landing-title"]').should('be.visible')
    .and('contain.text', 'Welcome to Gallery')

  })

  it('Landing subtitle exist', () => {
    cy.get('[data-test="landing-subtitle"]').should('be.visible')
    .and('contain.text', 'Browse albums and photos powered')

  })

  it('Navigates to login when button is clicked', () => {
    cy.get('[data-test="login-btn"]').should('be.visible').click()
    cy.location('pathname').should('eq', '/login')


  })
  
  it('Navigates to signup when button is clicked', () => {
    cy.visit('/')
    cy.get('[data-test="signup-btn"]').should('be.visible').click()
    cy.location('pathname').should('eq', '/signup')

      //go back to landing page
    cy.go('back')
   

  
})

})