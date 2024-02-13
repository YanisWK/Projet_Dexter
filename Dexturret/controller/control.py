update_time=60


class Avancer():
    def __init__(self,distance):
        self.distance=distance
    def start(self):
        self.parcouru=0
    def etape(self):
        self.parcouru+=self.distance #il me faudrait la distance parcouru poure chaque etapes ou j'ai juste mal compris peut être la distance parcouru par le robot d'ailleurs
        if self.stop() : return
    def stop(self):
        return self.parcouru>self.distance
    

class Tourner():
    def __init__(self,angle):
        self.angle=angle
    def start(self):
        self.angle_parcouru=0
    def etape(self):
        self.angle_parcouru+=self.angle 
        if self.stop(): return
    def stop(self):
        return self.angle_parcouru>self.angle
    

class TracerCarre():
    def __init__(self,tailleCote):
        stratAvancer=Avancer(tailleCote)
        stratTourner=Tourner(tailleCote)
        self.strats=[stratAvancer,stratTourner]
        self.tailleCote=tailleCote
        self.current=-1
    def start(self):
        self.current=-1
    def etape(self):
        if self.stop():return
        if self.current<0 or self.strats[self.current].stop():
        self.current+=1
        self.strats[current].start()
        self.strat

    def stop(self):
        return self.current==len(self.starts)-1 and self.strats[self.current].stop()
