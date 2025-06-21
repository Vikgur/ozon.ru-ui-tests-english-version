import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
import os


@allure.description(
    "Expected result: an HTML file of the current page is saved in a separate directory."
)
@allure.tag("Main Page")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test Cases for Ozon")
@allure.testcase("Ozon-7", name="Getting page attributes")
def test_get_attributes():
    # Navigate to the main page.
    driver.get("https://www.ozon.ru/")
    time.sleep(5)

    # Create a variable to store the current URL.
    url = driver.current_url

    # Print the current page URL.
    print("Current page URL:", url)

    # Create a variable to get the page title.
    current_title = driver.title

    # Assert the current page title is correct.
    assert (
        current_title == "OZON маркетплейс – миллионы товаров по выгодным ценам"
    ), "Title mismatch, incorrect page title :-("

    # Print the current page title.
    print("Current page title:", current_title)

    # Create a variable to store the page's HTML source.
    current_page_source = driver.page_source

    # Save the HTML source to the page_source directory.
    with open(
        os.getcwd() + "/Tests/page_source/page_source.html", "w", encoding="utf-8"
    ) as f:
        f.write(driver.page_source)

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
