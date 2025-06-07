
import unittest
import pandas as pd
from src.simulation.agent_model import CommuteSimulation

class TestCommuteSimulation(unittest.TestCase):
    def test_simulation_runs_and_generates_trajectories(self):
        # Datos mínimos de ejemplo
        data = {
            'Lat_Residencia': [38.0, 38.1],
            'Lon_Residencia': [-1.0, -1.1],
            'Lat_Trabajo': [38.05, 38.15],
            'Lon_Trabajo': [-1.05, -1.15],
        }
        df = pd.DataFrame(data)

        # Ejecutar simulación
        model = CommuteSimulation(df)
        model.run(steps=10)

        # Comprobar que cada agente tiene una trayectoria con al menos 2 puntos
        trajectories = model.get_trajectories()
        self.assertEqual(len(trajectories), 2)
        for path in trajectories:
            self.assertGreaterEqual(len(path), 2)
            self.assertIsInstance(path, list)
            self.assertTrue(all(isinstance(p, tuple) and len(p) == 2 for p in path))

if __name__ == '__main__':
    unittest.main()
