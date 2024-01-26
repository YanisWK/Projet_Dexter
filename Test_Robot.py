from Robot import *
<<<<<<< HEAD

=======
>>>>>>> fedd047aa38d3cd32a4f5c07865148b5c238fff6
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
<<<<<<< HEAD

rb = Robot(12)
print(rb)
rb.avancer(10)
print(rb)
rb.tourner_a_droite(25)
print(rb)

=======
>>>>>>> fedd047aa38d3cd32a4f5c07865148b5c238fff6
rb.reculer(10)
print(rb)