import sys

sys.path.append(sys.path[0] + "/../..")
from imports_options import *
from page_elements.OzonTravel import OzonTravel
from page_elements.OzonTravelDates import OzonTravelDates
from page_elements.OzonTravelPassengers import OzonTravelPassengers


# Create a function to fill in all fields.
def filling_ticket_all_fields():

    # Create an instance of the ActionChains class.
    action = ActionChains(driver)

    # Pass control of the page to the driver.
    driver.get("https://www.ozon.ru/travel/")
    time.sleep(5)

    # Create an instance of the OzonTravel page class.
    ozon_page = OzonTravel(driver)

    # Clear the "From" input field.
    wait.until(EC.element_to_be_clickable(ozon_page.INPUT_FROM_CLEAR)).click()
    time.sleep(2)

    # Enter data in the "From" field.
    ozon_page.INPUT_FROM.send_keys("Vladivostok")
    time.sleep(2)

    # Click on "Vladivostok" from the dropdown list.
    VLADIVOSTOK_LOCATOR = ("xpath", "//span[normalize-space(.)='Владивосток']")
    VLADIVOSTOK = driver.find_element(*VLADIVOSTOK_LOCATOR).click()
    time.sleep(2)

    # Click on the "To" field.
    action.click(ozon_page.INPUT_TO).perform()
    time.sleep(1)
    action.click(ozon_page.INPUT_TO).perform()
    time.sleep(2)

    # Enter data in the "To" field.
    ozon_page.INPUT_TO.send_keys("Moscow")
    time.sleep(2)

    # Click on "Moscow" from the dropdown list.
    MOSCOW_LOCATOR = ("xpath", "//span[normalize-space(.)='Москва']")
    MOSCOW = driver.find_element(*MOSCOW_LOCATOR).click()
    time.sleep(2)

    # Click on the "Dates" option.
    action.click(ozon_page.INPUT_DATE).perform()
    time.sleep(1)
    action.click(ozon_page.INPUT_DATE).perform()
    time.sleep(2)

    # Create an instance of the "Dates" dropdown class OzonTravelDates.
    ozon_page_dates = OzonTravelDates(driver)

    # Select a date.
    action.click(ozon_page_dates.INPUT_DATE_DAY).perform()
    time.sleep(2)

    # Create a locator variable for the "One-way ticket only" button.
    INPUT_DATE_ONE_WAY_LOCATOR = (
        "xpath",
        "//div[normalize-space(.)='Обратный билет не нужен']",
    )

    # Create an element variable for the "One-way ticket only" button.
    INPUT_DATE_ONE_WAY = driver.find_element(*INPUT_DATE_ONE_WAY_LOCATOR)

    # Click on "One-way ticket only".
    action.click(INPUT_DATE_ONE_WAY).perform()
    time.sleep(2)

    # Dismiss the cookie notification.
    COOKIE_LOCATOR = (
        "xpath",
        "//button[normalize-space(.)='ОК']",
    )
    COOKIE = driver.find_element(*COOKIE_LOCATOR).click()
    time.sleep(2)

    # Click on the "Passengers and class" option.
    action.click(ozon_page.INPUT_PASSENGERS_CLASS).perform()
    time.sleep(2)

    # Create an instance of the "Passengers and class" dropdown class OzonTravelPassengers.
    ozon_page_passengers = OzonTravelPassengers(driver)

    # Add 1 infant passenger (under 2 years old).
    action.click(ozon_page_passengers.INPUT_PASSENGERS_NEWBORN_ADD).perform()
    time.sleep(2)

    # Select "Business" class.
    action.click(ozon_page_passengers.INPUT_PASSENGERS_CLASS_BUSINESS).perform()
    time.sleep(2)
