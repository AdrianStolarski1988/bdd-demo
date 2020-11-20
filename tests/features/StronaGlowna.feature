Feature: test task2
 As a user,
 I want to go to task number 2
 I want to filter product by one of category



  Scenario: check confirm working task2
    Given the user go to main site
    When the user click on task number "2"
    Then url is correct


  Scenario: check working filter
    Given check if products are displayed
    When I choose category "Sport"
    Then I expect products in category in amount "6"



