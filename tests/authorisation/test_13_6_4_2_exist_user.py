# Import driver options and open the authorization window,
# open the "Sign in by email" window.
from tests.authorisation.test_auth_window_imports_options import *
from page_elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)
from tests.authorisation.test_email_window_check import email_window_check


@allure.description(
    "Expected result: after entering a valid email of a registered user in the input field and clicking the 'Sign in' button, the 'Enter code' window for SMS code appears."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.6.4.2", name="Enter a valid email of a registered user")
def test_exist_user():
    # Open the "Sign in by email" window.
    email_window_check()

    # Create an object of the "Sign in by email" window class.
    email_window = MainPageAuthorisationEmailWindow(driver)

    # Click the input field and enter data.
    (
        action.click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("registered_on_ozon_email@gmail.com")
        .perform()
    )
    time.sleep(2)

    # Click the "Sign in" button.
    wait.until(EC.element_to_be_clickable(email_window.LOGIN_BUTTON)).click()
    time.sleep(3)

    # BLOCK for checking the transition to the "Enter code" window.
    # If the SMS code entry window opened.
    try:
        # Create locator variables for the "Enter code" window.
        TEXT_ENTER_CODE_LOCATOR = ("xpath", "//span[normalize-space(.)='Введите код']")

        # Create the element variable for the "Enter code" window.
        TEXT_ENTER_CODE = driver.find_element(*TEXT_ENTER_CODE_LOCATOR)

        # Assert that the "Enter code" window opened.
        assert (
            TEXT_ENTER_CODE.text == "Введите последние 6 цифр входящего номера"
        ), 'Transition to the "Enter code" window did not occur :-('

        # Print the result for debugging.
        if TEXT_ENTER_CODE.text == "Введите последние 6 цифр входящего номера":
            print('Transition to the "Enter code" window succeeded!')
        else:
            print('Transition to the "Enter code" window did not occur :-(')

    # If a push was sent or the attempt limit was exceeded.
    except:
        # Push notification was sent.
        try:
            # Create a locator variable for the "Enter code from push" window.
            TEXT_ENTER_PUSH_CODE_LOCATOR = (
                "xpath",
                "//span[normalize-space(.)='Enter the code from the push notification']",
            )

            # Create an element variable for the "Enter code from push" window.
            TEXT_ENTER_PUSH_CODE = driver.find_element(*TEXT_ENTER_PUSH_CODE_LOCATOR)

            # Assert that the "Enter code" window opened.
            assert (
                TEXT_ENTER_PUSH_CODE.text == "Enter the code from the push notification"
            ), 'Transition to the "Enter code" window did not occur :-('

            # Print verification for the push code window.
            if TEXT_ENTER_PUSH_CODE.text == "Enter the code from the push notification":
                print('Transition to the "Enter code" window succeeded!')
            else:
                print('Transition to the "Enter code" window did not occur :-(')
        # Input attempt limit exceeded.
        except:
            # Create a locator variable for the "Too many attempts" message.
            TEXT_TRY_LIMIT_LOCATOR = (
                "xpath",
                "//span[normalize-space(.)='Too many attempts']",
            )

            # Create an element variable for the "Too many attempts" message.
            TEXT_TRY_LIMIT = driver.find_element(*TEXT_TRY_LIMIT_LOCATOR)

            # Assert that the attempt limit window appeared.
            assert (
                TEXT_TRY_LIMIT.text == "Too many attempts"
            ), 'Transition to the "Enter code" window did not occur :-('

            # Print verification for the attempt limit message.
            if TEXT_TRY_LIMIT.text == "Too many attempts":
                print('Transition to the "Enter code" window succeeded!')
            else:
                print('Transition to the "Enter code" window did not occur :-(')

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
