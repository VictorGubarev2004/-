import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, opponent):
        """Уменьшает здоровье противника на 20 очков."""
        opponent.health -= 20
        print(f"{self.name} атаковал {opponent.name}. У {opponent.name} осталось {opponent.health} здоровья.")

warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

while True:
    attacker, defender = (warrior1, warrior2) if random.choice([True, False]) else (warrior2, warrior1)
    attacker.attack(defender)

    if defender.health <= 0:
        print(f"{defender.name} погиб в бою! Победил {attacker.name}.")
        break