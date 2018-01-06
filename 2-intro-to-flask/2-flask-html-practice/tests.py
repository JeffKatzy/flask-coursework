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
        self.assertTrue("Welcome!" in htmlString)

    def test_homeContenthasH1(self):
        """initial test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        htmlString = response.data.decode("utf-8")
        html = BeautifulSoup(htmlString, "lxml")
        self.assertTrue("Welcome!" in html.h1.text, "Welcome! in h1 tag")

    def test_aboutContent(self):
        """initial test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        htmlString = response.data.decode("utf-8")
        html = BeautifulSoup(htmlString, "lxml")
        self.assertTrue("All about our restaurant" in html.h1.text)

    def test_teamContent(self):
        """initial test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/team', content_type='html/text')
        htmlString = response.data.decode("utf-8")
        html = BeautifulSoup(htmlString, "lxml")
        self.assertTrue("Built by two best friends!" in html.h1.text)

    def test_homepageLinksToAbout(self):
        """Ensure there is a link with text About"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        htmlString = response.data.decode("utf-8")
        html = BeautifulSoup(htmlString, "lxml")
        element = html.find('a', text="About")
        self.assertTrue(element != None)

    def test_homepageLinksToAbout(self):
        """Ensure About link points to about page"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        htmlString = response.data.decode("utf-8")
        html = BeautifulSoup(htmlString, "lxml")
        element = html.find('a', text="About")
        self.assertTrue(html.find('a', {"href": "/about"}).text == "About")

    def test_homepageLinksToTeam(self):
        """Ensure there is a link with text Team"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        htmlString = response.data.decode("utf-8")
        html = BeautifulSoup(htmlString, "lxml")
        element = html.find('a', text="Team")
        self.assertTrue(element != None)

    def test_homepageLinksToTeam(self):
        """Ensure About link points to team page"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        htmlString = response.data.decode("utf-8")
        html = BeautifulSoup(htmlString, "lxml")
        element = html.find('a', text="About")
        self.assertTrue(html.find('a', {"href": "/team"}).text == "Team")

if __name__ == '__main__':
    unittest.main()
