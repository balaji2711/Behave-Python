Feature: Websocket Specification
	Consume Web Socket

@Sanity
@Regression
  @Websocket
Scenario: Hello World Websocket
  When I tests a valid socket connection
  Then connection should be established