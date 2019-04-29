
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()

def main():
    driver.get("https://10fastfingers.com/typing-test/french")
    my_input = driver.find_element_by_xpath('//*[@id="inputfield"]')
    index = 1
    while 1:
        words = []
        for i in range(index, index + 10):
            word = driver.find_element_by_xpath(f'//*[@id="row1"]/span[{i}]')
            words.append(word.text)
        for i in words:
            my_input.send_keys(i)
            my_input.send_keys(Keys.SPACE)
        index += 10

if __name__ == "__main__":
    main()