# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BorrarDespues(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_borrar_despues(self):
        driver = self.driver

        #driver.get("https://qservus-qa.redcalidad.com/newsfeed/")
        
        driver.get("https://qservus-qa.redcalidad.com/login/sign_in/")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("hector.sandoval.13@sansano.usm.cl")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("practica_qservus")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        
        driver.find_element_by_xpath("//li[@id='surveys']/a/span").click()
        driver.find_element_by_id("template_new").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("Foto50")
        driver.find_element_by_xpath("//button[@type='submit']").click()

        driver.find_element_by_link_text("Foto").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("Foto con Comentario 50%")
        driver.find_element_by_id("id_help_text").clear()
        driver.find_element_by_id("id_help_text").send_keys("Ayuda")

        driver.find_element_by_id("id_su_question_group_tpl").click()
        Select(driver.find_element_by_id("id_su_question_group_tpl")).select_by_visible_text(u"Página 1")
        driver.find_element_by_id("id_su_question_group_tpl").click()
        
        driver.find_element_by_id("id_priority").click()
        #Cambiar el porcentaje a 100% 30% o 50% para distintos tipos de pregunta
        Select(driver.find_element_by_id("id_priority")).select_by_visible_text("50%")
        driver.find_element_by_id("id_priority").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='menu_questions']/ul/li[5]").click()
        driver.find_element_by_xpath("//ul[@id='pautas_tab']/li[2]/a").click()
       
        



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


		
