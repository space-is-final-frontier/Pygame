def update_health(amount):
    health += amount

health = 10
print(health)
update_health(20)
print(health)


class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)

class Monster:
    def __init__(self, health):
        self.health = health

    def get_damage(self, amount):
        self.health -= amount

monster = Monster(100)
hero = Hero(20, monster)

hero.attack()
print(monster.health)