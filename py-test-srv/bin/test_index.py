from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, logging

logging.basicConfig(level=logging.INFO)

SERVICE_URL = "http://py-srv:5000/"

class TestGet(unittest.TestCase):
    """docstring for TestGet."""

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # example
        self.driver = webdriver.Remote(
            "http://selenium:4444/wd/hub", options=options
        )

    def tearDown(self):
        self.driver.quit()

    def test_title(self):
        self.driver.get(SERVICE_URL)
        title = self.driver.title
        assert '"Matplot"' in title