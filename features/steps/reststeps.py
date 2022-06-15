from behave import *
from actions.rest_actions import RestActions

use_step_matcher("re")

request = RestActions.open_rest_client()
title = None


@when("I run the user request API")
def step_impl(context):
    global title
    api_url = RestActions.apiBaseUrl + "todos/1"
    headers = {"Content-Type": "application/json"}
    response = RestActions.get(api_url, headers)
    RestActions.statusCode = response.status_code
    print(response.json())
    json_data = response.json()
    title = json_data['title']
    print(title)


@then("verify the success response from user API")
def step_impl(context):
    assert RestActions.statusCode == 200, "Status code is not matching"
    assert title == 'delectus aut autem', "Title is not matching"


@when("I run the post request API")
def step_impl(context):
    api_url = RestActions.apiBaseUrl + "todos"
    headers = {"Content-Type":"application/json"}
    data = {"userId": 1, "title": "Buy milk", "completed": False}
    response = RestActions.post(api_url, data, headers)
    RestActions.statusCode = response.status_code
    print(response.json())


@then("verify the success response from post API")
def step_impl(context):
    assert RestActions.statusCode == 201, "Status code is not matching"
