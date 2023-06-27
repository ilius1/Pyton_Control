import pytest
import allure
from selenium.webdriver import ActionChains
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


url = 'https://magento.softwaretestingboard.com/'
adres=''         #ввести почту
security=''      #ввести пароль


@pytest.mark.usefixtures('setup')
class Test:

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store1(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/a/img').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store2(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/footer/div/ul/li[5]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/a/img').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store3(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[2]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/footer/div/ul/li[4]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/a/img').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store4(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[2]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/footer/div/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/a/img').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store5(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-3"]/span').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div/div/ul[1]/li[1]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[1]/div[1]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[1]/div[2]/ol/li[1]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/a/img').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store6(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="firstname"]').click()
            element61 = self.browser.find_element(By.XPATH, '//*[@id="firstname"]').send_keys('Иван')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element61 == "Иван", "Ошибка!!!!"

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store7(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="firstname"]').click()
            element71 = self.browser.find_element(By.XPATH, '//*[@id="firstname"]').send_keys('Иван')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element71 == "Иван", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="lastname"]').click()
            element72 = self.browser.find_element(By.XPATH, '//*[@id="lastname"]').send_keys('Иванов')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element72 == "Иванов", "Ошибка!!!!"

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store8(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="firstname"]').click()
            element81 = self.browser.find_element(By.XPATH, '//*[@id="firstname"]').send_keys('Иван')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element81 == "Иван", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="lastname"]').click()
            element82 = self.browser.find_element(By.XPATH, '//*[@id="lastname"]').send_keys('Иванов')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element82 == "Иванов", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="is_subscribed"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store9(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="firstname"]').click()
            element91 = self.browser.find_element(By.XPATH, '//*[@id="firstname"]').send_keys('Иван')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element91 == "Иван", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="lastname"]').click()
            element92 = self.browser.find_element(By.XPATH, '//*[@id="lastname"]').send_keys('Иванов')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element92 == "Иванов", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="is_subscribed"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="email_address"]').click()
            element93 = self.browser.find_element(By.XPATH,
                                                  '//*[@id="email_address"]').send_keys(adres)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element93 == adres, "Ошибка!!!!"

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store10(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="firstname"]').click()
            element101 = self.browser.find_element(By.XPATH, '//*[@id="firstname"]').send_keys('Иван')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element101 == "Иван", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="lastname"]').click()
            element102 = self.browser.find_element(By.XPATH, '//*[@id="lastname"]').send_keys('Иванов')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element102 == "Иванов", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="is_subscribed"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="email_address"]').click()
            element103 = self.browser.find_element(By.XPATH,
                                                  '//*[@id="email_address"]').send_keys(adres)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element103 == adres, "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="email_address"]').click()
            element104 = self.browser.find_element(By.XPATH,
                                                  '//*[@id="email_address"]').send_keys(security)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element104 == security, "Ошибка!!!!"

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store11(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="firstname"]').click()
            element111 = self.browser.find_element(By.XPATH, '//*[@id="firstname"]').send_keys('Иван')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element111 == "Иван", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="lastname"]').click()
            element112 = self.browser.find_element(By.XPATH, '//*[@id="lastname"]').send_keys('Иванов')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element112 == "Иванов", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="is_subscribed"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="email_address"]').click()
            element113 = self.browser.find_element(By.XPATH,
                                                   '//*[@id="email_address"]').send_keys(adres)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element113 == adres, "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="password"]').click()
            element114 = self.browser.find_element(By.XPATH,
                                                   '//*[@id="password"]').send_keys(security)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element114 == security, "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="password-confirmation"]').click()
            element115 = self.browser.find_element(By.XPATH,
                                                   '//*[@id="password-confirmation"]').send_keys(security)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element115 == security, "Ошибка!!!!"

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store12(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="firstname"]').click()
            element121 = self.browser.find_element(By.XPATH, '//*[@id="firstname"]').send_keys('Иван')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element121 == "Иван", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="lastname"]').click()
            element122 = self.browser.find_element(By.XPATH, '//*[@id="lastname"]').send_keys('Иванов')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element122 == "Иванов", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="is_subscribed"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="email_address"]').click()
            element123 = self.browser.find_element(By.XPATH,
                                                   '//*[@id="email_address"]').send_keys(adres)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element123 == adres, "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="password"]').click()
            element124 = self.browser.find_element(By.XPATH,
                                                   '//*[@id="password"]').send_keys(security)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element124 == security, "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="password-confirmation"]').click()
            element125 = self.browser.find_element(By.XPATH,
                                                   '//*[@id="password-confirmation"]').send_keys(security)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element125 == security, "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="form-validate"]/div/div[1]/button/span').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_storeOUT(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            with allure.step('Открывает ссылку'):
                self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[2]/div/ul/li[3]/a').click()
                allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                              attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store13(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[2]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="email"]').click()
            element131 = self.browser.find_element(By.XPATH, '//*[@id="email"]').send_keys(adres)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element131 == adres, "Ошибка!!!!"

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store14(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[2]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="email"]').click()
            element141 = self.browser.find_element(By.XPATH, '//*[@id="email"]').send_keys(adres)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element141 == adres, "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="pass"]').click()
            element142 = self.browser.find_element(By.XPATH, '//*[@id="pass"]').send_keys(security)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element142 == security, "Ошибка!!!!"

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store15(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[2]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="email"]').click()
            element151 = self.browser.find_element(By.XPATH, '//*[@id="email"]').send_keys(adres)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element151 == adres, "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="pass"]').click()
            element152 = self.browser.find_element(By.XPATH, '//*[@id="pass"]').send_keys(security)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        #assert element152 == security, "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="send2"]/span').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
