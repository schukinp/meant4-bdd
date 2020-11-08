import uuid
from pytest_bdd import when, parsers
from selene.api import s, browser, have


@when(parsers.parse('I create account with random email'))
def create_account_with_email():
    email = generate_email()
    s('#email_create').set(email)
    s('#SubmitCreate').click()


@when(parsers.parse('I fill required information {first_name}, {last_name}, {password}, {firstname}, {lastname},'
                    '{address1}, {city}, {state}, {postcode}, {mobile}'))
def fill_in_required_account_info(first_name,
                                  last_name,
                                  password,
                                  firstname,
                                  lastname,
                                  address1,
                                  city,
                                  state,
                                  postcode,
                                  mobile):
    s('#customer_firstname').set(first_name)
    s('#customer_lastname').set(last_name)
    s('#passwd').set(password)
    s('#passwd').set(password)
    s('#firstname').set(firstname)
    s('#lastname').set(lastname)
    s('#address1').set(address1)
    s('#city').set(city)
    s('#uniform-id_state').click()
    browser.all('option').element_by(have.text(state)).click()
    s('#postcode').set(postcode)
    s('#phone_mobile').set(mobile)
    s('#submitAccount').click()


def generate_email():
    return "{}".format(str(uuid.uuid4()))[:8] + '@example.com'
