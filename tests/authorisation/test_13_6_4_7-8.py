# Import driver options, open the authorization window,
# open the "Sign in via email" window.
from tests.authorisation.test_auth_window_imports_options import *
from page_elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)
from tests.authorisation.test_email_window_check import email_window_check
from tests.authorisation import email_window_asserts


@allure.description("Tests: 13.6.4.7, 13.6.4.8")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
# Create a function to click the "Sign in" button and check the "Please enter email" error.
def click_and_check():
    # Create an object of the EmailWindow class.
    window = email_window_asserts.TestEmailWindow()

    # Create an object of the "Sign in via email" window
    # from the MainPageAuthorisationEmailWindow class.
    email_window = MainPageAuthorisationEmailWindow(driver)

    # Click the "Sign in" button.
    wait.until(EC.element_to_be_clickable(email_window.LOGIN_BUTTON)).click()
    time.sleep(3)

    # Check if the error occurred.
    window.error_check_fill_email()


def test_from_7_till_8():
    # Open the "Sign in via email" window.
    email_window_check()

    # Create an object of the "Sign in via email" window
    # from the MainPageAuthorisationEmailWindow class.
    email_window = MainPageAuthorisationEmailWindow(driver)

    # TEST 13.6.4.7
    # Click the input field and enter data.
    (action.click(email_window.INPUT_FIELD).pause(1).send_keys(" ").perform())
    time.sleep(1)

    # Click "Sign in" and check the error.
    click_and_check()

    print("TEST 13.6.4.7 PASSED SUCCESSFULLY!")

    # TEST 13.6.4.8
    # Enter data.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys(Keys.BACKSPACE)
        .pause(1)
        .send_keys("")
        .perform()
    )
    time.sleep(1)

    # Click "Sign in" and check the error.
    click_and_check()

    print("TEST 13.6.4.8 PASSED SUCCESSFULLY!")

    driver.quit()
