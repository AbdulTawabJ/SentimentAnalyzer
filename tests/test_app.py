import unittest
from src.app import analyze_sentiment

class TestSentimentAnalyzer(unittest.TestCase):

    def test_positive_sentiment(self):
        self.assertEqual(analyze_sentiment("I love this product"), "Positive")

    def test_negative_sentiment(self):
        self.assertEqual(analyze_sentiment("I hate this service"), "Negative")

    def test_neutral_sentiment(self):
        self.assertEqual(analyze_sentiment("It is a table"), "Neutral")

if __name__ == '__main__':
    unittest.main()
