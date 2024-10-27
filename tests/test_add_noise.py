import unittest
from src.add_noise import add_noise_to_sentence, add_noise_to_dataset

class TestAddNoise(unittest.TestCase):

    def test_add_noise_to_sentence(self):
        sentence = "This is a test sentence."
        noised_sentence = add_noise_to_sentence(sentence, noise_level=0.5)
        self.assertNotEqual(sentence, noised_sentence)
        self.assertEqual(len(sentence), len(noised_sentence))

    def test_add_noise_to_dataset(self):
        dataset = [
            "This is the first example sentence.",
            "Here is another one.",
            "Adding random noise to datasets can be fun!"
        ]
        noised_dataset = add_noise_to_dataset(dataset, noise_level=0.5)
        self.assertEqual(len(dataset), len(noised_dataset))
        for original, noised in zip(dataset, noised_dataset):
            self.assertNotEqual(original, noised)
            self.assertEqual(len(original), len(noised))

if __name__ == '__main__':
    unittest.main()
