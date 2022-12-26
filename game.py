# Difficulties so far, marked with stars for how difficult
# How do we make the player move around the grid?** fixed: new problem, movement has to be disturbed by enter
# Possibly make the game slow paced?
# Create a nice display for in game inventory and stats while game is playing.
# Consider implementing a GUI since this is so frustrating
# Add level class maybe?



from random import randrange
import os

    # Creating graphicaldisplay of game, starting with whitespace, maybe a special symbol in future?

    # test 2

    #test 3

#class UI():

class weapon:
    def __init__(self, weapon, damage, range, price):
        self.weapon_name = weapon
        self.damage = damage
        self.range = range
        self.price = price

    def returnName(self):
        return self.weapon_name

    def returnDamage(self):
        return self.damage


# Melee category for melee weapons.
class melee(weapon):
    def __init__(self, weaponName):
        super().__init__(weaponName, 25, 1, 10)
        self.health = 100
        self.upgradeCost = 20

    def functions(self):
        return weapon.returnName()

    def getUpgradeCost(self):
        return self.upgradeCost

    def upgradeWeapon(self):
        self.damage += 5
        self.range += 2
        self.health += 15



    def useWeapon(self):
        self.health -= 5


# Take in a dictionary where weapons are chosen randomly and the damage is value assigned to chosen key.
class ranged(weapon):
    def __init__(self, weaponList):
        randomlyChosen = randrange(0, len(weaponList))
        super().__init__(weaponList[randomlyChosen][0], weaponList[randomlyChosen][1], weaponList[randomlyChosen][2],
                         weaponList[randomlyChosen][4])
        self.fireRate = weaponList[randomlyChosen][3]
        self.ammo = 100
        self.magazine = 10

    def upgradeWeapon(self):
        self.fireRate *= 1.3
        self.damage *= 1.2
        self.range *= 1.2

        # Return true if user can use weapon, return false if not.
    def useWeapon(self):
        self.magazine -= 1
        if self.magazine == 0:
            # Figure out where to print this
            print("Reloading...")
            self.magazine = 10
            if self.ammo < 10:
                return False
            self.ammo -= 10
            return True

    def __str__(self):
        return "Damage:" + self.damage + "\n" + "Range:" + self.range + "\n" + "Firerate:" + self.fireRate + "\n" + \
               "Magazine:" + self.magazine



# Person class which every person should inherit,
class person:

    def __init__(self, name, age, weight, height, health):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.health = health
        self.alive = True

# Pimp with an example of how a class which inherits should look maybe?
class pimp(person):
    def __init__(self, name):
        super().__init__(name, randrange(30, 50), randrange(70, 120), randrange(170, 200), 100)
        self.money = 1000

# Main character class, starts out with a knife as weapon

class mainCharacter(person):
    def __init__(self, name):
        super().__init__(name, randrange(16, 30), randrange(50, 100), randrange(140, 210), 100)
        self.money = 100
        self.weapons = [melee("knife")]
        self.col = 5
        self.row = 5

    def eatCheap(self):
        if self.money >= 2:
            self.money -= 2
            self.heal(2)

    def heal(self, amount):
        for i in range(amount):
            if (self.health + amount) > 100:
                break
            self.health += 1

    # Considering printing in method, but maybe a work around where the stat is always displayed and updated on screen?

    def weightGain(self, amount):
        self.weight += amount

    # Boolean return maybe??
    def buy(self, amount):
        if self.money >= amount:
            self.money -= amount
            return True
        print("You're too broke.")
        return False

    # View weapons and upgrade possibilities

    def viewWeapons(self):
        counter = 0
        for weapon in self.weapons:
            print(counter)
            weapon.returnName()
            counter += 1
        choice = input("Do you wanna upgrade your weapons? y for yes, n for no")
        if choice == "y":
            choice = input("Which weapon? type the number")
            self.weapons[choice].upgradeWeapon()
            if (self.buy(self.weapons[choice].getUpgradeCost())):
                print("You upgraded", self.weapons[choice], "The new stats are", )

# To add fight mechanic


class salesWoman:
    def __init__(self, name):
        super().__init__(name, randrange(20, 70), randrange(50, 140), randrange(130, 180), 100)
        self.STDstatus = False
        self.money = 20


# Considered Dict, chose 2d list with weapon name, damage, range, fire rate and price, feel free to add more
weapons = [["AK47", 25, 50, 50, 70], ["SCAR", 30, 50, 40, 100], ["Uzi",20, 30, 70, 100]]

player = mainCharacter("Daniel")
gui = graphicalDisplay(player)
gui.printGrid()
gui.menu()
gui.printGrid()
