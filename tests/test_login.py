import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin:


    def test_login(self, driver):

        driver.find_element(*locators.LOGIN_BUTTON).click()

        driver.find_element(*locators.EMAIL_FIELD).send_keys(locators.EMAIL_EXISTS)
        driver.find_element(*locators.PASSWORD_FIELD).send_keys(locators.PASSWORD)

        driver.find_element(*locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.AVATAR_IMAGE)))

        # Перехода на главную стр. нет - тренажер так и остается на /login - поэтому проверки нет

        avatar = driver.find_element(*locators.AVATAR_IMAGE)
        assert avatar.is_displayed(), "На главной странице нет аватарки после регистрации"

        name = driver.find_element(*locators.USER_NAME)
        assert name.text == locators.USER_NAME_CONST, f"Имя юзера {name.text} не совпадает с константой {locators.USER_NAME_CONST}"
