from src.robot import Robot 

import unittest

class TestRobot(unittest.TestCase):
    def test_robot_est_instancce_de_robot(self):
        test_robot = Robot("Dexter",50,25,0,0)
        self.assertIsInstance(test_robot, Robot)

    def test_robot_avancer(self):
        test_robot = Robot("Dexter",50,25,0,0)
        test_robot.avancer(10)
        self.assertEqual(test_robot.x, 10)
        self.assertEqual(test_robot.y, 0)

if __name__ == '__main__':
    unittest.main()
