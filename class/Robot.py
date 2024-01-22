class Robot:
    vitesses
    position
    temps
    def __init__(self,vitesses,position) -> None:
        self.vitesses = vitesses
        self.position = position
    
    def avancer(self,temps):
        self.position = self.position + self.vitesses*temps