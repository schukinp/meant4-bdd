from selene.api import s, by, be, ss
from pytest_bdd import when, then


@when('I add first popular item to chart and proceed to checkout')
def add_first_popular_item_to_cart_and_proceed_to_checkout():
    s('.product-container').hover()
    s('a[title="Add to cart"]').click()
    s('a[title="Proceed to checkout"]').click()


@when('I click Proceed to checkout on Summary tab')
def proceed_to_checkout_on_summary():
    ss('a[title="Proceed to checkout"]')[1].click()


@when('I click Proceed to checkout on Address tab')
def proceed_to_checkout_on_address():
    s(by.name('processAddress')).click()


@when('I click Agree to ToS and Proceed to checkout on Shipping tab')
def proceed_to_checkout_on_shipping():
    s('#uniform-cgv').click()
    s(by.name('processCarrier')).click()


@when('I select Pay by bank wire and Confirm order')
def proceed_to_checkout_on_shipping():
    s('a[title="Pay by bank wire"]').click()
    s(by.text('I confirm my order')).click()


@then('I should see my order is complete')
def check_order_is_complete():
    s(by.text('Your order on My Store is complete.')).should(be.visible)
