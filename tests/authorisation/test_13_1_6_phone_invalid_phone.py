# Import driver options and open the authorization window.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field


@allure.description(
    "Expected result: the field displays the entered characters, and after clicking the 'Log in' button, an error message 'Invalid phone format' appears, and the SMS code input window does not open."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.1.6", name="Enter an invalid phone number '1111111111'")
def test_invalid_phone():
    # Create an object of the PhoneField class.
    field = phone_field.PhoneField()

    # Enter the number 1111111111 into the phone input field.
    authorisation_window.PHONE_INPUT_FIELD.send_keys(1111111111)
    time.sleep(2)

    # Verify correct behavior with a valid but incorrect value.
    field.valid_error_steps()

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
