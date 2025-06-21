# Import driver options, open the authorization window,
# and open the "Sign in by email" window.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation.test_email_window_check import email_window_check
from tests.authorisation.test_close_window import close_window


@allure.description(
    "Expected result: after clicking the 'X' button in the upper right corner, the authorization window closes."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.6.3", name="Testing the 'X' close button")
def test_close_window():
    # Open the "Sign in by email" window.
    email_window_check()

    # Run the test for closing the authorization window with the 'X' button.
    close_window()
