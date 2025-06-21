import sys

sys.path.append(sys.path[0] + "/../..")
from imports_options import *
from page_elements.MainPageAuthorisationIcon import MainPageAuthorisationIcon
from page_elements.MainPageAuthorisationWindow import (
    MainPageAuthorisationWindow,
    MainPageAuthorisationWindowLocators,
)
from authorisation_page_check import authorisation_page_check


# Create an instance of the ActionChains class.
action = ActionChains(driver)

# Pass control of the page to the driver.
driver.get("https://www.ozon.ru/")
time.sleep(5)

# After launching the driver and opening the main page,
# create an object of the main page class MainPageAuthorisationIcon.
main_page = MainPageAuthorisationIcon(driver)

# Click on the "Face" icon in the header.
wait.until(EC.element_to_be_clickable(main_page.MAIN_FACE_ICON)).click()
time.sleep(2)

# Check that the authorization window has opened.
authorisation_page_check()

# Create an object of the authorization window class MainPageAuthorisationWindow.
authorisation_window = MainPageAuthorisationWindow(driver)
