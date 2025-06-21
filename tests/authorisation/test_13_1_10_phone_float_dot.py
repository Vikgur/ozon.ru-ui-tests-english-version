# Import driver options and open the authorization window.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field


@allure.description(
    "Expected result: the input field displays only digits and does not show the dot; after clicking the 'Log in' button, an error 'Incorrect phone number format' appears and the SMS code input window does not open."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.1.10", name="Enter floating-point number with dot '9.999999999'")
def test_float_dot():
    # Create an object of the PhoneField class.
    field = phone_field.PhoneField()

    # Enter the number 9.999999999 in the phone number input field.
    authorisation_window.PHONE_INPUT_FIELD.send_keys("9.999999999")
    time.sleep(2)

    # Verify correct behavior with valid input (note: should be an error).
    field.valid_error_steps()

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
