Feature: Login
    Check I can logg in as a registered user

    Scenario: Login to the dashboard
        Given I open homepage
        When I click Sign In
        And I login as test1@example.com, 12345
        Then I should be logged in as QA Engineer
        And Close browser
