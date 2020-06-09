from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
import sys
from unittest import skip


class FunctionTest(StaticLiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):
        # cls.server_url = 'http://47.103.1.96/'
        cls.server_url = 'http://127.0.0.1:8000/'
        super().setUpClass()
    
    @classmethod
    def tearDownClass(cls):\
        super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Chrome(options=self.delete_devtools_listening())
        self.browser.implicitly_wait(3)

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')

    def tearDown(self):
        self.browser.quit()

    def delete_devtools_listening(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        return options

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

   