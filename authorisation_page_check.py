import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from page_elements.AuthorisationPage import AuthorisationPage


# Create a function to check if the authorization page is opened.
def authorisation_page_check():

    # Create a locator for the iframe.
    FIELD_IFRAME_LOCATOR = ("xpath", "//iframe[@id='authFrame']")

    # Switch the driver to the iframe.
    driver.switch_to.frame("authFrame")

    # After navigating to the authorization page,
    # create an object of the AuthorisationPage class.
    authorisation_page = AuthorisationPage(driver)

    # Assert that the authorization page is opened.
    assert (
        authorisation_page.VISIBILITY_TEXT_PHONE.text == "Введите номер телефона"
    ), "Authorization page was not opened :-("

    # Print result for confirmation.
    if authorisation_page.VISIBILITY_TEXT_PHONE.text == "Введите номер телефона":
        print("Authorization page opened successfully!")
    else:
        print("Authorization page not opened :-(")
