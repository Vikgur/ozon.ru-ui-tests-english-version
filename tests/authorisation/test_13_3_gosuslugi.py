# Import driver options and open the authorization window.
from tests.authorisation.test_auth_window_imports_options import *


@allure.description(
    "Expected result: after clicking the 'Log in via Gosuslugi' button, the Gosuslugi window opens."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.3", name="Testing login via Gosuslugi")
def test_gosuslugi():
    # Click on the "Log in via Gosuslugi" button.
    action.click(on_element=authorisation_window.GOSUSLUGI_BUTTON).perform()
    time.sleep(2)

    # Switch the driver to the second tab with the Gosuslugi window.
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # Verify via assert that the Gosuslugi window is opened.
    assert (
        driver.title == "Портал государственных услуг Российской Федерации"
    ), "Redirection to Gosuslugi was not successful :-("

    # Verify via print that the Gosuslugi window is opened.
    if driver.title == "Портал государственных услуг Российской Федерации":
        print("Gosuslugi window opened successfully!")
    else:
        print("Redirection to Gosuslugi was not successful :-(")

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
