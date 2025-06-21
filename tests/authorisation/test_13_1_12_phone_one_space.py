# Import driver options and open the authorization window.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field


@allure.description(
    "Expected result: the input field does not display the entered space; after clicking the 'Log in' button, an error 'Incorrect phone number format' appears and the SMS code input window does not open."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.1.12", name="Enter one space")
def test_one_space():
    # Create an object of the PhoneField class.
    field = phone_field.PhoneField()

    # Enter one space in the phone number input field.
    authorisation_window.PHONE_INPUT_FIELD.send_keys(" ")
    time.sleep(2)

    # Verify the correct behavior for an empty input field.
    field.valid_empty_steps()

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
