# Class for validating the phone number input field.

from tests.authorisation.test_auth_window_imports_options import *


class Validate:

    # Function to check that only valid characters are entered into the phone number field.
    def valid_input(self):

        # Create a variable to check the presence of the element.
        PHONE_INPUT_CHECK = driver.find_elements(
            *MainPageAuthorisationWindowLocators.PHONE_INPUT_CHECK_LOCATOR
        )

        # Check via assert.
        assert (
            len(PHONE_INPUT_CHECK) == 0
        ), "Invalid characters entered into the phone number field :-("

        # Check via print.
        if len(PHONE_INPUT_CHECK) == 0:
            print("Valid characters entered into the phone number field!")
        else:
            print("Invalid characters entered into the phone number field :-(")

    # Function to check that no characters are present in the phone number field.
    def valid_empty_input(self):

        # Create a variable to check the presence of the element.
        PHONE_INPUT_CHECK = driver.find_elements(
            *MainPageAuthorisationWindowLocators.PHONE_INPUT_CHECK_LOCATOR
        )

        # Check via assert.
        assert (
            len(PHONE_INPUT_CHECK) > 0
        ), "Valid characters unexpectedly present in the phone number field :-("

        # Check via print.
        if len(PHONE_INPUT_CHECK) > 0:
            print("No characters present in the phone number field!")
        else:
            print("Valid characters unexpectedly present in the phone number field :-(")

    # Function to check for the error message "Invalid phone format"
    # in the phone number input field.
    def valid_error_input(self):

        # Create a locator variable for the check.
        ERROR_CHECK_LOCATOR = (
            "xpath",
            "//p[normalize-space(.)='Некорректный формат телефона']",
        )

        # Create a variable to check the presence of the element.
        ERROR_CHECK = driver.find_elements(*ERROR_CHECK_LOCATOR)

        # Check via assert.
        assert (
            len(ERROR_CHECK) > 0
        ), "Expected error not found — valid characters may have been entered :-("

        # Check via print.
        if len(ERROR_CHECK) > 0:
            print('Error "Invalid phone format" appeared!')
        else:
            print("Expected error not found — valid characters may have been entered :-(")

    # Function to check that the SMS code entry window has opened.
    def sms_window_open(self):

        # Create locator variables for the check.
        SMS_CODE_CHECK_LOCATOR_1 = ("xpath", "//span[normalize-space(.)='Введите код']")
        SMS_CODE_CHECK_LOCATOR_2 = (
            "xpath",
            "//span[normalize-space(.)='Превышено количество попыток ввода']",
        )

        # Create variables to check for the presence of elements.
        SMS_CODE_CHECK_1 = driver.find_elements(*SMS_CODE_CHECK_LOCATOR_1)
        SMS_CODE_CHECK_2 = driver.find_elements(*SMS_CODE_CHECK_LOCATOR_2)

        # Check via assert.
        assert (
            len(SMS_CODE_CHECK_1) > 0 or len(SMS_CODE_CHECK_2) > 0
        ), "SMS code entry window did not open :-("

        # Check via print.
        if len(SMS_CODE_CHECK_1) > 0 or len(SMS_CODE_CHECK_2) > 0:
            print("SMS code entry window opened: TEST PASSED!")
        else:
            print("SMS code entry window did not open :-(")

    # Function to check that the SMS code entry window did NOT open.
    def sms_window_not_open(self):

        # Create locator variables for the check.
        SMS_CODE_CHECK_LOCATOR_1 = ("xpath", "//span[normalize-space(.)='Введите код']")
        SMS_CODE_CHECK_LOCATOR_2 = (
            "xpath",
            "//span[normalize-space(.)='Превышено количество попыток ввода']",
        )

        # Create variables to check for the presence of elements.
        SMS_CODE_CHECK_1 = driver.find_elements(*SMS_CODE_CHECK_LOCATOR_1)
        SMS_CODE_CHECK_2 = driver.find_elements(*SMS_CODE_CHECK_LOCATOR_2)

        # Check via assert.
        assert (
            len(SMS_CODE_CHECK_1) == 0 or len(SMS_CODE_CHECK_2) == 0
        ), "SMS code entry window is unexpectedly open :-("

        # Check via print.
        if len(SMS_CODE_CHECK_1) == 0 or len(SMS_CODE_CHECK_2) == 0:
            print("SMS code entry window did not open: TEST PASSED!")
        else:
            print("SMS code entry window is unexpectedly open :-(")
