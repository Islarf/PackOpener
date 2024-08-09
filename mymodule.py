import random

common = [0.6, "Common"]
uncommon = [0.2, "Uncommon"]
rare = [0.15, "Rare"]
mythic = [0.05, "Mythic"]
class Card:
    def rarity(self, rarity: float):
        global common
        global uncommon
        global rare
        global mythic

        for c,u,r,m in zip(common, uncommon, rare, mythic):
            if rarity <= m:
                return mythic
            elif rarity <= r:
                return rare
            elif rarity <= u:
                return uncommon
            else:
                return common

    def __init__(self, name, howrare=False):
        self.name = name
        if not howrare:
            howrare = random.uniform(0,1)
        self.rarity = self.rarity(howrare)

