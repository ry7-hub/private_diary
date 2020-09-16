from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver


class TestSample(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path='C:/tool/chromedriver.exe')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_sample(self):
        # ログインページを開く
        self.selenium.get('http://localhost:8000')

        # Inquiryクリック
        self.selenium.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[1]/li/a').click()
        self.selenium.find_element_by_xpath('//*[@id="wrapper"]/nav/div/a').click()

        # テキトーに検証
        self.assertEqual('web上にあなた専用の日記ページを保存できるサービス | Private Diary', self.selenium.title)

    def test_sample2(self):
        # ログインページを開く
        # self.selenium.get('http://localhost:8000')

        self.selenium.implicitly_wait(20)

        # Inquiryクリック
        self.selenium.find_element_by_xpath('//*[@id="navbarResponsive"]/ul[1]/li/a').click()
        self.selenium.find_element_by_xpath('//*[@id="wrapper"]/nav/div/a').click()

        # テキトーに検証
        self.assertEqual('web上にあなた専用の日記ページを保存できるサービス | Private Diary', self.selenium.title)
