# Import driver options and open the authorization window.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field


@allure.description(
    "Expected result: the input field displays only digits and does not show the comma; after clicking the 'Log in' button, the SMS code input window opens."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.1.9", name="Enter floating-point number with comma '9,999999999'")
def test_float_comma():
    # Create an object of the PhoneField class.
    field = phone_field.PhoneField()

    # Enter the number 9,999999999 in the phone number input field.
    authorisation_window.PHONE_INPUT_FIELD.send_keys("9,999999999")
    time.sleep(2)

    # Verify correct behavior with valid input.
    field.valid_steps()

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
