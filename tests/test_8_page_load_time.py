import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
import requests


@allure.description(
    "Expected result: the time interval between sending the request and receiving the response is obtained."
)
@allure.tag("Main Page")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test Cases for Ozon")
@allure.testcase("Ozon-8", name="Performance testing")
def test_page_load_time():
    # Create a variable to store the time delta
    # between sending the request to the URL and receiving the response.
    time_delta = requests.get("https://www.ozon.ru/")

    # Print the result of time_delta in seconds,
    # rounded to milliseconds.
    print(f"Result: {round(time_delta.elapsed.total_seconds(), 3)} seconds")

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
