class Robot:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return "C'est le robot d'identifiant " + str(self.id)