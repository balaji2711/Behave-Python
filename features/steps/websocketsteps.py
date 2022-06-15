from behave import *

from actions.websocket_actions import WebsocketActions

use_step_matcher("re")


@when("I tests a valid socket connection")
def step_impl(context):
    WebsocketActions.create_connection()
    WebsocketActions.receive()
    print("Sending 'Hello, World'...")
    WebsocketActions.send("Hello, World")


@then("connection should be established")
def step_impl(context):
    print("Receiving...")
    result = WebsocketActions.receive()
    print("Received '%s'" % result)
    WebsocketActions.close()
