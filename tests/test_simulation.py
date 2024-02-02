from src.simulation import Simulation
from src.robot import Robot

import unittest

class TestSimulation(unittest.TestCase):
    def test_simulation_est_instancce_de_simulation(self):
        robot = Robot("Dexter",50,25,0,0)
        simulation = Simulation(1,robot,1000,700,60)
        self.assertIsInstance(simulation, Simulation)