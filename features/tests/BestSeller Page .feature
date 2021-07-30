# Created by yurka at 6/16/2021
Feature: Best Seller Page


  Scenario: Verify links
    Given Open Best Sellers
    Then Verify 5 links are displayed



  Scenario: Verify links open new page
    Given Open Best Sellers
    Then Verify user can click through links