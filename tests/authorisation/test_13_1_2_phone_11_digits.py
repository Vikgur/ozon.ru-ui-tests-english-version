# Import driver options and open the authorization window.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field


@allure.description(
    "Expected result: the field displays only the first 10 digits, and after clicking the 'Log in' button, the SMS code input window appears."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.1.2", name="Enter 11 digits '99999999999'")
def test_11_digits():
    # Create an object of the PhoneField class.
    field = phone_field.PhoneField()

    # Enter the number 99999999999 in the phone number input field.
    authorisation_window.PHONE_INPUT_FIELD.send_keys(99999999999)
    time.sleep(2)

    # Check correct behavior with a valid value.
    field.valid_steps()

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
