# Import driver options and open the authorization window.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field


@allure.description(
    "Expected result: after clicking the 'Log in' button, an error message 'Invalid phone format' appears, and the SMS code input window does not open."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.1.5", name="Leave the field empty")
def test_empty_field():
    # Create an object of the PhoneField class.
    field = phone_field.PhoneField()

    # Check correct behavior with an empty phone number input field.
    field.valid_empty_steps()

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
