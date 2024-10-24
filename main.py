from abc import ABC, abstractmethod
import random

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        damage = random.randint(10, 20)
        print(f"Боец атакует мечом и наносит {damage} урона!")
        return damage

class Bow(Weapon):
    def attack(self):
        damage = random.randint(5, 15)
        print(f"Боец стреляет из лука и наносит {damage} урона!")
        return damage

class Axe(Weapon):
    def attack(self):
        damage = random.randint(15, 25)
        print(f"Боец рубит топором и наносит {damage} урона!")

class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon
        self.health = 100

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print(f"{self.name} сменил оружие!")

    def attack(self, monster):
        damage = self.weapon.attack()
        monster.take_damage(damage)

class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            print(f"У монстра {self.name} осталось {self.health} здоровья!")
        else:
            print(f"Монстр {self.name} побеждён!")

def game():
    fighter = Fighter("Воин", Sword())

    monster = Monster("Гоблин", 50)

    while monster.health > 0 and fighter.health > 0:
        action = input("Выберите действие: 1 - Атака, 2 - Смена оружия: ")
        if action == "1":
            fighter.attack(monster)
        elif action == "2":
            weapon_choice = input("Выберите оружие: 1 - Меч, 2 - Лук, 3 - Топор: ")
            if weapon_choice == "1":
                fighter.change_weapon(Sword())
            elif weapon_choice == "2":
                fighter.change_weapon(Bow())
            elif weapon_choice == "3":
                fighter.change_weapon(Axe())
            else:
                print("Некорректный ввод!")

            if monster.health <= 0:
                print(f"{fighter.name} победил монстра {monster.name}!")
                break

game()                