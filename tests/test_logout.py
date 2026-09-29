import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLogout:


    def test_logout(self, driver):

        driver.find_element(*locators.LOGIN_BUTTON).click()

        driver.find_element(*locators.EMAIL_FIELD).send_keys(locators.EMAIL_EXISTS)
        driver.find_element(*locators.PASSWORD_FIELD).send_keys(locators.PASSWORD)

        driver.find_element(*locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.EXIT_BUTTON)))

        driver.find_element(*locators.EXIT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element_located((locators.AVATAR_IMAGE)))

        avatar = driver.find_elements(*locators.AVATAR_IMAGE)
        assert len(avatar) == 0, "На главной странице осталась аватарка после разлогина"

        name = driver.find_elements(*locators.USER_NAME)
        assert len(name) == 0, f"Имя юзера {name.text} осталось на стр. после разлогина"

        login_btn = driver.find_element(*locators.LOGIN_BUTTON)
        assert login_btn.is_displayed(), "Не появилась кнопка входа"
