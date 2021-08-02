# Created by yurka at 8/1/2021
Feature: Cart

  Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify 'Your Amazon Cart is empty' text present