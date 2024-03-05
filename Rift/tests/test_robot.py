from .Dexturret.turret.robot import Robot 
from math import cos, sin, radians

import unittest

class TestRobot(unittest.TestCase):
    def test_robot_est_instancce_de_robot(self):
        test_robot = Robot("Dexter",50,25,0,0)
        self.assertIsInstance(test_robot, Robot)

    def test_robot_avancer(self):
        test_robot = Robot("Dexter",50,25,0,0)
        test_robot.avancer(10)
        self.assertEqual(test_robot.x, 0)
        self.assertEqual(test_robot.y, -10)

    def test_robot_tourner(self):
        test_robot = Robot("Dexter",50,25,0,0)
        test_robot.tourner(90)
        self.assertEqual(test_robot.direction, 180)
        test_robot.tourner(-180)
        self.assertEqual(test_robot.direction, 0)

    #def test_robot_pos_coins_Robot(self):
    #    test_robot = Robot("Dexter",50,25,0,0)
    #    test_robot.pos_coins_Robot()
    #    self.assertEqual(test_robot.coordRobot, [(25.0, 0.0), (25.0, 50.0), (-25.0, 50.0), (-25.0, 0.0)])

    def test_robot_deplacementRobot(self):  
        test_robot = Robot("Dexter",50,25,0,0)
        test_robot.deplacementRobot(1)
        self.assertEqual(test_robot.x, 0)
        self.assertEqual(test_robot.y, 0)

    def test_robot_coeff_directeur(self):
        test_robot = Robot("Dexter", 50, 25, 0, 0)
        res = test_robot.coeff_directeur(45) #angle = 45
        res_assert = (cos(radians(45)),sin(radians(45)))
        self.assertEqual(res, res_assert)

    def test_robot_detect_distance(self):
        test_robot = Robot("Dexter", 50, 25, 0, 0)
        simu_longueur = 1000
        simu_largeur = 700
        res = test_robot.detect_distance(simu_longueur, simu_largeur)
        res_assert = round(simu_longueur/2,simu_largeur/2)
        self.assertEqual(res, res_assert)

    def test_robot_set_vitesse_roue(self):
        test_robot = Robot("Dexter", 50, 25, 0, 0)
        #test roue gauche
        test_robot.set_vitesse_roue(1, 10)
        self.assertEqual(test_robot.vitesse_lineaire_roue_gauche, 10)

        #test roue droite
        test_robot.set_vitesse_roue(2, 8)
        self.assertEqual(test_robot.vitesse_lineaire_roue_droite, 8)

        #test pour les deux roues
        test_robot.set_vitesse_roue(3, 5)
        self.assertEqual(test_robot.vitesse_lineaire_roue_gauche, 5)
        self.assertEqual(test_robot.vitesse_lineaire_roue_droite, 5)

    if __name__ == '__main__':
        unittest.main()