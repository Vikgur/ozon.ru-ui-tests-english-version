# Import driver options and open the authorization window.
from tests.authorisation.test_auth_window_imports_options import *
from page_elements.AuthorisationPage import AuthorisationPage
from page_elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)
from tests.authorisation.test_email_window_check import email_window_check


@allure.description(
    "Expected result: after clicking the 'Back to main screen' button, the user is returned one step back to the authorization window."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.6.1", name="Testing the 'Back to main screen' button")
def test_email_back():
    # Open the "Sign in by email" window.
    email_window_check()

    # Create an object for the "Sign in by email" window
    # from the MainPageAuthorisationEmailWindow class.
    email_window = MainPageAuthorisationEmailWindow(driver)

    # Click the "Back to main screen" button.
    wait.until(
        EC.element_to_be_clickable(email_window.BACK_TO_AUTHORISATION_WINDOW)
    ).click()
    time.sleep(2)

    # After navigating back to the authorization screen,
    # create an object from the AuthorisationPage class.
    authorisation_page = AuthorisationPage(driver)

    # Check with assert that the return to the authorization screen occurred.
    assert (
        authorisation_page.VISIBILITY_TEXT_PHONE.text == "Введите номер телефона"
    ), 'Return to the "Enter phone number" screen did not occur :-('

    # Print check for the return to the authorization screen.
    if authorisation_page.VISIBILITY_TEXT_PHONE.text == "Введите номер телефона":
        print('Successfully returned to the "Enter phone number" screen!')
    else:
        print('Failed to return to the "Enter phone number" screen :-(')

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
