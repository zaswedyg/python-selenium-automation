# Created by yurka at 6/6/2021
Feature: Test empty cart


  Scenario: Verify cart is empty by default
    Given Open Amazon
    When Click on cart
    Then Verify cart is empty