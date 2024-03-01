from Dexturret.Turret.simulation import Simulation
from Dexturret.Turret.robot import Robot

import unittest

class TestSimulation(unittest.TestCase):
    def test_simulation_est_instancce_de_simulation(self):
        robot = Robot("Dexter", 50, 25, 0, 0)
        test_simu = Simulation(1, robot, 1000, 700, 60)
        self.assertEqual(test_simu.id, 1)
        self.assertEqual(test_simu.robot, robot)
        self.assertEqual(test_simu.longueur, 1000)
        self.assertEqual(test_simu.largeur, 700)
        self.assertEqual(test_simu.fps, 60)
        self.assertTrue(test_simu.awake)

    def test_simulation_check_collision_arrete_simu(self):
        robot = Robot("Dexter", 50, 25, 0, 0)
        test_simu = Simulation(1, robot, 1000, 700, 60)
        robot.x = 1100
        test_simu.check_collision()
        self.assertFalse(test_simu.awake)

if __name__ == '__main__':
    unittest.main()
