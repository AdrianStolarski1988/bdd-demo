Feature: as not logged user choose category in main menu and enter to category.
  In category list the user change filters of products
  and choose one of the product



  Scenario: from main site the user chose one of category
    Given the user go to main site
    When the user overrun one of the main category
    And the user choose one of subcategories "Formy do pieczenia" and click on them
    Then the user choose price filter "Cena"
#    Then the user is on search site with url "szukaj"
#    And the text in header of search is "psi patrol"
#    And the user see list of products after click on search button
#    And amount displayed product is equal with amount in hint
  #TODO dokonczyc