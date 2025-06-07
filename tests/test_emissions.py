import unittest
from src.emissions.model import estimate_emissions

class TestEmissions(unittest.TestCase):
    def test_estimate_emissions(self):
        self.assertAlmostEqual(estimate_emissions('coche', 10), 1.2)
        self.assertAlmostEqual(estimate_emissions('bus', 10), 0.6)
        self.assertAlmostEqual(estimate_emissions('bici', 10), 0.0)
        self.assertAlmostEqual(estimate_emissions('a pie', 5), 0.0)
        self.assertIsNone(estimate_emissions('desconocido', 10))

if __name__ == '__main__':
    unittest.main()
