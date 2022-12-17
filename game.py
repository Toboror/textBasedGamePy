
# Create a weapon class where you can specify a weapons damage and name
class weapon:
    def __init__(self, weapon, damage):
        self.weapon_name = weapon
        self.damage = damage

    def returnName(self):
        return self.weapon_name


# Melee category and range category, but not sure if to implement
class melee(weapon):
    def __init__(self, weapon):
        super.__init__(weapon, 25)
        self.range = 1
        self.health = 100

    def functions(self):
        return weapon.returnName()



# Person class which every person should inherit,
class person:

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


# Pimp with an example of how a class which inherits should look maybe?
class pimp(person):
    def __init__(self, name, age, weight, height):
        super.__init__(name,age, weight, height)
        self.weapon = "Melee"



#class mainCharacter:

#class salesWoman:

