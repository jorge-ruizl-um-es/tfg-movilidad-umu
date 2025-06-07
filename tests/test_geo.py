import unittest
from src.geo.distance import haversine_km

class TestGeoDistance(unittest.TestCase):
    def test_haversine_known_distance(self):
        lat1, lon1 = 38.0, -1.0
        lat2, lon2 = 38.1, -1.1
        dist = haversine_km(lat1, lon1, lat2, lon2)
        self.assertTrue(13 < dist < 15)

    def test_same_point(self):
        dist = haversine_km(38.0, -1.0, 38.0, -1.0)
        self.assertEqual(dist, 0.0)

if __name__ == '__main__':
    unittest.main()
