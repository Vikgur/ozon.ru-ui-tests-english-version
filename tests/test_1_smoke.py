import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from scrolls import Scrolls
from page_elements.MainPage import MainPage
from page_elements.DetailPage import DetailPageBuyOneClick
from authorisation_page_check import authorisation_page_check


@allure.description(
    "Expected result: the product is successfully added to the cart, but when trying to proceed to checkout, the user is redirected to the authorization page."
)
@allure.tag("Main Page", "Detail Page", "Authorization Page")
@allure.severity(allure.severity_level.BLOCKER)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test Cases for Ozon")
@allure.issue("Ozon-bag-tracker-666", name="Authorization page does not open")
@allure.testcase(
    "Ozon-1", name="Smoke Test — Verifying Main Functionality"
)
def test_smoke():
    # Create an ActionChains object.
    action = ActionChains(driver)

    # Create a Scrolls object.
    scrolls = Scrolls(driver, action)

    # Navigate to the main page.
    driver.get("https://www.ozon.ru/")
    time.sleep(5)

    # After launching the driver and opening the main page,
    # create a MainPage object.
    main_page = MainPage(driver)

    # Scroll to the nearest product with a name for clicking.
    scrolls.scroll_to_center(main_page.MAIN_PRODUCT_1)
    time.sleep(2)

    # Click on the first product in the "Hot Deals" section.
    # A new tab opens with the first product.
    wait.until(EC.element_to_be_clickable(main_page.MAIN_PRODUCT_1)).click()
    time.sleep(2)

    # Switch the driver to the second tab with the product.
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # After switching to the second tab,
    # create a DetailPage object for "Buy in One Click".
    detail_page = DetailPageBuyOneClick(driver)

    # On the second tab, click the "Buy in One Click" button.
    # This navigates to the authorization page in the same window.
    action.click(on_element=detail_page.BUY_1_CLICK).perform()
    time.sleep(3)

    # Verify the navigation to the authorization page.
    authorisation_page_check()

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
