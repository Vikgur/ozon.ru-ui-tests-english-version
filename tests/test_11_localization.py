import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from page_elements.MainPage import MainPage
from page_elements.Allerts import Allerts
from page_elements.MainPageCurrency import MainPageСurrency
from page_elements.MainPageCurrencyDropdown import MainPageСurrencyDropdown
from locators.locators import MainPageCurrencyLocators, MainPageCurrencyDropdownLocators


@allure.description(
    "Expected result: after clicking the 'RUB' button, a currency selection window opens, and selecting 'US Dollar' changes the currency."
)
@allure.tag("Main Page")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test Cases for Ozon")
@allure.testcase("Ozon-11", name="Localization testing")
def test_localization():
    # Create an ActionChains object.
    action = ActionChains(driver)

    # Open the main page.
    driver.get("https://www.ozon.ru/")
    time.sleep(5)

    # Create an AllertsPage object to handle cookie pop-ups.
    allerts = Allerts(driver)

    # Accept the cookie alert.
    wait.until(EC.element_to_be_clickable(allerts.ACCEPT_ALLERT_COOKIE)).click()
    time.sleep(5)

    # Create a MainPage object.
    main_page = MainPage(driver)

    # Click the "RUB" button in the header.
    wait.until(EC.element_to_be_clickable(main_page.MAIN_CURRENCY)).click()
    time.sleep(3)

    # Create an object for the Currency modal.
    currency_page = MainPageСurrency(driver)

    # Verify the currency modal is visible.
    VISIBILITY_CURRENCY = driver.find_elements(
        *MainPageCurrencyLocators.MAIN_CURRENCY_VISIBILITY_LOCATOR
    )

    # Assert the currency modal opened.
    assert len(VISIBILITY_CURRENCY) > 0, 'Currency modal did not open :-('

    # Print the result.
    if len(VISIBILITY_CURRENCY) > 0:
        print('Currency modal opened! TEST PASSES!')
    else:
        print('Currency modal did not open :-(')

    # Find the dropdown element.
    DROPDOWN = driver.find_element(
        *MainPageCurrencyLocators.MAIN_CURRENCY_DROPDOWN_LOCATOR
    )

    # Click the dropdown.
    wait.until(EC.element_to_be_clickable(DROPDOWN)).click()
    time.sleep(2)

    # Create an object for the currency dropdown list.
    currency_page_dropdown = MainPageСurrencyDropdown(driver)

    # Find the "USD" currency option.
    DOLLAR_USA = driver.find_element(
        *MainPageCurrencyDropdownLocators.MAIN_CURRENCY_DROPDOWN_USD_LOCATOR
    )

    # Click on "USD".
    wait.until(EC.element_to_be_clickable(DOLLAR_USA)).click()
    time.sleep(5)

    # Create a variable to confirm currency switched to USD.
    CONFIRM_USD = driver.find_element(
        "xpath", "//button[@data-widget='selectedCurrency']"
    )

    # Assert currency is switched to USD.
    assert CONFIRM_USD.text == "USD", "Currency is not USD :-("

    # Print confirmation.
    if CONFIRM_USD.text == "USD":
        print(f"Currency switched to {CONFIRM_USD.text}: TEST PASSED!")
    else:
        print("Currency is not USD :-(")

    driver.quit()
