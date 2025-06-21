import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from page_elements.CartPageProducts import CartPageTwoProducts
from main_detail_cart import MainDetailCart


@allure.description(
    "Expected result: The total price with Ozon Card for all units of Product 1 plus the total price for all units of Product 2 must equal the total price in the cart with Ozon Card."
)
@allure.tag("Main Page", "Detail Page", "Cart Page")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test Cases for Ozon")
@allure.testcase(
    "Ozon-3",
    name="Check cart total calculation with Ozon Card"
)
def test_cart_calculator():
    # Create an object for adding 2 products to the cart from the main page.
    main_detail_cart = MainDetailCart()

    # Add 2 products to the cart from the main page.
    main_detail_cart.two_products()

    # After switching to the third tab,
    # create a CartPage object.
    cart_page = CartPageTwoProducts(driver)

    # Create a variable for calculating the total price
    # with Ozon Card for all units of the first product.
    sum_price_product_1 = int(
        "".join(i for i in cart_page.CART_PRODUCT_1_PRICE.text if i.isdigit())
    )

    # Create a variable for calculating the total price
    # with Ozon Card for all units of the second product.
    sum_price_product_2 = int(
        "".join(i for i in cart_page.CART_PRODUCT_2_PRICE.text if i.isdigit())
    )

    # Create a variable for the total price
    # with Ozon Card for all products in the cart.
    total_price_in_cart = int(
        "".join(i for i in cart_page.CART_TOTAL_PRICE.text if i.isdigit())
    )

    # Assert that the sum of both product prices equals the total cart price.
    assert (
        sum_price_product_1 + sum_price_product_2 == total_price_in_cart
    ), "Total amount was calculated incorrectly"

    # Print result for verification.
    if sum_price_product_1 + sum_price_product_2 == total_price_in_cart:
        print(
            f"The sum of the products equals the cart total = {total_price_in_cart} RUB"
        )
        print("TEST PASSED SUCCESSFULLY!")
    else:
        print("The amounts do not match :-(")

    driver.quit()
