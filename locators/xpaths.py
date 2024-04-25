from selenium.webdriver.common.by import By


""" Страница авторизации """
class XpathLoginPage:
    login = (By.XPATH, '//input[@name = "Email"]')
    password = (By.XPATH, '//input[@id = "Password"]')
    login_btn = (By.XPATH, '//input[@class = "button-1 login-button"]')
    welcome_to_store = (By.XPATH, '//h2[@class = "topic-html-content-header"]')


""" Страница "Books" """
class XpathBooks:
    books_btn = (By.XPATH, "(//a[contains(text(), 'Books')])[1]")
    add_to_cart_onpage = (By.XPATH, "(//input[contains(@class, 'button-2')])[1]")
    notification = (By.XPATH, "//div[@id='bar-notification']")
    shopping_cart_btn = (By.XPATH, "(//a[@class='ico-cart'])[1]")
    """ Книги """
    book1 = (By.XPATH, "(//div[@class='product-item'])[1]")
    add_to_cart = (By.XPATH, "//input[contains(@id, 'add-')]")
    added_book1 = (By.XPATH, "(//a[contains(@class, 'product-name')])[1]")
    book2 = (By.XPATH, '(//div[@class="item-box"])[2]')
    book3 = (By.XPATH, '(//div[@class="item-box"])[3]')

""" Страница "Computers" """
class XpathComputers:
    computers_btn = (By.XPATH, "(//a[contains(text(), 'Computers')])[1]")
    shopping_cart_btn = (By.XPATH, "(//a[@class='ico-cart'])[1]")
    comp_1 = (By.XPATH, "(//div[@class='item-box'])[1]")
    add_cart_btn = (By.XPATH, "//input[contains(@id, 'add-')]")

    """ Desktops """
    desk_btn = (By.XPATH, "(//div[@class='item-box'])[1]")
    added_comp1 = (By.XPATH, "(//a[contains(@class, 'product-name')])[2]")

    """ Notebooks """
    note_btn = (By.XPATH, "(//div[@class='item-box'])[2]")
    note_card = (By.XPATH, "//div[@class='item-box']")

    """ Accessories """
    access_btn = (By.XPATH, "(//div[@class='item-box'])[3]")
    access_card = (By.XPATH, "//div[@class='item-box']")





  

