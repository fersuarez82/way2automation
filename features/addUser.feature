Feature: Add User
    Scenario: Add a User and validate the user has been added to the table
        Given launch chrome browser
        When open way2automation page
        And add a user
        Then validate added user
        And close browser

