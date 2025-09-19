describe('Search Functionality', () => {
  
  beforeEach(() => {
    cy.session('userSession', () => {
      cy.visit('/login');
      cy.get('[data-test="email"]').type('Sincere@april.biz');
      cy.get('[data-test="password"]').type('12345');
      cy.get('[data-test="signin-btn"]').click();
      cy.location('pathname').should('eq', '/dashboard');
    });
  });

  // Positive Test Cases

  it('Check search box exists', () => {
    cy.visit('/dashboard');
    cy.location('pathname').should('eq', '/dashboard');
    cy.get('[data-set="seach-box"]').should('exist');
  });

  it('Search for a valid album', () => {
    cy.visit('/dashboard');
    cy.get('[data-set="seach-box"]').type('natus impedit quibusdam illo est')
      .type('{enter}');
    cy.get('[data-set="album-search"]').should('exist');
    cy.get('[data-set="album-search"]').first().click(); 
  });

  it('Search for a partial album name', () => {
    cy.visit('/dashboard');
    cy.get('[data-set="seach-box"]').type('natus')
      .type('{enter}');
    cy.get('[data-set="album-search"]').should('exist');
    cy.get('[data-set="album-search"]').first().click(); 
  });

  it('Search with different letter case', () => {
    cy.visit('/dashboard');
    cy.get('[data-set="seach-box"]').type('QUIDEM MOLESTIAE ENIM')
      .type('{enter}');
    cy.get('[data-set="album-search"]').should('exist');
    cy.get('[data-set="album-search"]').first().click(); 
  });

  // Negative Test Cases

  it('Search with no input', () => {
    cy.visit('/dashboard');
    cy.get('[data-set="seach-box"]').type('{enter}');
    cy.get('[data-set="album-search"]').should('exist'); 
    
  });

  it('Search with a non-existent album name', () => {
    cy.visit('/dashboard');
    cy.get('[data-set="seach-box"]').type('nonexistent album name')
      .type('{enter}');
    cy.get('[data-set="album-search"]').should('not.exist'); 
    
  });

  it('Search with special characters', () => {
    cy.visit('/dashboard');
    cy.get('[data-set="seach-box"]').type('!@#$%^&*()')
      .type('{enter}');
    cy.get('[data-set="album-search"]').should('not.exist'); 
   

  it('Search with extra spaces', () => {
    cy.visit('/dashboard');
    cy.get('[data-set="seach-box"]').type('   natus   impedit    ')
      .type('{enter}');
    cy.get('[data-set="album-search"]').should('not.exist');
   
  });

  it('Search with a very long string', () => {
    cy.visit('/dashboard');
    cy.get('[data-set="seach-box"]').type('a'.repeat(1000)) // 1000 'a' characters
      .type('{enter}');
    cy.get('[data-set="album-search"]').should('not.exist'); 
  });

});

});
