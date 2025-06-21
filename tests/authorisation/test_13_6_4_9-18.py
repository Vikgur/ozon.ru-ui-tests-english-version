# Import driver options, open the authorization window,
# open the "Sign in via email" window.
from tests.authorisation.test_auth_window_imports_options import *
from page_elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)
from tests.authorisation.test_email_window_check import email_window_check
from tests.authorisation import email_window_asserts


@allure.description(
    "Tests: 13.6.4.9 to 13.6.4.18"
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
# Create a function to click the "Sign in" button and check for the "Invalid email format" error.
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
    window.error_check_incorrect_format()


def test_from_9_till_18():
    # Open the "Sign in via email" window.
    email_window_check()

    # Create an object of the "Sign in via email" window
    # from the MainPageAuthorisationEmailWindow class.
    email_window = MainPageAuthorisationEmailWindow(driver)

    # TEST 13.6.4.9
    # Click the input field and enter data.
    (action.click(email_window.INPUT_FIELD).pause(1).send_keys("w w@w.ww").perform())
    time.sleep(1)

    # Click "Sign in" and check for the error.
    click_and_check()

    print("TEST 13.6.4.9 PASSED SUCCESSFULLY!")

    # TEST 13.6.4.10
    # Enter data.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("ж@w.ww")
        .perform()
    )
    time.sleep(1)

    # Click "Sign in" and check for the error.
    click_and_check()

    print("TEST 13.6.4.10 PASSED SUCCESSFULLY!")

    # TEST 13.6.4.11
    # Enter data.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("w_-1@www")
        .perform()
    )
    time.sleep(1)

    # Click "Sign in" and check for the error.
    click_and_check()

    print("TEST 13.6.4.11 PASSED SUCCESSFULLY!")

    # TEST 13.6.4.12
    # Enter data.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("w_-1w.ww")
        .perform()
    )
    time.sleep(1)

    # Click "Sign in" and check for the error.
    click_and_check()

    print("TEST 13.6.4.12 PASSED SUCCESSFULLY!")

    # TEST 13.6.4.13
    # Enter data.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("w")
        .perform()
    )
    time.sleep(1)

    # Click "Sign in" and check for the error.
    click_and_check()

    print("TEST 13.6.4.13 PASSED SUCCESSFULLY!")

    # TEST 13.6.4.14
    # Enter data.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("w/w@w.ww")
        .perform()
    )
    time.sleep(1)

    # Click "Sign in" and check for the error.
    click_and_check()

    print("TEST 13.6.4.14 PASSED SUCCESSFULLY!")

    # TEST 13.6.4.15
    # Enter data.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("<div>")
        .perform()
    )
    time.sleep(1)

    # Click "Sign in" and check for the error.
    click_and_check()

    print("TEST 13.6.4.15 PASSED SUCCESSFULLY!")

    # TEST 13.6.4.16
    # Enter data.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("'); SELECT * FROM users; )")
        .perform()
    )
    time.sleep(1)

    # Click "Sign in" and check for the error.
    click_and_check()

    print("TEST 13.6.4.16 PASSED SUCCESSFULLY!")

    # TEST 13.6.4.17
    # Enter data.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("<script>alert('xss');</script>")
        .perform()
    )
    time.sleep(1)

    # Click "Sign in" and check for the error.
    click_and_check()

    print("TEST 13.6.4.17 PASSED SUCCESSFULLY!")

    # TEST 13.6.4.18
    # Enter data.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("123.123.123.123")
        .perform()
    )
    time.sleep(1)

    # Click "Sign in" and check for the error.
    click_and_check()

    print("TEST 13.6.4.18 PASSED SUCCESSFULLY!")

    driver.quit()
