# Note on colors: ANSI doesn't work in windows terminal anymore, so I'd have to make a tkinter version at some point.
import random

# TODO: clean up the code.  Possibly compress variables into lists.
# TODO: add a "punching bag" character with a lot of health so that I can test things better.
# TODO: fix the 's in instances of a name ending with an S.
# TODO: make the elements relevant.

# one dueler per weapon type
# Tidus
gen_1 = {"name" : "Tidus", "weapon" : "1h", "wname" : "Brotherhood, the blue steel sword", "element" : "water", "health" : 100, "warcry" : "\"To Zanarkand!\"", "traits" : "pretty"}

# Auron
gen_2 = {"name" : "Auron", "weapon" : "2h", "wname" : "a katana", "element": "fire", "health" : 100, "warcry" : "\"No more!\"", "traits" : "missing eye, dueling expert"}

# Jecht
gen_3 = {"name" : "Jecht", "weapon" : "gl", "wname" : "a glaive called Breaker", "element" : "green", "health" : 100, "warcry" : "\"I'm the best!\"", "traits" : "grotesque"}

dict_of_gens = []
dict_of_gens.append(gen_1)
dict_of_gens.append(gen_2)
dict_of_gens.append(gen_3)

print("Duelist 1: ", gen_1["name"], ", wielding ", gen_1["wname"], ".\n",
      "Duelist 2: ", gen_2["name"], ", wielding ", gen_2["wname"], ".\n",
      "Duelist 3: ", gen_3["name"], ", wielding ", gen_3["wname"], ".\n",
      sep="")

# list of accessible duelists and assassins
duelists = gen_1["name"], gen_2["name"], gen_3["name"]

# choosing duelist names
while 1:
#print("Duelists and Assassins available: %s, %s" % duelists) #requires precise indication of the number of duelists, not flexible enough
    print("Duelists and Assassins available:", ', '.join(duelists)) #this works much better!
    first_duelist = input("Choose a first duelist from the list: ")
    if first_duelist in duelists:
        print("First duelist: ", first_duelist, "!", sep="")
        for k in dict_of_gens:  # for other modifiers, an x in y format should work.
            if k['name'] == first_duelist:
                warcry_1 = k['warcry']
                print(warcry_1, "\n")
        break
    else:
        print("That duelist is not available.\n")

while 2: # currently duelists can play against each other, I'll want to fix that later.
    second_duelist = input("Choose a second duelist from the list: ")
    if second_duelist in duelists:
        print("Second duelist: ", second_duelist, "!", sep="")
        for k in dict_of_gens:  # for other modifiers, an x in y format should work.
            if k['name'] == second_duelist:
                warcry_2 = k['warcry']
                print(warcry_2, "\n")
        break
    else:
        print("That duelist is not available.\n")

first_health = 100
second_health = 100
# use this to set health later on.
#    if k['name'] == first_duelist:
#        first_health = k['health] ???
#    if k['name'] == second_duelist:
#        first_health = k['health] ???

for k in dict_of_gens: # for other modifiers, an x in y format should work.
    if k['name'] == first_duelist:
        first_weapon = k['weapon']
    if k['name'] == second_duelist:
        second_weapon = k['weapon']

# Setting weapon bonuses.
first_bonus = 0
second_bonus = 0
# if first_weapon == "1h" and second_weapon == "1h": #no advantage
if first_weapon == "1h" and second_weapon == "2h":
    second_bonus += 6
    print(second_duelist, "'s two-handed sword grants him an advantage over ", first_duelist, "!" ,sep="")
    w_msg1 = "tries to block"
    w_msg2 = "'s two-handed sword with his shield and gets knocked several feet across the sand for his effort."
if first_weapon == "1h" and second_weapon == "gl":
    first_bonus += 6
    print(first_duelist, "'s sword and shield gives him a maneuverability advantage over ", second_duelist, "'s glaive!", sep="")
    w_msg1 = "uses his shield to press past the guard of"
    w_msg2 = "'s glaive, driving his sword deeply into his foe."

if first_weapon == "2h" and second_weapon == "1h":
    first_bonus += 6
    print(first_duelist, "'s two-handed sword grants him an advantage over ", second_duelist, "!", sep="")
    w_msg1 = "tries to block"
    w_msg2 = "'s two-handed sword with his shield and gets knocked several feet across the sand for his effort."
