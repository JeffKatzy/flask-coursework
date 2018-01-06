from restaurant import app
import unittest
import pdb
from bs4 import BeautifulSoup

class BasicTestCase(unittest.TestCase):
    def test_home(self):
        """initial test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        htmlString = response.data.decode("utf-8")
        self.assertEqual(response.status_code, 200)

    def test_homeContent(self):
        """initial test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        htmlString = response.data.decode("utf-8")
        self.assertEqual(htmlString, "hello world")

    def test_aboutPage(self):
        """initial test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        htmlString = response.data.decode("utf-8")
        self.assertEqual(htmlString, "A family owned restaurant!")

    def test_teamPage(self):
        """initial test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/team', content_type='html/text')
        htmlString = response.data.decode("utf-8")
        self.assertEqual(htmlString, "Built by two best friends!")

if __name__ == '__main__':
    unittest.main()
