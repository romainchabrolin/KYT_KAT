from selenium import webdriver
from selenium.webdriver import *
import time

driver = webdriver.Chrome(executable_path='/home/chabrolin/Delivery/TEK2/RPA/chromedriver')
driver.maximize_window()

class KYT_KAT():

    def __init__(self):
        self.access_to_intra_page()
        self.connect_to_office()
        self.access_to_module_page()
        self.check_is_registered()
        time.sleep(1)
        driver.quit()

    def access_to_intra_page(self):
        driver.get("https://intra.epitech.eu/")
        driver.find_element_by_xpath('//*[@id="gdpr-banner"]/div/div/a[1]/span/span[2]').click()
        print("Access to the intra page succesfully.")

    def connect_to_office(self):
        driver.find_element_by_xpath('//*[@id="auth-login"]/fieldset/div/div/div[1]/a').click()
        driver.find_element_by_id('i0116').send_keys('YOUR EPITECH ADDRESS')
        driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('YOUR EPITECH PASSWORD')
        driver.find_element_by_xpath('//*[@id="submitButton"]').click()
        driver.find_element_by_id('idSIButton9').click()
        print("Connect to office 365 successfully.")

    def access_to_module_page(self):
        driver.find_element_by_class_name('module').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[contains(text(), "MyChap")]').click()
        driver.find_element_by_xpath('//*[contains(text(), "Voir les details du projet")]').click()
        print("Access to the module page successfully.")

    def check_is_registered(self):
        driver.find_element_by_xpath('//*[contains(text(), "[B4][NWP] MyChap romain.chabrolin@epitech.eu")]')
        print("Student is registered")

def main():
    print('>> KYT KAT')
    KYT_KAT()
    print("Finish")

if __name__ == "__main__":
    main()
