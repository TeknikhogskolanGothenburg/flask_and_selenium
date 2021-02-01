from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def search(driver):
    driver.get('http://127.0.0.1:5000')

    search_field = driver.find_element_by_id('search')
    search_field.clear()
    search_field.send_keys('Stockholm')
    search_field.send_keys(Keys.RETURN)

    search_results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'results')))

    results = search_results.find_elements_by_tag_name('article')
    for result in results:
        print(result.text)


def login(driver):
    driver.get('http://127.0.0.1:5000')
    username_field = driver.find_element_by_id('username')
    password_field = driver.find_element_by_id('password')
    submit = driver.find_element_by_name('submit')

    username_field.send_keys('admin')
    password_field.send_keys('superstar')
    submit.send_keys(Keys.RETURN)

    welcome = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'welcome')))

    print(welcome.text)

def add_friend(driver):
    driver.get('http://127.0.0.1:5000')
    username_field = driver.find_element_by_id('username')
    password_field = driver.find_element_by_id('password')
    submit = driver.find_element_by_name('submit')

    username_field.send_keys('admin')
    password_field.send_keys('superstar')
    submit.send_keys(Keys.RETURN)

    welcome = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'welcome')))

    num_friends = len(driver.find_elements_by_class_name('friend'))
    print(f'We have {num_friends} friends')
    print('Adding new friend Bosse')

    friend_field = driver.find_element_by_id('friend')
    friend_field.send_keys('Bosse')
    friend_field.send_keys(Keys.RETURN)

    welcome = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'welcome')))
    num_friends = len(driver.find_elements_by_class_name('friend'))
    print(f'We now have {num_friends} friends')

def main():
    driver = webdriver.Chrome('chromedriver.exe')
    #search(driver)
    #login(driver)
    add_friend(driver)
    #time.sleep(5)
    driver.close()


if __name__ == '__main__':
    main()
