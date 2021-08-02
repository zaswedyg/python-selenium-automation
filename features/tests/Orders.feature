# Created by yurka at 8/1/2021
Feature: Orders

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened