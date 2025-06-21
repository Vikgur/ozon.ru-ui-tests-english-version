# Import driver options and open the authorization window.
from tests.authorisation.test_auth_window_imports_options import *
from page_elements.AuthorisationPage import AuthorisationPage
from page_elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)


# Create a function to check that the "Sign in with email" window is open.
def email_window_check():

    # Click the "Sign in with email" button.
    wait.until(EC.element_to_be_clickable(authorisation_window.EMAIL_SIGN_IN)).click()
    time.sleep(2)

    # Create an object for the "Sign in with email" window
    # using the MainPageAuthorisationEmailWindow class.
    email_window = MainPageAuthorisationEmailWindow(driver)

    # Check via assert that the "Sign in with email" window is opened.
    assert (
        email_window.EMAIL_WINDOW.text == "Войдите по почте"
    ), 'Transition to the "Sign in with email" window failed :-('

    # Check via print that the "Sign in with email" window is opened.
    if email_window.EMAIL_WINDOW.text == "Войдите по почте":
        print('"Sign in with email" window is open!')
    else:
        print('"Sign in with email" window is not open :-(')
