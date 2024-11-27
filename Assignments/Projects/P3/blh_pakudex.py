from blh_pakuri import *


class Pakudex:

    def __init__(self, capacity=20):
        self.capacity = capacity
        self.size = 0
        self.my_pakudex = []

    @property
    def get_size(self):
        return self.size

    @property
    def get_capacity(self):
        return self.capacity

    @property
    def get_species_array(self):
        if self.get_size == 0:
            return None
        return [p.get_species for p in self.my_pakudex]

    def get_stats(self,species):
        for p in self.my_pakudex:
            if p.get_species == species:
                return [p.get_attack, p.get_defense, p.get_speed]
        return None

    def sort_pakuri(self):
        # self.my_pakudex.sort()
        self.my_pakudex.sort(key = lambda p: p.get_species)

    def add_pakuri(self,species):
        if self.size == self.capacity:
            return False
        for p in self.my_pakudex:
            if p.get_species == species:
                return False

        self.my_pakudex.append(Pakuri(species))
        self.size += 1
        return True

    def evolve_species(self,species):
        for p in self.my_pakudex:
            if p.get_species == species:
                p.evolve()
                return True
        return False





