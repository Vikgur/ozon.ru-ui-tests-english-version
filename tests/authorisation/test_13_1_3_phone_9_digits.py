# Import driver options and open the authorization window.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field


@allure.description(
    "Expected result: the field displays the entered characters, after clicking the 'Log in' button, an error message 'Invalid phone format' appears, and the SMS code input window does not open."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.1.3", name="Enter 9 digits '999999999'")
def test_9_digits():
    # Create an object of the PhoneField class.
    field = phone_field.PhoneField()

    # Enter the number 999999999 in the phone number input field.
    authorisation_window.PHONE_INPUT_FIELD.send_keys(999999999)
    time.sleep(2)

    # Check correct behavior with a valid but incorrect value.
    field.valid_error_steps()

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
