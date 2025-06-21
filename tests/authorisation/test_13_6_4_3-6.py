# Import driver options, open the authorization window,
# open the "Sign in via email" window.
from tests.authorisation.test_auth_window_imports_options import *
from page_elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)
from tests.authorisation.test_email_window_check import email_window_check
from tests.authorisation import email_window_asserts


@allure.description("Tests: 13.6.4.3, 13.6.4.4, 13.6.4.5, 13.6.4.6")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
# Create a function that clicks the "Sign in" button and checks for the error
# "We can't find an account with this email. Try entering another or sign in by phone number."
def click_and_check():
    # Create an object of the EmailWindow class.
    window = email_window_asserts.TestEmailWindow()

    # Create an object of the "Sign in via email" window
    # from the MainPageAuthorisationEmailWindow class.
    email_window = MainPageAuthorisationEmailWindow(driver)

    # Click the "Sign in" button.
    wait.until(EC.element_to_be_clickable(email_window.LOGIN_BUTTON)).click()
    time.sleep(3)

    # Check for the appearance of the error message.
    window.error_check_empty_account()


@allure.description("Tests: 13.6.4.3, 13.6.4.4, 13.6.4.5, 13.6.4.6")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
def test_from_3_till_6():

    # Open the "Sign in via email" window.
    email_window_check()

    # Create an object of the "Sign in via email" window
    # from the MainPageAuthorisationEmailWindow class.
    email_window = MainPageAuthorisationEmailWindow(driver)

    # TEST 13.6.4.3
    # Click the input field and enter data.
    (action.click(email_window.INPUT_FIELD).pause(1).send_keys("w_-1@w.ww").perform())
    time.sleep(1)

    # Click "Sign in" and check for the error.
    click_and_check()

    print("TEST 13.6.4.3 PASSED SUCCESSFULLY!")

    # TEST 13.6.4.4
    # Enter data.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("W_-1@W.WW")
        .perform()
    )
    time.sleep(1)

    # Click "Sign in" and check for the error.
    click_and_check()

    print("TEST 13.6.4.4 PASSED SUCCESSFULLY!")

    # TEST 13.6.4.5
    # Enter data.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys(" ww@w.ww")
        .perform()
    )
    time.sleep(1)

    # Click "Sign in" and check for the error.
    click_and_check()

    print("TEST 13.6.4.5 PASSED SUCCESSFULLY!")

    # TEST 13.6.4.6
    # Enter data.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("ww@w.ww ")
        .perform()
    )
    time.sleep(1)

    # Click "Sign in" and check for the error.
    click_and_check()

    print("TEST 13.6.4.6 PASSED SUCCESSFULLY!")

    driver.quit()
