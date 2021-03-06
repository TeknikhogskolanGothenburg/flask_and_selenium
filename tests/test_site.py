import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WowSiteTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver.exe')

    def test_search(self):
        self.driver.get('http://127.0.0.1:5000')

        search_field = self.driver.find_element_by_id('search')
        search_field.clear()
        search_field.send_keys('Stockholm')
        search_field.send_keys(Keys.RETURN)

        search_results = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'results')))

        results = [item.text for item in search_results.find_elements_by_tag_name('article')]
        self.assertIn('Stockholm, Sweden', results)
        self.assertEqual(len(results), 6)

    def test_login(self):
        self.driver.get('http://127.0.0.1:5000')
        username_field = self.driver.find_element_by_id('username')
        password_field = self.driver.find_element_by_id('password')
        submit = self.driver.find_element_by_name('submit')

        username_field.send_keys('admin')
        password_field.send_keys('superstar')
        submit.send_keys(Keys.RETURN)

        welcome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'welcome')))
        self.assertEqual('Welcome admin', welcome.text)

    def test_add_friend(self):
        self.driver.get('http://127.0.0.1:5000')
        username_field = self.driver.find_element_by_id('username')
        password_field = self.driver.find_element_by_id('password')
        submit = self.driver.find_element_by_name('submit')

        username_field.send_keys('admin')
        password_field.send_keys('superstar')
        submit.send_keys(Keys.RETURN)

        welcome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'welcome')))

        num_friends_before = len(self.driver.find_elements_by_class_name('friend'))

        friend_field = self.driver.find_element_by_id('friend')
        friend_field.send_keys('Bosse')
        friend_field.send_keys(Keys.RETURN)

        welcome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'welcome')))
        num_friends_after = len(self.driver.find_elements_by_class_name('friend'))

        self.assertEqual(num_friends_before+1, num_friends_after)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
