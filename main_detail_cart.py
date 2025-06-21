import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from scrolls import Scrolls
from page_elements.MainPage import MainPage
from page_elements.DetailPage import DetailPageInDemand

# Test session:
# Add products from the main page to the cart,
# more than 1 unit each.

class MainDetailCart(object):

    # Add 2 products to the cart
    def two_products(self):
        # Initialize ActionChains object
        action = ActionChains(driver)

        # Initialize Scrolls object
        scrolls = Scrolls(driver, action)

        # Navigate to the main page
        driver.get("https://www.ozon.ru/")
        time.sleep(3)

        # After driver launch and opening the main page,
        # initialize MainPage object
        main_page = MainPage(driver)

        # Scroll to the nearest product with a name for clicking
        scrolls.scroll_to_center(main_page.MAIN_PRODUCT_1)
        time.sleep(1)

        # Click on the first product in the "Hot Deals" section.
        # A new tab opens with the first product.
        wait.until(EC.element_to_be_clickable(main_page.MAIN_PRODUCT_1)).click()
        time.sleep(2)

        # Click on the second product in the "Hot Deals" section.
        # A third tab opens with the second product.
        wait.until(EC.element_to_be_clickable(main_page.MAIN_PRODUCT_2)).click()
        time.sleep(1)

        # Switch the driver to the second tab with the first product.
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])

        # After switching to the second tab,
        # initialize DetailPage object
        detail_page = DetailPageInDemand(driver)

        # On the second tab, add multiple units of the product to the cart.
        wait.until(EC.element_to_be_clickable(detail_page.PRODUCT_ADD)).click()
        time.sleep(1)

        # Switch to the third tab with the second product,
        # and initialize DetailPage object again
        driver.switch_to.window(tabs[2])
        detail_page = DetailPageInDemand(driver)

        # On the third tab, add multiple units of the product to the cart.
        wait.until(EC.element_to_be_clickable(detail_page.PRODUCT_ADD)).click()
        time.sleep(1)

        # On the third tab, click the cart icon in the header
        wait.until(EC.element_to_be_clickable(detail_page.ADD_TO_CART_ICON)).click()
        time.sleep(2)
