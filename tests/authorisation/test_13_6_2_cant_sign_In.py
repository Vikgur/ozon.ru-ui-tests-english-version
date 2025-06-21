# Import driver options, open the authorization window,
# and open the "Sign in by email" window.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation.test_email_window_check import email_window_check
from tests.authorisation.test_cant_sign_in import cant_sign_in


@allure.description(
    "Expected result: after clicking the 'Can't sign in' button, the 'Choose a reason' window appears."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.6.2", name="Testing the 'Can't sign in' button")
def test_cant_sign_in():
    # Open the "Sign in by email" window.
    email_window_check()

    # Run the test for the "Can't sign in" button.
    cant_sign_in()
