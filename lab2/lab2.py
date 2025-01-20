import random
def game():
    weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
    try:
        combatStrength = int(input("Enter your combat Strength: "))
        mCombatStrength = int(input("Enter the monster's combat Strength: "))
    except ValueError:
        print("Invalid input! Combat strengths must be integers.")
        return
    try:
        weaponRoll = int(input("Roll the dice for your weapon (Enter a number between 1-6): "))
        if weaponRoll < 1 or weaponRoll > 6:
            print("Error: Dice roll must be between 1 and 6.")
            return
    except ValueError:
        print("Invalid input! Please enter an integer between 1 and 6.")
        return
    heroWeapon = weapons[weaponRoll - 1]
    print(f"You rolled a {weaponRoll}, and your weapon is: {heroWeapon}")
    combatStrength += weaponRoll
    print(f"Your updated combat strength is: {combatStrength}")
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")
    if heroWeapon != "Fist":
        print("Thank goodness you didn't roll the Fist.")
    input("Roll the dice for your health points (Press enter)")
    healthPoints = random.randint(1, 6)
    print(f"You rolled {healthPoints} health points.")
    input("Roll the dice for the monster's health points (Press enter)")
    mHealthPoints = random.randint(1, 6)
    print(f"The monster rolled {mHealthPoints} health points.")
    input("Roll the dice to see if you find a healing potion (Press enter)")
    healingPotion = random.choice([0, 1])
    print(f"Have you found a healing potion?: {bool(healingPotion)}")
    matchedStrength = combatStrength == mCombatStrength
    print("--- You are matched in strength: " + str(matchedStrength))
    strongPlayer = (combatStrength + healthPoints) >= 15
    print("--- You have a strong player: " + str(strongPlayer))
    shouldTakePotion = healingPotion == 1 and healthPoints <= 6
    print("--- Remember to take a healing potion!: " + str(shouldTakePotion))
    hasHealingPotion = not (healthPoints < mCombatStrength and healingPotion == 1)
    print("--- Phew, you have a healing potion: " + str(hasHealingPotion))
    dangerousSituation = healingPotion == 0 or healthPoints == 1
    print("--- Things are getting dangerous: " + str(dangerousSituation))
    if healthPoints >= 5:
        print("--- Your health is ok")
    elif healingPotion == 1:
        healingPotion = 0
        healthPoints = 6
        print("--- Using your healing potion... Your Health Points are now full at", healthPoints)
    else:
        print(f"--- Your health is low at {healthPoints}, and you have no healing potions available!")
    print("You meet the monster. FIGHT!!")
    input("You strike first (Press enter)")
    print(f"Your sword ({combatStrength}) ---> Monster ({mHealthPoints})")
    if combatStrength >= mHealthPoints:
        print("You've killed the monster")
    else:
        mHealthPoints -= combatStrength
        print(f"You've reduced the monster's health to: {mHealthPoints}")
        print("The monster strikes!!!")
        print(f"Monster's Claw ({mCombatStrength}) ---> You ({healthPoints})")
        if mCombatStrength >= healthPoints:
            print("You're dead")
        else:
            healthPoints -= mCombatStrength
            print(f"The monster has reduced your health to: {healthPoints}")
game()
