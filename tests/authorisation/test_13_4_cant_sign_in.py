import allure
from tests.authorisation.test_cant_sign_in import cant_sign_in


@allure.description(
    "Expected result: after clicking the 'Can't sign in' button, the 'Select reason' window opens."
)
@allure.tag("Authorization window")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test cases for Ozon")
@allure.severity(allure.severity_level.MINOR)
@allure.issue(
    "Ozon-bag-tracker-66", name='Missing "Return to main screen" button'
)
@allure.testcase("Ozon-13.4", name="Testing the 'Can't sign in' button")
def test_cant_sign_in():
    # Run the test for the "Can't sign in" button.
    cant_sign_in()
