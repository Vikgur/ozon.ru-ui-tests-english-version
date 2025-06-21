# Import driver options, open the authorization window,
# open the "Sign in via email" window.
from tests.authorisation.test_auth_window_imports_options import *


class TestEmailWindow:

    # Create a function to check for the error:
    # "We can't find an account with this email. Try entering a different one or sign in with a phone number."
    def error_check_empty_account(self):
        # Create a locator variable for the error.
        TEXT_error_check_LOCATOR = (
            "xpath",
            "//div[normalize-space(.)='Не можем найти аккаунт с этой почтой. Попробуйте ввести другую или войти по номеру телефона.']",
        )

        # Create an element variable for the error.
        TEXT_error_check = driver.find_element(*TEXT_error_check_LOCATOR)

        # Check via assert that the error occurred.
        assert (
            TEXT_error_check.text
            == "Не можем найти аккаунт с этой почтой. Попробуйте ввести другую или войти по номеру телефона."
        ), "Error did not appear :-("

        # Print check that the error occurred.
        if (
            TEXT_error_check.text
            == "Не можем найти аккаунт с этой почтой. Попробуйте ввести другую или войти по номеру телефона."
        ):
            print("Error appeared!")
        else:
            print("Error did not appear :-(")

    # Create a function to check for the error "Please fill in your email."
    def error_check_fill_email(self):
        # Create a locator variable for the error.
        TEXT_ERROR_NOT_EXIST_LOCATOR = (
            "xpath",
            "//div[normalize-space(.)='Заполните почту']",
        )

        # Create an element variable for the error.
        TEXT_ERROR_NOT_EXIST = driver.find_element(*TEXT_ERROR_NOT_EXIST_LOCATOR)

        # Check via assert that the error occurred.
        assert TEXT_ERROR_NOT_EXIST.text == "Заполните почту", "Error did not appear :-("

        # Print check that the error occurred.
        if TEXT_ERROR_NOT_EXIST.text == "Заполните почту":
            print("Error appeared!")
        else:
            print("Error did not appear :-(")

    # Create a function to check for the error "Invalid email format."
    def error_check_incorrect_format(self):
        # Create a locator variable for the error.
        TEXT_ERROR_NOT_EXIST_LOCATOR = (
            "xpath",
            "//div[normalize-space(.)='Некорректный формат почты']",
        )

        # Create an element variable for the error.
        TEXT_ERROR_NOT_EXIST = driver.find_element(*TEXT_ERROR_NOT_EXIST_LOCATOR)

        # Check via assert that the error occurred.
        assert (
            TEXT_ERROR_NOT_EXIST.text == "Некорректный формат почты"
        ), "Error did not appear :-("

        # Print check that the error occurred.
        if TEXT_ERROR_NOT_EXIST.text == "Некорректный формат почты":
            print("Error appeared!")
        else:
            print("Error did not appear :-(")
