from page_objects.book_page import BookPage
from locators.xpaths import XpathBooks


def test_book_page_1(authorized_browser):
    """ Переход на страницу "Books" """
    book_page = BookPage(authorized_browser)
    book_page.click_book_btn()

    """ Проверка открытия карточки товара """
    book_page.add_book_card(XpathBooks.book1, XpathBooks.add_to_cart_onpage)

    """ Проверка того, добавился ли товар """
    book_page.is_book_added(XpathBooks.added_book1, XpathBooks.book1)
