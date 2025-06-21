import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
import requests


@allure.description(
    "Expected result: the time interval between sending the request and receiving the response is obtained while the browser is running with an enabled extension."
)
@allure.tag("Main Page")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test Cases for Ozon")
@allure.testcase(
    "Ozon-9", name="Performance test with any enabled browser extension"
)
def test_extension_page_load_time():
    # Install the required extension.
    chrome_options.add_extension("Tests/Extensions/adblock.crx")

    # Create a new driver instance that opens a second browser window.
    driver = webdriver.Chrome(options=chrome_options)

    # Define the main page URL.
    url = "https://www.ozon.ru/"

    # Open the main page.
    driver.get(url)
    time.sleep(5)

    # Create a variable to store the time delta between
    # sending the request and receiving the response.
    time_delta = requests.get(url)

    # Print the result of time_delta in seconds, rounded to milliseconds.
    print(f"Result: {round(time_delta.elapsed.total_seconds(), 3)} seconds")

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
