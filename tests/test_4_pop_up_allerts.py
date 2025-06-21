import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from page_elements.Allerts import Allerts
from locators.locators import AllertsLocators


@allure.description(
    "Expected result: the cookie notification appears and disappears after clicking the 'OK' button."
)
@allure.tag("Main Page")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test Cases for Ozon")
@allure.testcase("Ozon-4", name="Check for pop-up notifications")
def test_pop_up_allerts():
    # Navigate to the main page.
    driver.get("https://www.ozon.ru/")
    time.sleep(5)

    # After launching the driver and opening the main page,
    # create an AllertsPage object to handle alerts.
    allerts = Allerts(driver)

    # Function to check visibility of an element
    # and print the result.
    def visibility_check(button):
        try:
            if len(button) > 0:
                print("Notification appeared! TEST is in progress.")
            else:
                print("No notification found :-(")
        except:
            pass

    # Function to check invisibility of an element
    # and print the result.
    def invisibility_check(button):
        try:
            if len(button) > 0:
                print("Notification is still visible :-(")
            else:
                print("Notification disappeared! TEST PASSED SUCCESSFULLY!")
        except:
            pass

    # Create variable to check
    # for visibility of the cookie notification.
    VISIBILITY_COOKIES_BEFORE_CLICK = driver.find_elements(
        *AllertsLocators.VISIBILITY_ALLERT_COOKIE_LOCATOR
    )

    # Assert that the cookie notification appeared.
    assert (
        len(VISIBILITY_COOKIES_BEFORE_CLICK) > 0
    ), "Dropdown list/menu did not appear :-("

    # Print the notification visibility result.
    visibility_check(VISIBILITY_COOKIES_BEFORE_CLICK)

    # Close the cookie notification.
    wait.until(EC.element_to_be_clickable(allerts.ACCEPT_ALLERT_COOKIE)).click()
    time.sleep(2)

    # Create variable to check
    # if the notification is still visible after clicking.
    VISIBILITY_COOKIES_AFTER_CLICK = driver.find_elements(
        *AllertsLocators.VISIBILITY_ALLERT_COOKIE_LOCATOR
    )

    # Assert that the notification disappeared.
    assert (
        len(VISIBILITY_COOKIES_AFTER_CLICK) == 0
    ), "Dropdown list/menu did not disappear :-("

    # Print the notification invisibility result.
    invisibility_check(VISIBILITY_COOKIES_AFTER_CLICK)

    driver.quit()
