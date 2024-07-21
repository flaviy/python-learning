a_word = "polymorphism"
a_list = ["Classes", "OOP", "Polymorphism"]
a_tuple = (1, 2, 3, 80)

for element in [a_word, a_list, a_tuple]:
    print(len(element))


class Wizard():
    def attack(self):
        print("magic attack")


class Archer():
    def attack(self):
        print("shoot arrow")


class Samurai():
    def attack(self):
        print("katana attack")


for char in [Wizard(), Archer(), Samurai()]:
    char.attack()


class Character:
    weapon = 'default'

    def defend(self):
        print(self.weapon)


class Wizard(Character):
    weapon = "magic shield"


class Archer(Character):
    weapon = "duck"


class Samurai(Character):
    weapon = "block"

class SomeCreature():
    def defend(self):
        print('I am defending')


def general_defense(character: Character):
    character.defend()

general_defense(Wizard())  # magic shield
general_defense(SomeCreature())  # I am defending, because SomeCreature class has the defend method. It is not necessary to inherit from the Character class to use the general_defense function.
