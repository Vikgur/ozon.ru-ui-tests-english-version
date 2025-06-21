# Import driver options and open the authorization window.
from tests.authorisation.test_auth_window_imports_options import *


@allure.description(
    "Expected result: when selecting the country code 'United States +1', the code is successfully switched to '+1'."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.testcase("Ozon-13.2", name="Testing the country code dropdown list")
def test_code_list():
    # Click on the country code dropdown list.
    wait.until(EC.element_to_be_clickable(authorisation_window.CODE_LIST)).click()
    time.sleep(2)

    # Create a locator for the country code "United States".
    CODE_USA_LOCATOR = ("xpath", "//span[normalize-space(.)='Соединенные Штаты +1']")

    # Create an element for the country code "United States".
    CODE_USA = driver.find_element(*CODE_USA_LOCATOR)

    # Click on the "United States" country code.
    wait.until(EC.element_to_be_clickable(CODE_USA)).click()
    time.sleep(2)

    # Create a locator for the selected country code "+1".
    CODE_USA_CHECK_LOCATOR = ("xpath", "//span[normalize-space(.)='+1']")

    # Create an element for checking if "+1" is selected.
    CODE_USA_CHECK = driver.find_elements(*CODE_USA_CHECK_LOCATOR)

    # Check via assert that "+1" was selected.
    assert len(CODE_USA_CHECK) > 0, 'Country code "United States" was not selected :-('

    # Check via print that "+1" was selected.
    if len(CODE_USA_CHECK) > 0:
        print('Country code "United States" selected!')
    else:
        print('Country code "United States" not selected :-(')

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
