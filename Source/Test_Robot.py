from Robot import *
from math import *

rb = Robot(12, 20, 10)
print("Affichage du robot:")
print(rb)
print("\n")

print("Le robot avance de 10cm:")
rb.avancer(10)
print(rb)
print("\n")

print("Le robot tourne de 90° vers la droite et avance de 5cm:")
rb.tourner(-90)
rb.avancer(5)
print(rb)
print("\n")

print("Le robot fait un demi-tour et avance de 5cm:")
rb.tourner(180)
rb.avancer(5)
print(rb)
print("\n")

print("Le robot tourne à droite de 90° vers la droite et recule de 10cm:")
rb.tourner(-90)
rb.avancer(-10)
print(rb)