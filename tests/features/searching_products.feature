Feature: check working search bar in store by looking paw patrol product
 As a not logged user,
 I want to find some products with collection of Paw Patrol



  Scenario: check working search products in shop
    Given the user go to main site
    When the user enter to search bar words "psi patrol" and see hint
    And the user click on search button
    Then the user is on search site with url "szukaj"
    And the text in header of search is "psi patrol"
    And the user see list of products after click on search button
    And amount displayed product is equal with amount in hint