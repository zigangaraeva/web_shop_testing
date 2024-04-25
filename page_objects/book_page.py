from page_objects.base_page import BasePage
from locators.xpaths import XpathBooks



class BookPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_book_btn(self):
        self._click(XpathBooks.books_btn)

    def add_book_card(self, book_locator, add_to_cart_locator):
        self._find_element(book_locator)   #XpathBooks.book1
        self._click(book_locator)          #XpathBooks.book1
        self._find_element(add_to_cart_locator) #XpathBooks.add_to_cart_onpage
        self._click(add_to_cart_locator)  # XpathBooks.add_to_cart_onpage

    def is_book_added(self, added_book, book_locator):
        self._click(XpathBooks.shopping_cart_btn)
        added_item_text = self._get_element_text(added_book) #XpathBooks.added_book1
        self._click(XpathBooks.books_btn)
        expected_text = self._get_element_text(book_locator) #XpathBooks.book1
        if added_item_text == expected_text:
            return True
        else:
            return False