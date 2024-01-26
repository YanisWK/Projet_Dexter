from Source.Robot import *
from math import *

rb = Robot(12)
print("Affichage du robot:")
print(rb)
print("\n")

print("Le robot avance de 10cm:")
rb.avancer(10)
print(rb)
print("\n")

print("Le robot tourne de 90° vers la droite et avance de 5cm:")
rb.tourner_a_droite(90)
rb.avancer(5)
print(rb)
print("\n")

print("Le robot fait un demi-tour et avance de 5cm:")
rb.tourner_a_gauche(180)
rb.avancer(5)
print(rb)
print("\n")

print("Le robot tourne à droite de 90° vers la droite et recule de 10cm:")
rb.tourner_a_droite(90)

rb = Robot(12)
print(rb)
rb.avancer(10)
print(rb)
rb.tourner_a_droite(25)
print(rb)

rb.reculer(10)
print(rb)