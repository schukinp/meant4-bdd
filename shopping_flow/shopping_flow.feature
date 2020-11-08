Feature: Shopping flow
    Check I purchase something on web site

    Scenario: Purchase something on web site
        Given I open homepage
        When I click Sign In
        And I login as test1@example.com, 12345
        Given I open homepage
        When I add first popular item to chart and proceed to checkout
        And I click Proceed to checkout on Summary tab
        And I click Proceed to checkout on Address tab
        And I click Agree to ToS and Proceed to checkout on Shipping tab
        And I select Pay by bank wire and Confirm order
        Then I should see my order is complete
        And Close browser
