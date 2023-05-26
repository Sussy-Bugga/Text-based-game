#7 situations with 3 Different Options = 35 different Choices
#Game Choice Database
c1={1:"Sword ",2:"Battle-Axe ",3:"Warhammer "}
c2={1:"Rocky Path ",2:"Smooth Path ",3:"Forest Path "}
c3={1:"Shield ",2:"Fire-Potion ",3:"Web-Slinger "}
c4={1:"Run ",2:"Fight ",3:"Ignore"}
c5={1:"Dragon's lair ",2:"Game-Win ",3:"Unlimited-bitches"}
c6={1:"Twerk Aggressively ",2:"Use your weapon ",3:"Run around in circles" }
c7={1:"Run away",2:"Attack it",3:"Drink a fire potion"}
health=100
skills = []
gameOn = int(input("Brave Adventurer! \nWelcome to the adventure's Guild! \nWould you like to Play Dragons Slayers 0.1?\nYes(1)    No(0):\n"))
def showhealth():
    print("Health:",health)
#Stage 1
while gameOn == 1 and health>0 and gameOn !=0:
    weapon = int(input(("Welcome. Chose your weapon to begin your journey\n"+c1[1]+c1[2]+c1[3]+"\n1/2/3: ")))
    if weapon ==1:
        weaponSelected = c1[1]
    elif weapon ==2:
        weaponSelected = c1[2]
    elif weapon ==3:
        weaponSelected = c1[3]
    else:
        print("Please Enter a valid number")
    showhealth()
    print("You've selected the "+weaponSelected+"!")
    gameOn =2
#Stage 2
while gameOn == 2 and health>0 and gameOn !=0:
    choice = int(input("Select a path to chose from:\n"+c2[1]+c2[2]+c2[3]+"\n1/2/3: "))
    if choice ==1:
        print("You gain terrain traversing experience")
        skills.append("terrain")
    elif choice ==2:
        print("You reach your destination smoothly")
    elif choice ==3:
       print("You Encounter a wild beast and are defeated")
       gameOn ="N"
    else:
         print("Please Enter a valid number")
    gameOn =3
#Stage 3
while gameOn == 3 and health>0 and gameOn !=0:
    choice = int(input("You encounter a witch and she decides to give you a blessing. Select a blessing:\n"+c3[1]+c3[2]+c3[3]+"\n1/2/3: "))
    if choice ==1:
        print("You gain a Shield")
        skills.append(c3[1])
    elif choice ==2:
        print("You gain a Fire-Potion")
        skills.append(c3[2])
    elif choice ==3:
       print("You gain a Web-Slinger ")
       skills.append(c3[3])
    else:
         print("Please Enter a valid number")
    gameOn =4
#Stage 4
while gameOn == 4 and health>0 and gameOn !=0:
    choice = int(input("You encounter a wild boar, what action do you take?:\n"+c4[1]+c4[2]+c4[3]+"\n1/2/3: "))
    if choice ==1:
        print("You run away")
    elif choice ==2:
        print("you kill the boar and gain battle experience")
        skills.append("battle-xp")
    elif choice ==3:
       print("The boar kills you ")
       gameOn = 0
    else:
         print("Please Enter a valid number")
    gameOn =5
#Stage5
while gameOn == 5 and health>0 and gameOn !=0:
    choice = int(input("You encounter a sign saying the following things:\n"+c5[1]+c5[2]+c5[3]+"\nWhich one would you chose?\n1/2/3: "))
    if choice ==1:
        print("You advance towards the dragon")
        gameOn =6
    elif choice ==2:
        print("you lazy ass")
        gameOn = 0
    elif choice ==3:
       print("Even if this game had that feature, you wouldnt be able to access it")
       gameOn = 0
    else:
         print("Please Enter a valid number")
#Stage6
while gameOn == 6 and health>0 and gameOn !=0:
    choice = int(input("You encounter the dragon.:\n"+c6[1]+c6[2]+c6[3]+"\nWhat will you do??\n1/2/3: "))
    if choice == 1 or choice==2:
        print("You are toast")
      
        gameOn = 0
    elif choice ==3:
       print("You dodge the dragon's breath")
       gameOn =7
    else:
         print("Please Enter a valid number")
#Stage7
while gameOn == 7 and health>0 and gameOn !=0:
    choice = int(input("The Dragon is tired.:\n"+c7[1]+c7[2]+c7[3]+"\nWhat will you do??\n1/2/3: "))
    if choice ==1:
        print("You're a coward\n~The city Folk")
        print("Yo've enraged the dragon, it burns your village to a crisp")
        gameOn=0
    elif choice==2:
        print("The dragon was just acting! You die")
        gameOn = 0
    elif choice ==3:
        if any(item == "Fire-Potion " for item in skills):
            print("You dodge the dragon's breath")
            gameOn=8
        else:
            print("You dont have a fire potion. You die")
            gameOn = 0
    else:
         print("Please Enter a valid number")
#Win
while gameOn == 8 and health>0 and gameOn !=0:
    print("You Win!")
print("Thank you for playing in this text based adventure game")
