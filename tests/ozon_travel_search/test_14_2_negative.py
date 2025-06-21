import sys

sys.path.append(sys.path[0] + "/../..")
from imports_options import *
from page_elements.OzonTravel import OzonTravel
from tests.ozon_travel_search.test_filling_ticket_all_fields import (
    filling_ticket_all_fields,
)


@allure.description(
    "Expected result: after entering all ticket purchase data and clearing the 'To' field, an error 'Fill in the field' appears and the search results page does not open."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-14.2", name="Negative test")
def test_negative():
    # Create an instance of the ActionChains class.
    action = ActionChains(driver)

    # Fill in all fields.
    filling_ticket_all_fields()

    # Create an instance of the OzonTravel page class.
    ozon_page = OzonTravel(driver)

    # Clear the "To" input field.
    action.click(ozon_page.INPUT_TO).perform()
    time.sleep(1)
    action.click(ozon_page.INPUT_TO).perform()
    time.sleep(2)

    # Click the "Find tickets" button.
    action.click(ozon_page.FIND_TICKETS_BUTTON).perform()
    time.sleep(1)
    action.click(ozon_page.FIND_TICKETS_BUTTON).perform()
    time.sleep(3)

    # Create variables for the locator and element of the "Fill in the field" error notification.
    ERROR_NOTIFICATION_LOCATOR = (
        "xpath",
        "//span[normalize-space(.)='Заполните поле']",
    )
    ERROR_NOTIFICATION = driver.find_element(*ERROR_NOTIFICATION_LOCATOR)

    # Assert that the "Fill in the field" error appears.
    assert (
        ERROR_NOTIFICATION.text == "Заполните поле"
    ), '"Fill in the field" error did not appear :-('

    # Print that the "Fill in the field" error appears.
    if ERROR_NOTIFICATION.text == "Заполните поле":
        print('"Fill in the field" error appeared!')
    else:
        print('"Fill in the field" error did not appear :-(')

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
