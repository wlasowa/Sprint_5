import locators
import data
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:


    def test_registration_new_user(self, driver):

        driver.find_element(*locators.LOGIN_BUTTON).click()
        driver.find_element(*locators.NO_ACCOUNT_BUTTON).click()

        driver.find_element(*locators.EMAIL_FIELD).send_keys(data.EMAIL_RANDOM)
        driver.find_element(*locators.PASSWORD_FIELD).send_keys(data.PASSWORD)
        driver.find_element(*locators.SUBMIT_PASSWORD_FIELD).send_keys(data.PASSWORD)

        driver.find_element(*locators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.AVATAR_IMAGE)))

        # Перехода на главную стр. нет - тренажер так и остается на /regiatration - поэтому проверки нет

        avatar = driver.find_element(*locators.AVATAR_IMAGE)
        assert avatar.is_displayed(), "На главной странице нет аватарки после регистрации"

        name = driver.find_element(*locators.USER_NAME)
        assert name.text == data.USER_NAME_CONST, f"Имя юзера {name.text} не совпадает с константой {data.USER_NAME_CONST}"

    @pytest.mark.parametrize('email',['111', '@', 'test@test', 'test.ru', '@test.ru'])
    def test_registration_invalid_email_negative(self, driver, email):

        driver.find_element(*locators.LOGIN_BUTTON).click()
        driver.find_element(*locators.NO_ACCOUNT_BUTTON).click()

        driver.find_element(*locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*locators.PASSWORD_FIELD).send_keys(data.PASSWORD)
        driver.find_element(*locators.SUBMIT_PASSWORD_FIELD).send_keys(data.PASSWORD)

        driver.find_element(*locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.ERROR_FIELDS)))

        assert len(driver.find_elements(*locators.ERROR_FIELDS)) == 3, "Поля с ошибками не подсвечиваются красным"

        assert driver.find_element(*locators.EMAIL_FIELD_ERROR).text == 'Ошибка', "Нет сообщения об ошибке email"

    def test_registration_exists_negative(self, driver):
        
        driver.find_element(*locators.LOGIN_BUTTON).click()
        driver.find_element(*locators.NO_ACCOUNT_BUTTON).click()

        driver.find_element(*locators.EMAIL_FIELD).send_keys(data.EMAIL_EXISTS)
        driver.find_element(*locators.PASSWORD_FIELD).send_keys(data.PASSWORD)
        driver.find_element(*locators.SUBMIT_PASSWORD_FIELD).send_keys(data.PASSWORD)

        driver.find_element(*locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.ERROR_FIELDS)))

        assert len(driver.find_elements(*locators.ERROR_FIELDS)) == 3, "Поля с ошибками не подсвечиваются красным"

        assert driver.find_element(*locators.EMAIL_FIELD_ERROR).text == 'Ошибка', "Нет сообщения об ошибке email"
        