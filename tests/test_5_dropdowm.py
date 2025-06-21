import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from page_elements.MainPageAuthorisationIcon import MainPageAuthorisationIcon
from page_elements.Allerts import Allerts
from locators.locators import MainPageFaceIconLocators


@allure.description(
    "Expected result: when hovering over the 'profile' icon, a dropdown menu should appear with the buttons: 'Log in or Register' and 'Personal Account'. Clicking 'Log in or Register' opens a non-blocking modal window on the same page. Clicking 'Personal Account' opens the personal account page."
)
@allure.tag("Main Page")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test Cases for Ozon")
@allure.testcase("Ozon-5", name="Testing dropdown element list")
def test_dropdown():
    # Create an ActionChains object.
    action = ActionChains(driver)

    # Navigate to the main page.
    driver.get("https://www.ozon.ru/")
    time.sleep(5)

    # After launching the driver and opening the main page,
    # create an AllertsPage object to handle cookie alerts.
    allerts = Allerts(driver)

    # Dismiss the cookie notification.
    wait.until(EC.element_to_be_clickable(allerts.ACCEPT_ALLERT_COOKIE)).click()
    time.sleep(3)

    # After accepting cookies, create a MainPageAuthorisationIcon object.
    main_page = MainPageAuthorisationIcon(driver)

    # Hover over the "profile" icon in the header.
    action.move_to_element(main_page.MAIN_FACE_ICON).perform()
    time.sleep(2)

    # Create a variable for the "Log in or Register" button
    # to check if it is present in the dropdown menu.
    VISIBILITY_SIGN_IN_BUTTON = driver.find_elements(
        *MainPageFaceIconLocators.MAIN_FACE_ICON_SIGN_IN_LOCATOR
    )

    # Assert that the "Log in or Register" button is visible in the dropdown.
    assert len(VISIBILITY_SIGN_IN_BUTTON) > 0, "Dropdown menu did not appear :-("

    # Print the result of the dropdown visibility check.
    if len(VISIBILITY_SIGN_IN_BUTTON) > 0:
        print("Dropdown appeared: TEST PASSED SUCCESSFULLY")
    else:
        print("Dropdown did not appear :-(")

    driver.quit()
