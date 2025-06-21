# Class for different types of scrolls.

class Scrolls:

    def __init__(self, driver, action):
        self.driver = driver
        self.action = action

    # Scroll by x and y
    def scroll_by(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    # Scroll to the very bottom of the page
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Scroll to the very top of the page
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    # Scroll to the element and reveal content beneath it
    def scroll_to_element(self, element):
        self.action.scroll_to_element(element).perform()
        self.driver.execute_script(
            """
        window.scrollTo({
            top: window.scrollY + 500,
        });
        """
        )

    # Scroll to the element and align it to the center of the page
    def scroll_to_center(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({ block: 'center' });", element
        )
