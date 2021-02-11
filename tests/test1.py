import unittest

from storybuilder.hello import helloworld


class HelloTest(unittest.TestCase):

    def test_hello(self):
        self.assertTrue(helloworld())


if __name__ == '__main__':
    unittest.main()
