import sys

sys.path.append(sys.path[0] + "/..")
import os
import pickle
from imports_options import *
from page_elements.CartPageProducts import CartPageTwoProducts
from locators.locators import CartPageTwoProductLocators
from main_detail_cart import MainDetailCart


@allure.description(
    "Expected result: after adding two different items to the cart and deleting cookies, the cart becomes empty. After restoring the deleted cookies, the same items in the same quantities return to the cart."
)
@allure.tag("Main Page", "Detail Page", "Cart Page")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test Cases for Ozon")
@allure.testcase("Ozon-6", name="Testing cookie behavior")
def test_cookies():
    # Create an object to add 2 products to the cart from the main page.
    main_detail_cart = MainDetailCart()

    # Add 2 products to the cart from the main page.
    main_detail_cart.two_products()

    # After switching to the third tab,
    # create a CartPage object.
    cart_page = CartPageTwoProducts(driver)

    # Assert that the current page is the cart page.
    assert driver.title == "OZON.ru - Моя корзина", "Wrong page opened :-("

    # Save all cookies from the cart page to cookies.pkl file in test_cookies directory.
    pickle.dump(
        driver.get_cookies(),
        open(os.getcwd() + "/Tests/test_cookies/cookies.pkl", "wb"),
    )

    # Delete all cookies.
    driver.delete_all_cookies()

    # Refresh the page.
    driver.refresh()

    # Delete cookies again in case they were not removed the first time.
    driver.delete_all_cookies()

    # Refresh the page again.
    driver.refresh()

    # Create variables to check the presence of product prices on the page.
    VISIBILITY_PRODUCT_PRICE_1 = driver.find_elements(
        *CartPageTwoProductLocators.CART_PRODUCT_1_PRICE_LOCATOR
    )
    VISIBILITY_PRODUCT_PRICE_2 = driver.find_elements(
        *CartPageTwoProductLocators.CART_PRODUCT_2_PRICE_LOCATOR
    )

        # Assert that product prices are not visible (cart is empty).
    assert len(VISIBILITY_PRODUCT_PRICE_1) == 0, "Product 1 was not removed :-("
    assert len(VISIBILITY_PRODUCT_PRICE_2) == 0, "Product 2 was not removed :-("

    # Print visibility check result.
    if len(VISIBILITY_PRODUCT_PRICE_1) > 0 and len(VISIBILITY_PRODUCT_PRICE_2) > 0:
        print("Products are still in the cart :-(")
    else:
        print("Cart is empty: COOKIES SUCCESSFULLY DELETED!")

    time.sleep(3)

    # Restore the session in the cart with previously added products
    # that were removed by clearing cookies.
    cookies = pickle.load(open(os.getcwd() + "/Tests/test_cookies/cookies.pkl", "rb"))

    for cookie in cookies:
        driver.add_cookie(cookie)

    # Refresh the page after restoring cookies.
    driver.refresh()
    time.sleep(3)

    # Create variables to check if product prices are visible again.
    VISIBILITY_PRODUCT_PRICE_1_RESTORED = driver.find_elements(
        *CartPageTwoProductLocators.CART_PRODUCT_1_PRICE_LOCATOR
    )
    VISIBILITY_PRODUCT_PRICE_2_RESTORED = driver.find_elements(
        *CartPageTwoProductLocators.CART_PRODUCT_2_PRICE_LOCATOR
    )

    # Assert that product prices are visible (cart restored).
    assert len(VISIBILITY_PRODUCT_PRICE_1_RESTORED) > 0, "Product 1 was not restored :-("
    assert len(VISIBILITY_PRODUCT_PRICE_2_RESTORED) > 0, "Product 2 was not restored :-("

    # Print result of cart restoration.
    if (
        len(VISIBILITY_PRODUCT_PRICE_1_RESTORED) > 0
        and len(VISIBILITY_PRODUCT_PRICE_2_RESTORED) > 0
    ):
        print("Products are in the cart, cookies restored, TEST PASSED SUCCESSFULLY!")
    else:
        print("Cart is still empty :-(")

    driver.quit()
