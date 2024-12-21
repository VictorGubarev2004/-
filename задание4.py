import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.armor = 50
        self.stamina = 50

    def attack(self, opponent):
        if self.stamina > 0:
            damage = random.randint(10, 30) if self.stamina > 0 else random.randint(0, 10)
            opponent.take_damage(damage)
            self.stamina -= 10
            print(f"{self.name} атакует {opponent.name}, нанося {damage} урона.")
        else:
            print(f"{self.name} нет выносливости, не может атаковать.")

    def defend(self):
        print(f"{self.name} защищается.")
        return True

    def take_damage(self, damage):
        if self.armor > 0:
            armor_damage = random.randint(0, 10)
            self.armor -= armor_damage
            damage_taken = max(0, damage - armor_damage)
            self.health -= damage_taken
            print(f"{self.name} теряет {damage_taken} здоровья и {armor_damage} брони.")
        else:
            damage_taken = random.randint(10, 30)
            self.health -= damage_taken
            print(f"{self.name} без брони и теряет {damage_taken} здоровья.")

    def is_alive(self):
        return self.health > 10


def gladiator_battle(warrior1, warrior2):
    while warrior1.is_alive() and warrior2.is_alive():
        action1 = random.choice(["attack", "defend"])
        action2 = random.choice(["attack", "defend"])

        print(f"\n{warrior1.name}: {action1}, {warrior2.name}: {action2}")

        if action1 == "attack" and action2 == "attack":
            warrior1.attack(warrior2)
            warrior2.attack(warrior1)
        elif action1 == "attack" and action2 == "defend":
            warrior1.attack(warrior2)
        elif action1 == "defend" and action2 == "attack":
            warrior2.attack(warrior1)
        else:
            print("Оба воина защищаются. Никто не теряет очков.")

        print(f"{warrior1.name}: здоровье={warrior1.health}, броня={warrior1.armor}, выносливость={warrior1.stamina}")
        print(f"{warrior2.name}: здоровье={warrior2.health}, броня={warrior2.armor}, выносливость={warrior2.stamina}")

    loser = warrior1 if not warrior1.is_alive() else warrior2
    print(f"\n{loser.name} упал! Убить его? Полlice verso.")
    decision = input("Ввести 'убить' или 'пощадить': ").strip().lower()
    if decision == "убить":
        print(f"{loser.name} погиб.")
    else:
        print(f"{loser.name} не погиб.")


# Тест
warrior1 = Warrior("Гладиатор 1")
warrior2 = Warrior("Гладиатор 2")

gladiator_battle(warrior1, warrior2)
