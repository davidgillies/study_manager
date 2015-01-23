from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # waits a little to let browser respond
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    # Susie has to use this hopeless setup to manage studies...
    # She goes to the dashboard at the root
    # She sees the page title is 'Dashboard'
    def test_dashboard_is_there(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Dashboard', self.browser.title)

    def test_study_is_there(self):
        self.browser.get('http://localhost:8000/study_manager/')
        self.assertIn('Study Admin', self.browser.title)


if __name__ == '__main__':
    unittest.main()
