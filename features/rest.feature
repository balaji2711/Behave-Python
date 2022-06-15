Feature: Rest Api Specification
	Consume Get Apis

@Sanity
@Regression
@Rest

Scenario: Get API
  When I run the user request API
  Then verify the success response from user API

  @Sanity
  @Regression
  @Rest
@AUTORETRY
  Scenario: Post API
    When I run the post request API
    Then verify the success response from post API