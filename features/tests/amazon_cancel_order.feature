# Created by yurka at 6/6/2021
Feature: Test cancel order

  Scenario: Cancel order is displayed
    Given Open page
    When Search for Cancel Order
    Then Verify Cancel Order is displayed