from behave import *

from pages.LoginPage import LoginPage

use_step_matcher("re")


@when("I enter (?P<username>.+) and (?P<password>.+)")
def step_impl(context, username, password):
    context.loginPage = LoginPage(context.driver)
    context.loginPage.enter_username(username)
    context.loginPage.enter_password(password)


@step("I click on login button")
def step_impl(context):
    context.loginPage.click_login()


@then("login should be successful")
def step_impl(context):
    context.loginPage.is_login_successful()
