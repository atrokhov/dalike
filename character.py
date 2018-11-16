class Character:

    def __init__(self, name, race, char_class, strength, dexterity, willpower, magic, cunning, constitution, health, stamina, attack_score, defense_score):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.strength = strength
        self.dexterity = dexterity
        self.willpower = willpower
        self.magic = magic
        self.cunning = cunning
        self.constitution = constitution
        self.xp = 0
        self.level = 1
        self.gold = 0
        self.health = health
        self.stamina = stamina
        self.attack_score = attack_score
        self.defense_score = defense_score
        self.inventory = []
        self.skills = []
        self.abilities = []
        self.spells = []
        self.journal = []
        