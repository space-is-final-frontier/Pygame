'''Example how we can place functions as arguemnts for objects

def add(a, b):
    return a + b

class Test:
    def __init__(self, add_func):
        self.add_function = add_func

test = Test(add)
print(test.add_function(1, 5))'''


#Example of placing methods as arguments for objects

class Monster:
    def __init__(self, func):
        self.func = func

class Attacks:
    def bite(self):
        print("BITE")

    def strike(self):
        print("STRIKE")

    def slash(self):
        print("SLASH")

    def kick(self):
        print("KICK")

monster = Monster(Attacks().bite)
monster.func()