from page_objects.base_page import BasePage
from locators.xpaths import XpathComputers


class ElectronicsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_electronics_btn(self):
        self._click()

    def click_product_btn(self, device_btn):
        self._click(device_btn)

    def add_product(self, device_card, add_to_cart_btn):
        self._find_element(device_card)
        self._click(device_card)
        self._find_element(add_to_cart_btn)
        self._click(add_to_cart_btn)

    def is_product_added(self, added_to_cart_device, device_btn, device_card):
        self._click(XpathComputers.shopping_cart_btn)
        added_item_text = self._get_element_text(added_to_cart_device)
        self._click(XpathComputers.computers_btn)
        self._click(device_btn)
        expected_text = self._get_element_text(device_card)

        if added_item_text == expected_text:
            return True
        else:
            return False



