import unittest

class TestRobot(unittest.TestCase):
    def test_robot_est_instancce_de_robot(self):
        robot = Robot()
        self.assertIsInstance(robot, Robot)