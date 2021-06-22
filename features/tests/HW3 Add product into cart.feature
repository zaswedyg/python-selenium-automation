# Created by yurka at 6/16/2021
Feature: Adding product into cart


  Scenario: Add product into cart
    Given Open product page
    When Add product into cart
    Then Verify product is added