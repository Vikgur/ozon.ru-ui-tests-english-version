# Import driver options, open the authorization window,
# and open the "Sign in via email" window.
import os
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation.test_email_window_check import email_window_check


@allure.description(
    "Expected result: the HTML code of the authorization page is downloaded to a separate directory for checking the presence of comments and hidden input fields."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.6.4.19", name="Download page HTML")
def test_html():
    # Open the "Sign in via email" window.
    email_window_check()

    # Create a variable to hold the current page URL.
    url = driver.current_url

    # Check via print that the page opened correctly.
    print("Current page URL:", url)

    # Create a variable to get the title of the current page.
    current_title = driver.title

    # Check via assert the title of the current page.
    assert (
        current_title == "OZON"
        or current_title == "OZON marketplace – millions of goods at great prices"
    ), "Title error: incorrect page title :-("

    # Check via print the title of the current page.
    print("Current page title:", current_title)

    # Create a variable to get the HTML code of the current page.
    current_page_source = driver.page_source

    # Save the HTML code of the current page to the page_source folder.
    with open(
        os.getcwd() + "/Tests/authorisation/auth_page_source/page_source.html",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(driver.page_source)

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
