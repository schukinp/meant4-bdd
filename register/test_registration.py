from login.login_steps import *
from register.register_steps import *
from pytest_bdd import scenario


@scenario('register.feature', 'Register on web site')
def test_registration():
    pass
