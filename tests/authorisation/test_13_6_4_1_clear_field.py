# Import driver options, open the authorization window,
# and open the "Sign in by email" window.
from tests.authorisation.test_auth_window_imports_options import *
from page_elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)
from tests.authorisation.test_email_window_check import email_window_check


@allure.description(
    "Expected result: after entering any number of characters in the email input field and clicking the clear field 'x' button, all characters are removed from the field."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase(
    "Ozon-13.6.4.1", name="Testing the 'x' clear email input button"
)
def test_clear_field():
    # Open the "Sign in by email" window.
    email_window_check()

    # Create an object of the "Sign in by email" window class.
    email_window = MainPageAuthorisationEmailWindow(driver)

    # Click on the input field and enter text.
    (
        action.click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("йцукен23456789")
        .perform()
    )
    time.sleep(2)

    # Create a locator variable for the clear field 'x' button.
    CLEAR_FIELD_LOCATOR = ("xpath", "//div[@class='f019-b a2019-a']")

    # Create an element variable for the clear field 'x' button.
    CLEAR_FIELD = driver.find_element(*CLEAR_FIELD_LOCATOR)

    # Click on the clear field 'x' button.
    wait.until(EC.element_to_be_clickable(CLEAR_FIELD)).click()
    time.sleep(2)

    # Assert that the input field is empty.
    assert (
        len(driver.find_elements(*CLEAR_FIELD_LOCATOR)) == 0
    ), "The input field is not empty :-("

    # Print result for debugging.
    if len(driver.find_elements(*CLEAR_FIELD_LOCATOR)) == 0:
        print("The input field was cleared!")
    else:
        print("The input field is not empty :-(")

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
