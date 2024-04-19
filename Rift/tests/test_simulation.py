from Dexturret.simu.simulation import Simulation
from Dexturret.simu.robot import Robot
from time import time

import unittest

#tester avec la commande python3 -m tests.test_simulation

class TestSimulation(unittest.TestCase):
    def test_simulation_est_instancce_de_simulation(self):
        test_robot = Robot(1, 50, 25, 5, 1000/2, 700/2, time())
        test_simu = Simulation(1, test_robot, 1000, 700, 60)
        self.assertEqual(test_simu.id, 1)
        self.assertEqual(test_simu.robot, test_robot)
        self.assertEqual(test_simu.longueur, 700)
        self.assertEqual(test_simu.largeur, 1000)
        self.assertEqual(test_simu.fps, 60)
        self.assertTrue(test_simu.awake)

    def test_simulation_check_collision_arrete_simu(self):
        robot = Robot("Dexter", 50, 25, 5, 1100, 700, time())
        test_simu = Simulation(1, robot, 1000, 700, 60)
        test_simu.check_collision()
        self.assertFalse(test_simu.awake)

if __name__ == '__main__':
    unittest.main()
