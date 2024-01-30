"""Documentation : """

class Environnement : 

    def __init__(self,id,longueur,largeur):
        self.id=id
        self.longueur=longueur
        self.largeur=largeur
    


    def setHandL(self,lo,la):
        self.longueur=lo
        self.largeur=la

    
    def getLo(self):
        return self.longueur
    def getLa(self):
        return self.largeur
        

    

