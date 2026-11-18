import unittest
from src.app import greet

class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet(), 
            "Hello, Raiven Christian Navor! Welcome to Software Engineering."
        )

if __name__ == "__main__":
    unittest.main()