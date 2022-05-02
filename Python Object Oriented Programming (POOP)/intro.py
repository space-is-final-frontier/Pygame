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

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')
        

monster = Monster(40, 50)
