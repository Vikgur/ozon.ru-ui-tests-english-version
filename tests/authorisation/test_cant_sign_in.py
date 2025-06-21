# Import driver options and open the authorization window.
from tests.authorisation.test_auth_window_imports_options import *


# Create a function to test the "Can't sign in" button.
def cant_sign_in():

    # Click the "Can't sign in" button.
    wait.until(EC.element_to_be_clickable(authorisation_window.CAN_NOT_SIGN_IN)).click()
    time.sleep(2)

    # Create a locator variable to check
    # transition to the "Choose a reason" window.
    REASON_WHY_LOCATOR = ("xpath", "//div[normalize-space(.)='Выберите причину']")

    # Create a variable to verify
    # transition to the "Choose a reason" window.
    REASON_WHY = driver.find_element(*REASON_WHY_LOCATOR)

    # Check via assert the transition to the "Choose a reason" window.
    assert (
        REASON_WHY.text == "Выберите причину"
    ), 'Transition to the "Choose a reason" window failed :-('

    # Check via print the transition to the "Choose a reason" window.
    if REASON_WHY.text == "Выберите причину":
        print('"Choose a reason" window opened successfully!')
    else:
        print('Transition to the "Choose a reason" window failed :-(')

    # Create a variable for the "Back to main screen" button element.
    BACK_TO_AUTHORISATION_WINDOW = driver.find_element(
        "xpath", "//button[normalize-space(.)='Вернуться на главный экран']"
    ).text

    # Check via assert that the button exists.
    assert (
        BACK_TO_AUTHORISATION_WINDOW.text == "Вернуться на главный экран"
    ), '"Back to main screen" button is missing'

    print("TEST PASSED SUCCESSFULLY!")

    driver.quit()
