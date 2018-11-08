# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CrearPautaMatriz1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_crear_pauta_matriz1(self):
        driver = self.driver
        driver.get("https://qservus-qa.redcalidad.com/newsfeed/")
        driver.find_element_by_xpath("//li[@id='surveys']/a/span").click()
        driver.find_element_by_id("template_new").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("CrearPauta_Matriz_1")
        driver.find_element_by_id("id_subtitle").click()
        driver.find_element_by_id("id_subtitle").clear()
        driver.find_element_by_id("id_subtitle").send_keys("CrearPauta_Matriz_1")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='menu_questions']/ul/li[14]/a/span").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("CrearPauta_Matriz_1")
        driver.find_element_by_id("id_matrix_type").click()
        driver.find_element_by_id("id_scale_label").click()
        driver.find_element_by_id("id_matrix_type").click()
        Select(driver.find_element_by_id("id_matrix_type")).select_by_visible_text(u"Matriz de escala de 7 números")
        driver.find_element_by_id("id_matrix_type").click()
        driver.find_element_by_id("submit_matrix").click()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li/a").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("CrearPauta_Matriz_1")
        driver.find_element_by_id("form_new_question_matrix_alternative").submit()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li/a").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("CrearPauta_Matriz_1")
        driver.find_element_by_id("form_new_question_matrix_alternative").submit()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li/a").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("CrearPauta_Matriz_1")
        driver.find_element_by_id("form_new_question_matrix_alternative").submit()
        driver.find_element_by_xpath("//ul[@id='pautas_tab']/li[2]/a/span").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
