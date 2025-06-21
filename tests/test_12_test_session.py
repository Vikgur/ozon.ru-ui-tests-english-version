# Сомневающийся покупатель.

import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from scrolls import Scrolls
from page_elements.MainPage import MainPage
from page_elements.DetailPage import DetailPageProduct
from page_elements.CatalogPageCleaner import CatalogPageCleaner
from page_elements.CartPageProducts import CartPageOneProduct, CartPageDeleteConfirm
from locators.locators import CatalogPageCleanerLocators
from authorisation_page_check import authorisation_page_check


@allure.description(
    "Expected result: the product is successfully added to the cart, and upon attempting to proceed to checkout, the user is redirected to the authorization page."
)
@allure.tag(
    "Main Page",
    "Catalog Page",
    "Product Detail Page",
    "Cart Page",
    "Authorization Page",
)
@allure.severity(allure.severity_level.BLOCKER)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test Cases for Ozon")
@allure.issue("Ozon-bag-tracker-666", name="Authorization page does not open")
@allure.testcase("Ozon-12", name="Test session based on 'uncertain buyer' tour")
def test_session():
    # Create an ActionChains object.
    action = ActionChains(driver)

    # Create a Scrolls object.
    scrolls = Scrolls(driver, action)

    # Navigate to the main page.
    driver.get("https://www.ozon.ru/")
    time.sleep(5)

    # Create a MainPage object.
    main_page = MainPage(driver)

    # Enter a search query and perform the search.
    wait.until(EC.element_to_be_clickable(main_page.MAIN_SEARCH)).click()
    time.sleep(1)
    main_page.MAIN_SEARCH.send_keys("пылесос")  # vacuum cleaner
    time.sleep(2)
    main_page.MAIN_SEARCH.send_keys(Keys.ENTER)
    time.sleep(2)

    # Function to add product to the cart from the catalog page.
    def add_product_to_cart():
        # Create a CatalogPageCleaner object.
        catalog_page = CatalogPageCleaner(driver)

        # Apply the filter "robot vacuum cleaner".
        wait.until(
            EC.element_to_be_clickable(catalog_page.FILTER_ROBOT_CLEANER)
        ).click()
        time.sleep(2)

        # Refresh catalog object if necessary.
        catalog_page = CatalogPageCleaner(driver)

        # Click on the first robot vacuum in the search results.
        action.click(on_element=catalog_page.ROBOT_CLEANER_FIRST_RESULT).perform()
        time.sleep(3)

        # Switch to the new tab with the product detail.
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])

        # Create a DetailPageProduct object.
        detail_page = DetailPageProduct(driver)

        # Click on "Go to description" button.
        action.click(on_element=detail_page.GO_TO_DESCRIPTION).perform()
        time.sleep(2)

        # Click on "Add to cart" button.
        action.click(on_element=detail_page.PRODUCT_ADD_TO_CART).perform()
        time.sleep(2)

        # Click on the cart icon in the top right.
        action.click(on_element=detail_page.ADD_TO_CART_ICON).perform()
        time.sleep(2)
    
    # Add the product to the cart.
    add_product_to_cart()

    # Create a CartPageOneProduct object.
    cart_page = CartPageOneProduct(driver)

    # Click the "Delete selected" button.
    wait.until(EC.element_to_be_clickable(cart_page.DELETE_ALL_SELECTED)).click()
    time.sleep(3)

    # Create a CartPageDeleteConfirm object for the confirmation modal.
    cart_page_delete_confirm = CartPageDeleteConfirm(driver)

    # Click the "Delete" button in the confirmation modal.
    wait.until(
        EC.element_to_be_clickable(cart_page_delete_confirm.DELETE_CONFIRM)
    ).click()
    time.sleep(2)

    # Create a variable to check the presence of "Cart is empty" text.
    VISIBILITY_CART_EMPTY_TEXT = driver.find_elements(
        "xpath", "//span[normalize-space(.)='Cart is empty']"
    )

    # Assert that the "Cart is empty" text is visible.
    assert (
        len(VISIBILITY_CART_EMPTY_TEXT) > 0
    ), "Empty cart page did not open :-("

    # Print confirmation of empty cart.
    if len(VISIBILITY_CART_EMPTY_TEXT) > 0:
        print("Cart is empty, the first product was removed!\nUser successfully starts a second search!")
    else:
        print("Empty cart page did not open :-(")
    time.sleep(2)

    # Go back one step in browser history.
    driver.back()
    time.sleep(2)

    # Close the current tab.
    driver.close()
    time.sleep(3)

    # Switch driver to the remaining tab.
    tabs = driver.window_handles
    driver.switch_to.window(tabs[0])

    # Create a CatalogPageCleaner object.
    catalog_page = CatalogPageCleaner(driver)

    # Scroll to the "Delivery time" filter.
    scrolls.scroll_to_center(catalog_page.FILTER_DELIVERY_TIME)
    time.sleep(2)

    # Click the "Up to 3 days" radiobutton.
    wait.until(
        EC.element_to_be_clickable(catalog_page.FILTER_DELIVERY_TIME_3_DAYS_CLICK)
    ).click()
    time.sleep(2)

    # Create a variable to check if the "Up to 3 days" radiobutton is selected.
    CONFIRM_3_DAYS_SELECTED = driver.find_element(
        *CatalogPageCleanerLocators.FILTER_DELIVERY_TIME_3_DAYS_CHECK_LOCATOR
    )

    # Assert that the "Up to 3 days" radiobutton is selected.
    assert (
        CONFIRM_3_DAYS_SELECTED.is_selected()
    ), 'Radiobutton "Up to 3 days" is not selected :-('

    # Print result for selected "Up to 3 days" radiobutton.
    if CONFIRM_3_DAYS_SELECTED.is_selected():
        print("Filter 'Up to 3 days' successfully selected!")
    else:
        print("Filter 'Up to 3 days' not selected :-(")

    # Scroll to the "Brand" filter.
    scrolls.scroll_to_center(catalog_page.FILTER_BRAND)
    time.sleep(2)

    # Click on brand "Xiaomi".
    wait.until(EC.element_to_be_clickable(catalog_page.FILTER_BRAND_XIAOMI)).click()
    time.sleep(2)

    # Scroll to the "Price" filter.
    scrolls.scroll_to_center(catalog_page.FILTER_PRICE)
    time.sleep(2)

    # Double click on the "from" price input field.
    action.double_click(catalog_page.FILTER_PRICE_INPUT_FROM).perform()
    time.sleep(2)

    # Create variable to interact with the "from" price input field.
    PRICE_INPUT_FROM = driver.find_element(
        *CatalogPageCleanerLocators.FILTER_PRICE_INPUT_FROM_LOCATOR
    )

    # Clear the "from" price input field.
    PRICE_INPUT_FROM.send_keys(Keys.BACKSPACE)
    time.sleep(2)

    # Enter "30000" into the "from" price input field.
    PRICE_INPUT_FROM.send_keys("30000")
    time.sleep(2)

    # Click on the "to" price input field.
    action.click(catalog_page.FILTER_PRICE_INPUT_TO).perform()
    time.sleep(2)

    # Double click on the "to" price input field.
    action.double_click(catalog_page.FILTER_PRICE_INPUT_TO).perform()
    time.sleep(2)

    # Create variable to interact with the "to" price input field.
    PRICE_INPUT_TO = driver.find_element(
        *CatalogPageCleanerLocators.FILTER_PRICE_INPUT_TO_LOCATOR
    )

    # Clear the "to" price input field.
    PRICE_INPUT_TO.send_keys(Keys.BACKSPACE)
    time.sleep(2)

    # Enter "60000" into the "to" price input field.
    PRICE_INPUT_TO.send_keys("60000")
    time.sleep(2)
    PRICE_INPUT_TO.send_keys(Keys.ENTER)
    time.sleep(2)
    action.click(on_element=catalog_page.FILTER_PRICE).perform()
    time.sleep(2)

    # Scroll to the "Original Product" filter.
    scrolls.scroll_to_center(catalog_page.FILTER_ORIGINAL)
    time.sleep(2)

    # Click on the "Original Product".
    action.click(on_element=catalog_page.FILTER_ORIGINAL).perform()
    time.sleep(2)

    # Scroll to the "Original Product" filter again.
    scrolls.scroll_to_center(catalog_page.FILTER_ORIGINAL)
    time.sleep(2)

    # Create variable to confirm "Original Product" checkbox selection.
    CONFIRM_ORIGINAL_SELECTED = driver.find_element(
        "xpath", "//input[@class='c7014-a0 c7014-a5']"
    )

    # Assert that "Original Product" is selected.
    assert CONFIRM_ORIGINAL_SELECTED.is_selected(), '"Original Product" is not selected :-('

    # Print result for "Original Product" selection.
    if CONFIRM_ORIGINAL_SELECTED.is_selected():
        print("Filter 'Original Product' successfully selected!")
    else:
        print("Filter 'Up to 3 days' not selected :-(")

    # Scroll to the "Dust collector type" filter.
    scrolls.scroll_to_center(catalog_page.FILTER_DUST_COLLECTOR)
    time.sleep(2)

    # Click the "Container" checkbox in the "Dust collector type" filter.
    action.click(on_element=catalog_page.FILTER_DUST_COLLECTOR).perform()
    time.sleep(1)
    action.click(on_element=catalog_page.FILTER_DUST_CHECKBOX_CONTAINER).perform()
    time.sleep(2)

    # Create a variable to confirm that the "Container" checkbox is selected.
    CONFIRM_CONTAINER_SELECTED = ("xpath", "//input[@class='b4014-a0 b4014-a9']")

    # Assert that the "Container" checkbox is selected.
    assert (
        driver.find_element(*CONFIRM_CONTAINER_SELECTED).get_attribute("checked")
        == "true"
    ), '"Container" checkbox is not selected :-('

    # Print that the "Container" checkbox is selected.
    if (
        driver.find_element(*CONFIRM_CONTAINER_SELECTED).get_attribute("checked")
        == "true"
    ):
        print('"Container" checkbox is successfully selected!')
    else:
        print('"Container" checkbox is not selected :-(')

    # Click the "Aqua filter" checkbox in the "Dust collector type" filter.
    action.click(on_element=catalog_page.FILTER_DUST_COLLECTOR).perform()
    time.sleep(1)
    action.click(on_element=catalog_page.FILTER_DUST_CHECKBOX_AQUA).perform()
    time.sleep(2)

    # Create a variable to confirm that the "Aqua filter" checkbox is selected.
    CONFIRM_AQUA_SELECTED = ("xpath", "//input[@class='b4014-a0 b4014-a9']")

    # Assert that the "Aqua filter" checkbox is selected.
    assert (
        driver.find_element(*CONFIRM_AQUA_SELECTED).get_attribute("checked") == "true"
    ), '"Aqua filter" checkbox is not selected :-('

    # Print that the "Aqua filter" checkbox is selected.
    if driver.find_element(*CONFIRM_AQUA_SELECTED).get_attribute("checked") == "true":
        print('"Aqua filter" checkbox is successfully selected!')
    else:
        print('"Aqua filter" checkbox is not selected :-(')

        # Scroll to the top of the page.
    scrolls.scroll_to_top()
    time.sleep(2)

    # Click on the sorting filter.
    action.click(on_element=catalog_page.SORTED).perform()
    time.sleep(2)

    # Select "High rating" sorting option.
    HIGH_RATING = driver.find_element(
        *("xpath", "//span[normalize-space(.)='С высоким рейтингом']")
    )
    action.click(on_element=HIGH_RATING).perform()
    time.sleep(3)

    # Create a variable to verify that "High rating" sorting is selected.
    CONFIRM_HIGH_RATING = driver.find_elements(
        *("xpath", "//input[@title='С высоким рейтингом']")
    )

    # Assert that "High rating" sorting is selected.
    assert (
        len(CONFIRM_HIGH_RATING) > 0
    ), '"High rating" sorting was not selected :-('

    # Print that "High rating" sorting is selected.
    if len(CONFIRM_HIGH_RATING) > 0:
        print('"High rating" sorting successfully selected!')
    else:
        print('"High rating" sorting was not selected :-(')

    time.sleep(2)

    # Create variables to check if all filters have been applied.
    CONFIRM_DELIVERY = driver.find_elements(
        *("xpath", "//span[normalize-space(.)='Сроки доставки: До 3 дней']")
    )
    CONFIRM_BRAND = driver.find_elements(
        *("xpath", "//span[normalize-space(.)='Бренд: Xiaomi']")
    )
    CONFIRM_PRICE = driver.find_elements(
        *("xpath", "//span[normalize-space(.)='Цена: от 30 000 до 60 000']")
    )
    CONFIRM_ORIGINAL = driver.find_elements(
        *("xpath", "//span[normalize-space(.)='Оригинальный товар']")
    )
    CONFIRM_DUST_CONTAINER = driver.find_elements(
        *("xpath", "//span[normalize-space(.)='Вид пылесборника: Контейнер']")
    )
    CONFIRM_DUST_AQUA = driver.find_elements(
        *("xpath", "//span[normalize-space(.)='Вид пылесборника: Аквафильтр']")
    )

    # Assert that all selected filters are applied.
    assert (
        len(CONFIRM_DELIVERY) > 0
        and len(CONFIRM_BRAND) > 0
        and len(CONFIRM_PRICE) > 0
        and len(CONFIRM_ORIGINAL) > 0
        and len(CONFIRM_DUST_CONTAINER) > 0
        and len(CONFIRM_DUST_AQUA) > 0
    ), "Some filters were not applied :-("

    # Print that all selected filters are applied.
    if (
        len(CONFIRM_DELIVERY) > 0
        and len(CONFIRM_BRAND) > 0
        and len(CONFIRM_PRICE) > 0
        and len(CONFIRM_ORIGINAL) > 0
        and len(CONFIRM_DUST_CONTAINER) > 0
        and len(CONFIRM_DUST_AQUA) > 0
    ):
        print("All filters successfully applied!")
    else:
        print("Some filters were not applied :-(")

    time.sleep(1)

    # Add product to the cart.
    add_product_to_cart()

    # Create cart page object from DetailPage class.
    cart_page = CartPageOneProduct(driver)

    # Click the "Proceed to checkout" button.
    action.click(on_element=cart_page.CLICK_TO_BUY).perform()
    time.sleep(2)

    # Check redirect to authorization page.
    authorisation_page_check()

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
