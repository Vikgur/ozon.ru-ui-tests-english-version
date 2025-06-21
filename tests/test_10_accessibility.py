import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from scrolls import Scrolls
from page_elements.MainPageBottom import MainPageBottom
from page_elements.Allerts import Allerts
from locators.locators import AccessibilityPageLocators


@allure.description(
    "Expected result: after clicking the 'Accessibility version' button, the user is redirected to the accessibility page."
)
@allure.tag("Main Page", "Accessibility Page")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test Cases for Ozon")
@allure.testcase("Ozon-10", name="Accessibility testing")
def test_accessebility():
    # Create an ActionChains object.
    action = ActionChains(driver)

    # Create a Scrolls object.
    scrolls = Scrolls(driver, action)

    # Open the main page.
    driver.get("https://www.ozon.ru/")
    time.sleep(5)

    # Create an AllertsPage object to handle cookie pop-ups.
    allerts = Allerts(driver)

    # Dismiss the cookie alert.
    wait.until(EC.element_to_be_clickable(allerts.ACCEPT_ALLERT_COOKIE)).click()
    time.sleep(2)

    # Scroll to the very bottom of the page (footer).
    scrolls.scroll_to_bottom()
    time.sleep(2)

    # Scroll again in case the page didn't fully load the first time.
    scrolls.scroll_to_bottom()
    time.sleep(2)

    # Create a MainPageBottom object for interacting with the footer.
    main_page_bottom = MainPageBottom(driver)

    # Click the "Accessibility version" button.
    wait.until(EC.element_to_be_clickable(main_page_bottom.MAIN_ACCESSIBILITY)).click()
    time.sleep(3)

    # Create a variable to check for the presence of font options
    # on the accessibility page.
    VISIBILITY_FONT_OPTIONS = driver.find_elements(
        *AccessibilityPageLocators.VISIBILITY_FONT_CHANGE_OPTIONS_LOCATOR
    )

    # Assert that the accessibility page opened.
    assert (
        len(VISIBILITY_FONT_OPTIONS) > 0
    ), "Accessibility page did not open :-("

    # Print result of the accessibility page check.
    if len(VISIBILITY_FONT_OPTIONS) > 0:
        print("Accessibility page opened! TEST COMPLETED SUCCESSFULLY!")
    else:
        print("Accessibility page did not open :-(")

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
