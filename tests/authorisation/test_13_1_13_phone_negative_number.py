# Import driver options and open the authorization window.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field


@allure.description(
    "Expected result: the input field displays only digits and does not display the minus sign; after clicking the 'Log in' button, an error 'Incorrect phone number format' appears and the SMS code input window does not open."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase(
    "Ozon-13.1.13", name="Enter a number with a negative value '-9999999999'"
)
def test_negative_number():
    # Create an object of the PhoneField class.
    field = phone_field.PhoneField()

    # Enter the number -9999999999 in the phone number input field.
    authorisation_window.PHONE_INPUT_FIELD.send_keys(-9999999999)
    time.sleep(2)

    # Verify the correct behavior with a valid value.
    field.valid_steps()

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
