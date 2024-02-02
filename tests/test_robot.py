from src.robot import Robot 

import unittest

class TestRobot(unittest.TestCase):
    def test_robot_est_instancce_de_robot(self):
        robot = Robot("Dexter",50,25,0,0)
        self.assertIsInstance(robot, Robot)

    def test_robot_avancer(self):
        robot = Robot("Dexter",50,25,0,0)
        robot.avancer(10)
        self.assertEqual(robot.getX(), 10)
        self.assertEqual(robot.getY(), 0)

if __name__ == '__main__':
    unittest.main()
