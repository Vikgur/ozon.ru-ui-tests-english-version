# Class for interacting with the phone number input field.

# Import driver options and open the authorization window.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import validate_phone_field


class PhoneField:

    # Create a function to work with a valid phone number value
    # in the input field.
    def valid_steps(self):

        # Create an object of the Validate class to perform checks.
        validate = validate_phone_field.Validate()

        # Check that the entered symbols are valid.
        validate.valid_input()

        # Click on the "Log in" button.
        wait.until(
            EC.element_to_be_clickable(authorisation_window.LOGIN_BUTTON)
        ).click()
        time.sleep(2)

        # Check that the SMS code entry window opened.
        validate.sms_window_open()

    # Create a function to work with a valid but incorrect
    # phone number value in the input field.
    def valid_error_steps(self):

        # Create an object of the Validate class to perform checks.
        validate = validate_phone_field.Validate()

        # Check that the entered symbols are valid.
        validate.valid_input()

        # Click on the "Log in" button.
        wait.until(
            EC.element_to_be_clickable(authorisation_window.LOGIN_BUTTON)
        ).click()
        time.sleep(2)

        # Check that the SMS code entry window did not open.
        validate.sms_window_not_open()

    # Create a function to handle the case when the phone number input field is empty.
    def valid_empty_steps(self):
        # Create an object of the Validate class to perform checks.
        validate = validate_phone_field.Validate()

        # Check that the input field is empty.
        validate.valid_empty_input()

        # Click on the "Log in" button.
        wait.until(
            EC.element_to_be_clickable(authorisation_window.LOGIN_BUTTON)
        ).click()
        time.sleep(2)

        # Check that the error "Invalid phone format" appears.
        validate.valid_error_input()

        # Check that the SMS code entry window did not open.
        validate.sms_window_not_open()
