# Import driver options and open the authorization window.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field


@allure.description(
    "Expected result: the input field does not display the entered character, and after clicking the 'Log in' button, an error message 'Invalid phone format' appears, and the SMS code input window does not open."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.1.8", name="Enter Cyrillic letter 'ж'")
def test_cyrillic():
    # Create an object of the PhoneField class.
    field = phone_field.PhoneField()

    # Enter "ж" into the phone number input field.
    authorisation_window.PHONE_INPUT_FIELD.send_keys("ж")
    time.sleep(2)

    # Verify correct behavior with an empty input field after filtering invalid input.
    field.valid_empty_steps()

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
