Feature: Login
  Check login scenario in sauce demo application

  @Sanity
    @Regression
    @Web
  Scenario Outline: Verify the user is able to login into sauce demo application
    When I enter <username> and <password>
    And I click on login button
    Then login should be successful

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |
