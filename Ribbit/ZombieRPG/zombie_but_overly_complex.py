# John Bowie
# 10/21/22
# zombie fighter

from random import randint, randrange
from time import sleep



def space(x):
    sleep(x)
    print(" \n ")



# count of zombies 
zomb_count = randint(1,100)

# Intro
print("Welcome survivor to the zombie apocalypse the road to saftey is full of zombies")
space(1)
dead = False
hits = 3

# BILL
found = False

choice = input("Oh No! A zombie horde shambles up to you what do you want to do? \n1. Run \n2. Fight \nEnter your choice: ").title()
if choice == "Run" or choice == "1":
    success_chance = randint(0,100)
    if success_chance <= 50:
        success = randint(1,15)
        zomb_count -= success
        print(f"You managed to run away from {success} zombies")
        print(f"There is {zomb_count} zombies left in the horde")
    else:
        print("You werent able to run away you got hit 2/3 hits left")
        hits -= 1
 




print("You have a few weapons at your desposal choose one from this list:")
space(2)

#durabilities
sgd = 2
cbd = 5
ad = 4
bbd = 3
kd = 5
hgd = 3
md = 4
shd = 5
hd = 4
csd = 4

weapons = (f"""Shotgun, Durability: {sgd}
    Crossbow, Durability: {cbd}
    Axe, Durability: {ad}
    Baseball Bat, Durability: {bbd}
    Katana, Durability: {kd}
    Handgun, Durability: {hgd}
    Machete, Durability: {md}
    Sledge Hammer, Durability: {shd}
    Hatchet, Durability: {hd}
    Cleaving Saw, Durability: {csd}
""")
print(weapons)
while zomb_count > 0 and dead == False:
    choice_1 = input("Options: \n1. Choose Weapon. \n2. Search For Ammo. \n3. Search For Companion.").title()
    # Live Counter
    if hits <= 1:
        dead = True
    if choice_1 == "2" or choice_1 == "Search For Ammo":
        pass
        luck = randint(1,100)
        if luck <= 50:
            sgd += randint(0,2)
            cbd += randint(0,5)
            ad += randint(0,4)
            bbd += randint(0,3)
            kd += randint(0,5)
            hgd += randint(0,3)
            md += randint(0,4)
            shd += randint(0,5)
            hd += randint(0,4)
            csd += randint(0,4)
            
    elif choice_1 == "3" or choice_1 == "Search For Companion":
        find_chance = randint(1,100)
        if find_chance <= 25:
            found = True
            print("Thanks for saving me! My name is bill")
            print("I'll help you from now on")
    elif choice_1 == "1" or choice_1 == "Choose Weapon":
        choice = input("Choose your weapon")
 
# SHOTGUN
    if choice == "Shotgun" and sgd > 0:
        killed = randint(2,5)
        print(f"You have killed, {killed} zombies")
        zomb_count -= killed
        print(f"There are {zomb_count} left")
        sgd -= 1
        print(f"{sgd}/2 remaning")
    elif choice == "Shotgun" and sgd == 0:
        print("The Shotgun ran out of ammo, you dont kill any zombies")
        print(f"There are {zomb_count} left")
        hits -= 1
        print(f"Oh No! a zombie bit you, you have {hits}/3 health left")

# CROSSBOW
    if choice == "Crossbow" and cbd > 0:
        killed = randint(0,2)
        print(f"You have killed, {killed} zombies")
        zomb_count -= killed
        print(f"There are {zomb_count} left")
        cbd -= 1
        chance = randint(0,100)
        if zomb_count > 25 and chance < 75:
            print("You manage to grab the arrow")
            cbd += 1 
        print(f"{cbd}/5 remaning")
    elif choice == "Crossbow" and cbd == 0:
        print("The Crossbow ran out of ammo, you dont kill any zombies")
        print(f"There are {zomb_count} left")
        hits -= 1
        print(f"Oh No! a zombie bit you, you have {hits}/3 health left")
    
