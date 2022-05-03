#A function is just an object with the dunder call method

'''
def test():
    pass

a = test

print(dir(a))
print(dir(test)))
'''

#These two print statement will give the same output as we stored the test object into variable a turning a into an object

#We can place functions as arguemnts for objects

'''
def add(a, b):
    return a + b

class Test:
    def __init__(self, add_func):
        self.add_function = add_func

test = Test(add)
print(test.add_function(1, 5))'''


#We can place methods as arguments for objects

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