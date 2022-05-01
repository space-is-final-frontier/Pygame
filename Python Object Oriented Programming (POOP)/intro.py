class Monster:

    #attributes (aka variables of the object defined here in the class)
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    #methods (aka functions of the object defined here in the class)
    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} damage was dealt')
        self.energy -= 20
        print(f'The energy is now {self.energy}')

    def move(self, speed):
        print(f'The monster has moved with speed of {speed}')
        

monster = Monster(40, 50)