# AXE
    if choice == "Axe" and ad > 0:
        killed = randint(0,1)
        print(f"You have killed, {killed} zombies")
        zomb_count -= killed
        print(f"There are {zomb_count} left")
        ad - 1
        print(f"{ad}/4 remaning")
    elif choice == "Axe" and ad == 0:
        print("The Axe broke, you dont kill any zombies")
        print(f"There are {zomb_count} left")
        hits -= 1
        print(f"Oh No! a zombie bit you, you have {hits}/3 health left")

# KATANA
    if choice == "Katana" and kd > 0:
        killed = randint(1,3)
        print(f"You have killed, {killed} zombies")
        zomb_count -= killed
        print(f"There are {zomb_count} left")
        kd -= 1
        print(f"{kd}/5 remaning")
    elif choice == "Katana" and kd == 0:
        print("The katana broke, you dont kill any zombies")
        print(f"There are {zomb_count} left")
        hits -= 1
        print(f"Oh No! a zombie bit you, you have {hits}/3 health left")
    
# HANDGUN
    if choice == "Handgun" and hgd > 0:
        killed = randint(0,5)
        print(f"You have killed, {killed} zombies")
        zomb_count -= killed
        print(f"There are {zomb_count} left")
        hgd -= 1
        print(f"{hgd}/3 remaning")
    elif choice == "Handgun" and hgd == 0:
        print("The Handgun ran out of ammo, you dont kill any zombies")
        print(f"There are {zomb_count} left")
        hits -= 1
        print(f"Oh No! a zombie bit you, you have {hits}/3 health left")
    
# MACHETE
    if choice == "Machete" and md > 0:
        killed = randint(0,1)
        print(f"You have killed, {killed} zombies")
        zomb_count -= killed
        print(f"There are {zomb_count} left")
        md -= 1
        print(f"{md}/4 remaning")
    elif choice == "Machete" and md == 0:
        print("The Machete broke, you dont kill any zombies")
        print(f"There are {zomb_count} left")
        hits -= 1
        print(f"Oh No! a zombie bit you, you have {hits}/3 health left")

# Sledge Hammer
    if choice == "Sledge Hammer" and shd > 0:
        killed = randint(0,2)
        print(f"You have killed, {killed} zombies")
        zomb_count -= killed
        print(f"There are {zomb_count} left")
        shd -= 1
        print(f"{shd}/5 remaning")
    elif choice == "Sledge Hammer" and shd == 0:
        print("The Sledge Hammer broke, you dont kill any zombies")
        print(f"There are {zomb_count} left")
        hits -= 1
        print(f"Oh No! a zombie bit you, you have {hits}/3 health left")

# Hatchet
    if choice == "Hatchet" and hd > 0:
        killed = randint(1,2)
        print(f"You have killed, {killed} zombies")
        zomb_count -= killed
        print(f"There are {zomb_count} left")
        hd -= 1
        print(f"{hd}/4 remaning")
    elif choice == "Hatchet" and hd == 0:
        print("The Hatchet broke, you dont kill any zombies")
        print(f"There are {zomb_count} left")
        hits -= 1
        print(f"Oh No! a zombie bit you, you have {hits}/3 health left")

# Cleaving Saw
    if choice == "Cleaving Saw" and csd > 0:
        killed = randint(1,2)
        print(f"You have killed, {killed} zombies")
        zomb_count -= killed
        print(f"There are {zomb_count} left")
        csd -= 1
        print(f"{csd}/4 remaning")
    elif choice == "Cleaving Saw" and csd == 0:
        print("The Cleaving Saw broke, you dont kill any zombies")
        print(f"There are {zomb_count} left")
        hits -= 1
        print(f"Oh No! a zombie bit you, you have {hits}/3 health left")

# "BRIMMING CONFIDENCE" (hidden)
    if choice == "Brimming Confidence":
        killed = zomb_count
        print(f"You have somehow... convinced the zombies to kill each other, {killed} zombies were killed by their comrades.")
        zomb_count -= killed

# BILL COMBAT
    if found == True:
        shot = randint(1,100)
        if shot <= 10:
            killed = randint(5,15)
            zomb_count -= killed
            print(f"Bill killed {killed} zombies.")
        else:
            print("Bill wasnt able to kill any zombies")
        

