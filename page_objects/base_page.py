
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _find_element(self, selector, index=0):
        return self.driver.find_elements(*selector)[index]

    def _find_elements(self, selector):
        return self.driver.find_elements(*selector)

    def _click(self, selector, index=0):
        element = self._find_element(selector, index)
        element.click()

    def _input(self, selector, value, index=0):
        element = self._find_element(selector, index)
        element.clear()
        element.send_keys(value)

    def _get_element_text(self, selector, index=0):
        return self._find_element(selector, index).text

