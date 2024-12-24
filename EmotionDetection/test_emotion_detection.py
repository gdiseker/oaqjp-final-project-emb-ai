import unittest
from .emotion_detection import app

class TestEmotionDetection(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_joy(self):
        response = self.app.post('/', json={'text': 'I am glad this happened'})
        data = response.get_json()
        self.assertEqual(data['dominant_emotion'], 'joy')

    def test_anger(self):
        response = self.app.post('/', json={'text': 'I am really mad about this'})
        data = response.get_json()
        self.assertEqual(data['dominant_emotion'], 'anger')

    def test_disgust(self):
        response = self.app.post('/', json={'text': 'I feel disgusted just hearing about this'})
        data = response.get_json()
        self.assertEqual(data['dominant_emotion'], 'disgust')

    def test_sadness(self):
        response = self.app.post('/', json={'text': 'I am so sad about this'})
        data = response.get_json()
        self.assertEqual(data['dominant_emotion'], 'sadness')

    def test_fear(self):
        response = self.app.post('/', json={'text': 'I am really afraid that this will happen'})
        data = response.get_json()
        self.assertEqual(data['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()