import allure
from tests.authorisation.test_close_window import close_window


@allure.description(
    "Expected result: after clicking the 'X' button in the top right corner, the authorization window closes."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.5", name="Testing the authorization window close button 'X'")
def test_close_window():
    # Run the test for the 'X' button that closes the authorization window.
    close_window()
