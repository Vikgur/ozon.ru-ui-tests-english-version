import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from page_elements.MainPage import MainPage


@allure.description(
    "Expected result: when hovering over the 'order list' icon, its color should change."
)
@allure.tag("Main Page")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Test Cases for Ozon")
@allure.testcase(
    "Ozon-2",
    name="Testing the color change of the 'order list' icon on hover",
)
def test_colour_change():
    # Create an ActionChains object.
    action = ActionChains(driver)

    # Navigate to the main page.
    driver.get("https://www.ozon.ru/")
    time.sleep(5)

    # After launching the driver and opening the main page,
    # create a MainPage object.
    main_page = MainPage(driver)

    # Get the element before mouse hover.
    before_move_to_element = main_page.MAIN_ORDER_LIST

    # Store the integer value of the color before hover.
    colour_before = int(
        "".join(
            i
            for i in before_move_to_element.value_of_css_property("color")
            if i.isdigit()
        )
    )
    time.sleep(2)

    # Print the RGBA color of the element before hover.
    print(
        f'Color before hover: {before_move_to_element.value_of_css_property("color")}'
    )

    # Perform mouse hover action.
    action.move_to_element(before_move_to_element).perform()
    time.sleep(5)

    # Get the element after mouse hover.
    after_move_to_element = main_page.MAIN_ORDER_LIST

    # Store the integer value of the color after hover.
    colour_after = int(
        "".join(
            i
            for i in before_move_to_element.value_of_css_property("color")
            if i.isdigit()
        )
    )

    # Print the RGBA color of the element after hover.
    print(
        f'Color after hover: {after_move_to_element.value_of_css_property("color")}'
    )

    # Assert that the color has changed after hover.
    assert colour_before != colour_after, "Text color did not change :-("

    # Print the result.
    if colour_before != colour_after:
        print("Element color changed: TEST PASSED SUCCESSFULLY!")
    else:
        print("Color did not change :-(")

    driver.quit()

