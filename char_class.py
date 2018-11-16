class CharClass:
    def __init__(self, name, description, health, stamina, attack_score, defense_score, strength=0, dexterity=0, willpower=0, magic=0, cunning=0, constitution=0):
        self.name = name
        self.description = description
        self.strength = strength
        self.dexterity = dexterity
        self.willpower = willpower
        self.magic = magic
        self.cunning = cunning
        self.constitution = constitution
        # self.skills = skills
        # self.spells = spells
        self.health = health
        self.stamina = stamina
        self.attack_score = attack_score
        self.defense_score = defense_score