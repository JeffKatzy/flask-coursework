import unittest

def sayHello():
    return 'say not hello'

class SimplisticTest(unittest.TestCase):
    def test_sayHello(self):
        self.assertEqual(sayHello(), 'say hello', msg="it does not say hello")

    def test_sayGoodbye(self):
        self.assertEqual(sayGoodbye(), 'goodbye', msg="it does not say 'goodbye'")

    def test_capitalizeName(self):
        self.assertEqual(capitalizeName('tom'), 'Tom', msg="it capitalizes the names")

    def test_combineNames(self):
        self.assertTrue('Tom' in combineNames('tom', 'brady'), msg="it capitalizes the first name")
        self.assertTrue('Brady' in combineNames('tom', 'brady'), msg="it capitalizes the last name")
        self.assertEqual(combineNames('tom', 'brady'), 'Tom Brady', msg="it combines the two names")
        self.assertEqual(combineNames('michael', 'jordan'), 'Michael Jordan', msg="it combines the two names")

    def test_addNumbers(self):
        self.assertEquals(addNumbers(3, 4), 7, msg="it adds the two numbers")
        self.assertEquals(addNumbers(5, 1), 6, msg="it adds the two numbers")

if __name__ == '__main__':
    unittest.main()