#if first_weapon == "2h" and second_weapon == "2h": # no advantage
if first_weapon == "2h" and second_weapon == "gl":
    second_bonus += 6
    print(second_duelist, "'s glaive has more reach than ", first_duelist, "'s two-handed sword!", sep="")
    w_msg1 = "'s glaive has more reach than"
    w_msg2 = "'s two-handed sword and this lets him strike at his foe's hands and arms with impunity."

if first_weapon == "gl" and second_weapon == "1h":
    second_bonus += 6
    print(second_duelist, "'s sword and shield gives him a maneuverability advantage over ", first_duelist,"'s glaive!", sep="")
    w_msg1 = "uses his shield to press past the guard of"
    w_msg2 = "'s glaive, driving his sword deeply into his foe."
if first_weapon == "gl" and second_weapon == "2h":
    first_bonus += 6
    print(first_duelist, "'s glaive has more reach than ", second_duelist, "'s two-handed sword!", sep="")
    w_msg1 = "'s glaive has more reach than"
    w_msg2 = "'s two-handed sword and this lets him strike at his foe's hands and arms with impunity."
#if first_weapon == "gl" and second_weapon == "gl": #no advantage


# Fumble variables
first_fumble = " stumbles!"
second_fumble = " stumbles!"
will_fumble1 = 0
will_fumble2 = 0

# Trait checking
for k in dict_of_gens:  # for other modifiers, an x in y format should work.
    if k['name'] == first_duelist:
        if "pretty" in k['traits']:
            first_bonus -= 1
            first_fumble = "'s pretty face amuses his enemy!"
        if "missing eye" in k['traits']:
            first_bonus -= 3
            first_fumble = " swivels his head at odd angles to keep his opponent within his field of vision."
        if "dueling expert" in k['traits']:
            first_bonus += 6
        if "grotesque" in k['traits']:
            first_bonus += 1

    if k['name'] == second_duelist:
        if "pretty" in k['traits']:
            second_bonus -= 1
            second_fumble = "'s pretty face amuses his foe!"
        if "missing eye" in k['traits']:
            second_bonus -= 3
            second_fumble = " swivels his head at odd angles to keep his opponent within his field of vision."
        if "dueling expert" \
           "" in k['traits']:
            second_bonus += 6
        if "grotesque" in k['traits']:
            second_bonus += 1

# This is a little messy but works for now, yet it would interfere with references in a more expanded game (and not make much sense).
if first_duelist == second_duelist:
    second_duelist = ' '.join(["Dark", first_duelist])
    print("An evil version of", first_duelist, "emerges from the shadows!")

print(first_duelist, " bonus: ", first_bonus, ", ", second_duelist, " bonus: ", second_bonus, ".", sep="")

first_roll = 1
second_roll = 1
winner = 1
canwarcry1 = 0
canwarcry2 = 0
warcrybonus_1 = 0
warcrybonus_2 = 0
#first dice roll
d50 = (random.randrange(1,51)) #follows a common python format where it isn't inclusive of the last value
def dice():
    global first_roll
    global second_roll
    global d50
    global winner
    global canwarcry1
    global canwarcry2
    global warcrybonus_1
    global warcrybonus_2
    global will_fumble1
    global will_fumble2
    first_roll = (random.randrange(1,51)) + first_bonus #follows a common python format where it isn't inclusive of the last value
    if warcrybonus_1 == 1:
        first_roll += 10
        warcrybonus_1 = 0
    if first_roll > 44:
        canwarcry1 = 1
    if first_roll < 6:
        will_fumble1 = 1
    second_roll = (random.randrange(1, 51)) + second_bonus #follows a common python format where it isn't inclusive of the last value
    if warcrybonus_2 == 1:
        second_roll += 10
        warcrybonus_2 = 0
    if second_roll > 44:
        canwarcry2 = 1
    if second_roll < 6:
        will_fumble2 = 1
    print(first_duelist, "roll:", first_roll, second_duelist, "roll:", second_roll)
    if first_roll > second_roll:
        d50 = first_roll - second_roll
        winner = 1
    elif second_roll > first_roll:
        d50 = second_roll - first_roll
        winner = 2
    else:
        winner = 3

