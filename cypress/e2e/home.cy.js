describe('Demo Web App - Login & Dashboard', () => {

    let startTime, endTime;

    before(() => {
        startTime = performance.now();
    });

    beforeEach(() => {
        cy.visit('http://localhost/home.html'); // folosit xampp local
    });

    after(() => {
        endTime = performance.now();
        const duration = ((endTime - startTime) / 1000).toFixed(2);
        cy.log(`Timp total de executie: ${duration} secunde`);
        console.log(`Timp total de executie: ${duration} secunde`);
    });

    it('err - invalid login', () => {
        cy.get('#username').type('wrong');
        cy.get('#password').type('wrong');
        cy.get('#login-container').find('button').click();
        cy.get('#error-msg').should('be.visible');
    });

    it('succes - user/pswd corecte', () => {
        cy.get('#username').type('test123');
        cy.get('#password').type('test123');
        cy.get('#login-container').find('button').click();
        cy.get('#dashboard-container').should('be.visible');
        cy.get('#user-name').should('contain', 'test123');
    });

    it('trimite feedback + return confirmare', () => {
        // login first
        cy.get('#username').type('test123');
        cy.get('#password').type('test123');
        cy.get('#login-container').find('button').click();

        cy.get('#feedback').type('Great website!');
        cy.contains('Trimitere Feedback').click();
        cy.get('#feedback-msg').should('be.visible');
    });

    it('logout + return la login form', () => {
        // login first
        cy.get('#username').type('test123');
        cy.get('#password').type('test123');
        cy.get('#login-container').find('button').click();

        // logout
        cy.contains('Logout').click();
        cy.get('#login-container').should('be.visible');
        cy.get('#dashboard-container').should('not.be.visible');
    });

});
