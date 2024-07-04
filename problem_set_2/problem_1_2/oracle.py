class Oracle:
    """L'oracle de l'énoncé..."""
    def __init__(self, k=0):
        self.stone_planet_index = None
        self.reset_oracle(k)

    def oracle(self, current_planet):
        """Retourne True si la pierre se trouve sur une planète dont le numéro est strictement plus grand que n"""
        return current_planet < self.stone_planet_index

    def reset_oracle(self, new_planet_index):
        """Permet de déplacer la pierre sur une autre "planète"..."""
        self.stone_planet_index = new_planet_index