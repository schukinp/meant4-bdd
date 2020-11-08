from selene.api import s, browser, be, have
from pytest_bdd import given, when, then, parsers
from conftest import base_url


@given('I open homepage')
def open_home_page():
    browser.open_url(base_url)


@when("I click Sign In")
def click_sign_in():
    s('a[title="Log in to your customer account"]').click()


@when(parsers.parse("I login as {email}, {password}"))
def login_as(email, password):
    s('#email').set(email)
    s('#passwd').set(password)
    s('#SubmitLogin').click()


@then(parsers.parse("I should be logged in as {username}"))
def check_if_logged_in_as(username):
    s('a[title="Log me out"]').should(be.visible)
    s('.header_user_info').should(have.text(username))


@then("Close browser")
def close_browser():
    browser.quit()
