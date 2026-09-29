import random
from selenium.webdriver.common.by import By

DOSKA_URL = "https://qa-desk.education-services.ru/"
EMAIL_RANDOM = f"testmail{random.randint(100, 999)}@ya.ru"
EMAIL_EXISTS = "testmail8@ya.ru"
PASSWORD = "123"
USER_NAME_CONST = 'User.'
AD_MODAL_TEXT = 'Чтобы разместить объявление, авторизуйтесь'
BOOK_TITLE = f"Москва {random.randint(2030, 2099)}"
BOOK_DESCRIPTION = "Новый фантастический роман"
PRICE = random.randint(10, 999)

# Главная страница
LOGIN_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
NO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")
AVATAR_IMAGE = (By.XPATH, ".//button[@class='circleSmall']")
USER_NAME = (By.XPATH, ".//h3[@class='profileText name']")
ENTER_BUTTON = (By.XPATH, ".//button[text()='Войти']")
EXIT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
AD_BUTTON = (By.XPATH, ".//button[text()='Разместить объявление']")
AD_MODAL = (By.XPATH, ".//form//h1[@class='h1']")
AD_CARDS = (By.CLASS_NAME, "card")

# Форма регистрации аккаунта
EMAIL_FIELD = (By.NAME, "email")
PASSWORD_FIELD = (By.NAME, "password")
SUBMIT_PASSWORD_FIELD = (By.NAME, "submitPassword")
CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
ERROR_FIELDS = (By.XPATH, ".//div[@class='input_inputError__fLUP9']")
EMAIL_FIELD_ERROR = (By.XPATH, ".//span[@class='input_span__yWPqB']")

# Форма подачи объявления
TITLE_FIELD = (By.NAME, "name")
DESCR_FIELD = (By.XPATH, ".//textarea[@name='description']")
PRICE_FIELD = (By.NAME, "price")
CATEGORY_BUTTON = (By.XPATH, ".//*[contains(@class, 'createListing_inputRow')]//*[contains(@class, 'dropDownMenu_arrowDown')]")
CATEGORY_BOOKS = (By.XPATH, ".//button/span[text()='Книги']")
CITY_BUTTON = (By.XPATH, "(//*[contains(@class, 'dropDownMenu_dropMenu__sBxhz')]//*[contains(@class, 'dropDownMenu_arrowDown')])[2]")
CITY_NOVOSIB = (By.XPATH, ".//button/span[text()='Новосибирск']")
ITEM_STATE_RBUTTON = (By.CLASS_NAME, "radioUnput_inputRegular__FbVbr")
PUBLISH_BUTTON = (By.XPATH, ".//button[text()='Опубликовать']")

# Профиль юзера
MY_AD_TITLE = (By.XPATH, ".//div[@class='card']//div[@class='about']/h2")