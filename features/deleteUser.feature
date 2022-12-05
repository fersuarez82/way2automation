Feature: Delete User
    Scenario: Delete user novak and validate the user has been deleted from the table
        Given launch chrome browser
        When open way2automation page
        And user novak exists
        And delete user novak
        Then validate deleted user
        And close browser