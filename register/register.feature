Feature: Registration
    Check I can register on web site

    Scenario: Register on web site
        Given I open homepage
        When I click Sign In
        And I create account with random email
        And I fill required information John, Doe, 123456, John, Doe, 5th Avenue, New York, New York, 10001, 0201234567
        Then I should be logged in as John Doe
        And Close browser
