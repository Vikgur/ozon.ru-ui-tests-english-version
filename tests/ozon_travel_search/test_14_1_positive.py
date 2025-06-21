import sys

sys.path.append(sys.path[0] + "/../..")
from imports_options import *
from page_elements.OzonTravel import OzonTravel
from tests.ozon_travel_search.test_filling_ticket_all_fields import (
    filling_ticket_all_fields,
)


@allure.description("Expected result: the search will start and results will be displayed.")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-14.1", name="Positive test")
def test_positive():
    # Fill in all fields.
    filling_ticket_all_fields()

    # Create an instance of the ActionChains class.
    action = ActionChains(driver)

    # After starting the driver, create an object
    # of the OzonTravel page class.
    ozon_page = OzonTravel(driver)

    # Click the "Find tickets" button.
    action.click(ozon_page.FIND_TICKETS_BUTTON).perform()
    time.sleep(1)
    action.click(ozon_page.FIND_TICKETS_BUTTON).perform()
    time.sleep(5)

    # Switch driver to the second tab with the product.
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # Create variables for the locator and element of the "Show price chart" button
    # on the opened search results page.
    SHOW_PRICE_CHART_LOCATOR = (
        "xpath",
        "//div[normalize-space(.)='Показать график цен']",
    )
    SHOW_PRICE_CHART = driver.find_element(*SHOW_PRICE_CHART_LOCATOR)

    # Assert that the search results page has opened.
    assert (
        SHOW_PRICE_CHART.text == "Показать график цен"
    ), "Search results page did not open :-("

    # Print that the search results page has opened.
    if SHOW_PRICE_CHART.text == "Показать график цен":
        print("Search results page opened!")
    else:
        print("Search results page did not open :-(")

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
