from page_objects.computers_page import ComputersPage
from locators.xpaths import XpathComputers


def test_comp_page_desktops_1(authorized_browser):
    desk_page = ComputersPage(authorized_browser)
    """ Переход на страницу "Computers" """
    desk_page.click_computer_btn()

    """ Переход на страницу "Desktops" """
    desk_page.click_product_btn(XpathComputers.desk_btn)

    """ Добавление компьютера в корзину """
    desk_page.add_product(XpathComputers.comp_1, XpathComputers.add_cart_btn)

    """ Проверка того, добавился ли компьютер в корзину """
    desk_page.is_product_added(XpathComputers.added_comp1, XpathComputers.desk_btn, XpathComputers.comp_1)


def test_comp_page_notebooks_1(authorized_browser):
    note_page = ComputersPage(authorized_browser)
    """ Переход на страницу "Computers" """
    note_page.click_computer_btn()

    """ Переход на страницу "Notebooks" """
    note_page.click_product_btn(XpathComputers.note_btn)

    """ Добавление ноутбука в корзину """
    note_page.add_product(XpathComputers.note_card, XpathComputers.add_cart_btn)

    """ Проверка того, добавился ли ноутбук в корзину """
    note_page.is_product_added(XpathComputers.added_comp1, XpathComputers.desk_btn, XpathComputers.comp_1)


def test_comp_page_accessories_1(authorized_browser):
    access_page = ComputersPage(authorized_browser)
    """ Переход на страницу "Computers" """
    access_page.click_computer_btn()

    """ Переход на страницу "Notebooks" """
    access_page.click_product_btn(XpathComputers.access_btn)

    """ Добавление ноутбука в корзину """
    access_page.add_product(XpathComputers.access_card, XpathComputers.add_cart_btn)

    """ Проверка того, добавился ли ноутбук в корзину """
    access_page.is_product_added(XpathComputers.added_comp1, XpathComputers.access_btn, XpathComputers.comp_1)