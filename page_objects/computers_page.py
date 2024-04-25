from page_objects.base_page import BasePage
from locators.xpaths import XpathComputers


class ComputersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_computer_btn(self):
        self._click(XpathComputers.computers_btn)

    def click_product_btn(self, device_btn):
        self._click(device_btn) #XpathComputers.desk_btn

    def add_product(self, device_card, add_to_cart_btn):
        self._find_element(device_card) #XpathComputers.comp_1
        self._click(device_card) #XpathComputers.comp_1
        self._find_element(add_to_cart_btn) #XpathComputers.add_cart_btn
        self._click(add_to_cart_btn) #XpathComputers.add_cart_btn

    def is_product_added(self, added_to_cart_device, device_btn, device_card):
        self._click(XpathComputers.shopping_cart_btn)
        added_item_text = self._get_element_text(added_to_cart_device) #XpathComputers.added_comp1
        self._click(XpathComputers.computers_btn)
        self._click(device_btn) #XpathComputers.desk_btn
        expected_text = self._get_element_text(device_card) #XpathComputers.comp_1

        if added_item_text == expected_text:
            return True
        else:
            return False



