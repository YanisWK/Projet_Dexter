import sys
sys.path.append("..")
from Source.Robot import Robot

import unittest

class TestRobot(unittest.TestCase):
    def test_robot_est_instancce_de_robot(self):
        robot = Robot()
        self.assertIsInstance(robot, Robot)

    def test_robot_avancer(self):
        robot = Robot()
        robot.avancer(10)
        self.assertEqual(robot.getX(), 10)
        self.assertEqual(robot.getY(), 0)
