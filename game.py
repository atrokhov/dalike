from character import *
from variables import races, char_classes

def choice(items):
    nums = ''
    i = 0
    for item in items:
        i += 1
        num = str(i) + '. ' + item.name + '\n'
        nums += num
    return nums

def level_up(hero):
    if hero.char_class.name == "Воин":
        hero.health += 6
        hero.stamina += 5
    elif hero.char_class.name == "Разбойник":
        hero.health += 5
        hero.stamina += 4
    else:
        hero.health += 4
        hero.stamina += 6
    hero.level += 1

def hero_stats(hero):
    name = 'Имя: ' + str(hero.name) + '\n'
    race = 'Раса: ' + str(hero.race.name) + '\n'
    char_class = 'Класс: ' + str(hero.char_class.name) + '\n'
    level = 'Уровень: ' + str(hero.level) + '\n'
    health = 'Здоровье: ' + str(hero.health) + '\n'
    if hero.char_class.name == 'Маг':
        stamina = 'Мана: ' + str(hero.stamina) + '\n'
    else:
        stamina = 'Выносливость: ' + str(hero.stamina) + '\n'
    xp = 'Опыт:' + str(hero.xp) + '\n'
    strength = 'Сила: ' + str(hero.strength) + '\n'
    dexterity = 'Ловкость: ' + str(hero.dexterity) + '\n'
    willpower = 'Сила воли: ' + str(hero.willpower) + '\n'
    magic = 'Магия: ' + str(hero.magic) + '\n'
    cunning = 'Хитрость: ' + str(hero.cunning) + '\n'
    constitution = 'Телосложение: ' + str(hero.constitution)
    return name + race + char_class + level + health + stamina + xp + strength + dexterity + willpower + magic + cunning + constitution

name = input("Введите имя: ")

print("Выберите расу:")
print(choice(races))
race_num = input("Введите число: ")
race = races[int(race_num) - 1]

print("Выберите класс: ")
print(choice(char_classes))
class_num = input("Введите число: ")
char_class = char_classes[int(class_num) - 1]

strength = 10 + race.strength + char_class.strength
dexterity = 10 + race.dexterity + char_class.dexterity
willpower = 10 + race.willpower + char_class.willpower
magic = 10 + race.magic + char_class.magic
cunning = 10 + race.cunning + char_class.cunning
constitution = 10 + race.constitution + char_class.constitution

health = char_class.health
stamina = char_class.stamina
attack_score = char_class.attack_score
defense_score = char_class.defense_score

hero = Character(name, race, char_class, strength=strength, dexterity=dexterity, willpower=willpower, magic=magic, cunning=cunning, constitution=constitution, health=health, stamina=stamina, attack_score=attack_score, defense_score=defense_score)

print(hero_stats(hero))

level_up(hero)

print(hero_stats(hero))

