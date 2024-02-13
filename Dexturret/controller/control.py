class Avancer():
    def __init__(self,distance):
        self.distance=distance
        
    def start(self):
        self.parcouru=0
    def etape(self):
        self.parcouru+=self.distance #il me faudrait la distance parcouru toute les x etapes ou j'ai juste mal compris
     

class Tourner():
    def __init__(self,angle):
        self.angle=angle

class DeplacerVers():
    def __init__(self,x,y):
        self.x=x
        self.y=y
class TracerCarre():
    def __init__(self,distance):
        self.distance=distance