def battle_msg():
    global canwarcry1
    global canwarcry2
    global warcrybonus_1
    global warcrybonus_2
    global will_fumble1
    global will_fumble2

    if canwarcry1 == 1:
        print(first_duelist, "'s eyes fill with fury as he shouts: ", warcry_1, sep="")
        warcrybonus_1 = 1
        canwarcry1 = 0
    if will_fumble1 == 1:
        print(first_duelist, first_fumble, sep="")
        will_fumble1 = 0

    if canwarcry2 == 1:
        print(second_duelist, "'s eyes fill with fury as he shouts: ", warcry_2, sep="")
        warcrybonus_2 = 1
        canwarcry2 = 0
    if will_fumble2 == 1:
        print(second_duelist, second_fumble, sep="")
        will_fumble2 = 0

    if winner == 1:
        if d50 > 30:
            if first_weapon == "1h" and second_weapon == "gl":
                w_msg1 = " uses his shield to press past the guard of "
                w_msg2 = "'s glaive, driving his sword deep into his foe!"
                print(first_duelist, w_msg1, second_duelist, w_msg2, sep="")

            if first_weapon == "2h" and second_weapon == "1h":
                w_msg1 = " tries to block "
                w_msg2 = "'s two-handed sword with his shield but the massive swing breaks through his guard!"
                print(second_duelist, w_msg1, first_duelist, w_msg2, sep="")

            if first_weapon == "gl" and second_weapon == "2h":
                w_msg1 = "'s glaive has more reach than "
                w_msg2 = "'s two-handed sword and this lets him strike at his foe's hands and arms with impunity."
                print(first_duelist, w_msg1, second_duelist, w_msg2, sep="")

        print(first_duelist, "deals", d50, "damage!") #X lands a super effective hit!
    elif winner == 2:
        if d50 > 30:
            if second_weapon == "1h" and first_weapon == "gl":
                w_msg1 = " uses his shield to press past the guard of "
                w_msg2 = "'s glaive, driving his sword deep into his foe!"
                print(second_duelist, w_msg1, first_duelist, w_msg2, sep="")

            if second_weapon == "2h" and first_weapon == "1h":
                w_msg1 = " tries to block "
                w_msg2 = "'s two-handed sword with his shield but the massive swing breaks through his guard!"
                print(first_duelist, w_msg1, second_duelist, w_msg2, sep="")

            if second_weapon == "gl" and first_weapon == "2h":
                w_msg1 = "'s glaive has more reach than "
                w_msg2 = "'s two-handed sword and this lets him strike at his foe's hands and arms with impunity."
                print(second_duelist, w_msg1, first_duelist, w_msg2, sep="")

        print(second_duelist, "deals", d50, "damage!")

    else:
        print("Weapons clash!", first_duelist, "and", second_duelist, "strain their steel as they circle each other.")

def battle():
    global first_health
    global second_health
    if winner == 2:
        first_health = first_health - d50
        if first_health > 0:
            # eventually I can change these to verbal dramatizations.
            print("     ", first_duelist, "has", first_health, "health remaining.", second_duelist, "has", second_health, "health remaining.")
        else:
            print("*", first_duelist, "is defeated!", second_duelist, "has", second_health, "health remaining.")
    elif winner == 1:
        second_health = second_health - d50
        if second_health > 0:
            print("     ", first_duelist, "has", first_health, "health remaining.", second_duelist, "has", second_health, "health remaining.")
        else:
            print("*", second_duelist, "is defeated!", first_duelist, "has", first_health, "health remaining.")
    else:
        print("The combatants break away, both looking for an opening.")

print(first_duelist, " (",first_health,") vs. ", second_duelist, " (", second_health, ")!", sep="",)
input("\033[1;31;40mPress enter to begin!\033[0m\n")

dice()
battle_msg()
battle()

while 3: #continue until one's health is 0
    if first_health <= 0 or second_health <= 0:
        # set the health levels in the .txt files when I get around to it.
        break

    input("Press enter to go to the next round.\n")
    dice()
    battle_msg()
    battle()

# Non-commercial use okay with me, otherwise,
# Copyright 2016 Alex Wortham