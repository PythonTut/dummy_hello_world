import unittest
from hello_world import hello_world


class HelloWorldTest(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual("Hello, World!", hello_world())
