import locators
import data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestAd:


    def test_ad_unauthorized(self, driver):

        driver.find_element(*locators.AD_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.AD_MODAL)))

        modal = driver.find_element(*locators.AD_MODAL)
        assert modal.text == data.AD_MODAL_TEXT, f"Заголовок окна {modal.text} отличается от ожидаемого {locators.AD_MODAL_TEXT}"

    def test_ad_authorized(self, driver):

        driver.find_element(*locators.LOGIN_BUTTON).click()

        driver.find_element(*locators.EMAIL_FIELD).send_keys(data.EMAIL_EXISTS)
        driver.find_element(*locators.PASSWORD_FIELD).send_keys(data.PASSWORD)

        driver.find_element(*locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.EXIT_BUTTON)))
        
        driver.find_element(*locators.AD_BUTTON).click()

        title = data.BOOK_TITLE
        price = data.PRICE

        driver.find_element(*locators.TITLE_FIELD).send_keys(title)
        driver.find_element(*locators.DESCR_FIELD).send_keys(data.BOOK_DESCRIPTION)
        driver.find_element(*locators.PRICE_FIELD).send_keys(price)

        driver.find_element(*locators.CATEGORY_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.CATEGORY_BOOKS)))

        driver.find_element(*locators.CATEGORY_BOOKS).click()

        driver.find_element(*locators.CITY_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.CITY_NOVOSIB)))

        driver.find_element(*locators.CITY_NOVOSIB).click()

        driver.find_element(*locators.ITEM_STATE_RBUTTON).click()
        driver.find_element(*locators.PUBLISH_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_all_elements_located(locators.AD_CARDS))

        driver.execute_script("window.scrollTo(0, 0);")

        avatar = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.AVATAR_IMAGE))
        avatar.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.MY_AD_TITLE)))

        element = driver.find_elements(*locators.MY_AD_TITLE)[-1]
        driver.execute_script("arguments[0].scrollIntoView();", element)

        assert element.text == title, f"Названия последней карточки {element.text} и ожидаемое {title} не совпадают"

