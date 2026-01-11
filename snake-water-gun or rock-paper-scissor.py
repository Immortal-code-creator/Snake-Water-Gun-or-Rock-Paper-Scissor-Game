#The Game is Snake-water-gun or Rock-paper-scissor
#The User will have to choose between two games which one he wants to play snake-water-gun or rock-paper-scissor
#Based on users decision the program will run and there will be a competition between user and computer
#The match will be of 5 points for easy level , 10 points for medium level and 15 points for hard level for 1st Game and 7 points for easy level,16 points for medium level and 22 points for hard level both the user and the computer score will be displayed after each round
#In each round the user will pick on of the following snake,water or gun and also same for rock,paper or scissor
#If the user and the computers decision are same then a draw will be displayed and no points will be given to either of the players
#The Game will end when either the user or the computer reach the points threshold
#we will use python's built-in module random
import random
user=str(input("Enter Your Name:-")).capitalize()
print(f"                    🎮 WELCOME TO SNAKE-WATER-GUN OR ROCK-PAPER-SCISSOR GAME,{user}                       ")
print("          PRESS '1' FOR SNAKE-WATER-GUN GAME OR PRESS '2' FOR ROCK-PAPER-SCISSOR GAME                    ")
print("          PRESS 'E'/'e' FOR EASY MODE OR PRESS 'M'/'m' FOR MEDIUM MODE OR PRESS 'H'/'h' FOR HARD MODE        ")
user1=0
play=False
while(user1!=1 and user1!=2):
    try:
        play=True
        user1 = int(input(f"Which Game You Want to Play,{user}:-"))
        if(play and user1==1):
            print(f"OK,{user} It Is SNAKE-WATER-GUN Game 🐍 🌊 🔫,Best Of Luck")
            user2=str(input("In Which Mode You Want Play The Game(Easy/Medium/Hard):-"))
            count=0
            count1=0
            if(play and (user2=='e'or user2=='E')):
                print("             Welcome To Easy Mode Of SNAKE-WATER-GUN Game 🐍 🌊 🔫                              ")
                print("         Press 's' For Snake or Press 'w' For Water or Press 'g' For Gun                         ")
                print("First To Reach 5 points will Win ")
                print("LET THE GAME BEGIN ✨ ")
                while(count<5 and count1<5):
                    l1=["Snake","Water","Gun"]
                    a=random.choice(l1)
                    user3=str(input("Enter Your Choice(Snake/Water/Gun):-"))
                    try:
                        if(user3=="s" and a=="Water"):
                            print(f"The Computer Chooses {a}")
                            print("Snake 🐍 Has Drunk The Water 🌊 ")
                            print(f"{user} Has Won")
                            count=count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="w" and a=="Snake"):
                            print(f"The Computer Chooses {a}")
                            print("Snake 🐍 Has Drunk The Water 🌊")
                            print("Computer Has Won")
                            count1=count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="s" and a=="Snake"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="g" and a=="Snake"):
                            print(f"The Computer Chooses {a}")
                            print("Snake 🐍 Is Killed By The Gun 🔫 ")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="s" and a=="Gun"):
                            print(f"The Computer Chooses {a}")
                            print("Snake 🐍 Is Killed By The Gun 🔫")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="g" and a=="Gun"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="w" and a=="Gun"):
                            print(f"The Computer Chooses {a}")
                            print("Water 🌊 Has Doused The Gun 🔫 ")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="g" and a=="Water"):
                            print(f"The Computer Chooses {a}")
                            print("Water 🌊 Has Doused The Gun 🔫")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="w" and a=="Water"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        else:
                            print("Enter a Valid Choice(s/w/g)")
                    except Exception as e:
                        print("Enter a Valid Choice(s/w/g)")
                print(f"Final Score of {user} is {count}")
                print(f"Final Score of Computer is {count1}")
                if(count>count1):
                    print(f"Congratulations, {user} You Have The Won The Game With {count} Points(Easy-Mode)")
                    print("You Can Try Medium/Hard Mode If You Want More Challenge ⚔️")
                else:
                    print(f"The Computer Has Won With {count1} Points(Easy-Mode)")
                    print("Better Luck Next Time!!")
            elif(play and (user2=='m'or user2=='M')):
                print("             Welcome To Medium Mode Of SNAKE-WATER-GUN Game 🐍 🌊 🔫                              ")
                print("         Press 's' For Snake or Press 'w' For Water or Press 'g' For Gun                         ")
                print("First To Reach 10 points will Win ")
                print("LET THE GAME BEGIN ✨ ")
                while(count<10 and count1<10):
                    l1=["Snake","Water","Gun"]
                    a=random.choice(l1)
                    user3=str(input("Enter Your Choice(Snake/Water/Gun):-"))
                    try:
                        if(user3=="s" and a=="Water"):
                            print(f"The Computer Chooses {a}")
                            print("Snake 🐍 Has Drunk The Water 🌊")
                            print(f"{user} Has Won")
                            count=count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="w" and a=="Snake"):
                            print(f"The Computer Chooses {a}")
                            print("Snake 🐍 Has Drunk The Water 🌊")
                            print("Computer Has Won")
                            count1=count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="s" and a=="Snake"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="g" and a=="Snake"):
                            print(f"The Computer Chooses {a}")
                            print("Snake 🐍 Is Killed By The Gun 🔫")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="s" and a=="Gun"):
                            print(f"The Computer Chooses {a}")
                            print("Snake 🐍 Is Killed By The Gun 🔫")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="g" and a=="Gun"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="w" and a=="Gun"):
                            print(f"The Computer Chooses {a}")
                            print("Water 🌊 Has Doused The Gun 🔫")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="g" and a=="Water"):
                            print(f"The Computer Chooses {a}")
                            print("Water 🌊 Has Doused The Gun 🔫")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif(user3=="w" and a=="Water"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        else:
                            print("Enter a Valid Choice(s/w/g)")
                    except Exception as e:
                        print("Enter a Valid Choice(s/w/g)")
                print(f"Final Score of {user} is {count}")
                print(f"Final Score of Computer is {count1}")
                if(count>count1):
                    print(f"Congratulations, {user} You Have The Won The Game With {count} Points(Medium-Mode)")
                    print("You Are on Your Way To Become Pro")
                else:
                    print(f"The Computer Has Won With {count1} Points(Medium-Mode)")
                    print("Better Luck Next Time!!")
            elif(play and (user2=='h'or user2=='H')):
                print(
                    "             Welcome To Hard Mode Of SNAKE-WATER-GUN Game 🐍 🌊 🔫                              ")
                print(
                    "         Press 's' For Snake or Press 'w' For Water or Press 'g' For Gun                         ")
                print("First To Reach 15 points will Win ")
                print("LET THE GAME BEGIN ✨ ")
                while (count < 15 and count1 < 15):
                    l1 = ["Snake", "Water", "Gun"]
                    a = random.choice(l1)
                    user3 = str(input("Enter Your Choice(Snake/Water/Gun):-"))
                    try:
                        if (user3 == "s" and a == "Water"):
                            print(f"The Computer Chooses {a}")
                            print("Snake 🐍 Has Drunk The Water 🌊")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "w" and a == "Snake"):
                            print(f"The Computer Chooses {a}")
                            print("Snake 🐍 Has Drunk The Water 🌊")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "s" and a == "Snake"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "g" and a == "Snake"):
                            print(f"The Computer Chooses {a}")
                            print("Snake 🐍 Is Killed By The Gun 🔫")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "s" and a == "Gun"):
                            print(f"The Computer Chooses {a}")
                            print("Snake 🐍 Is Killed By The Gun 🔫")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "g" and a == "Gun"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "w" and a == "Gun"):
                            print(f"The Computer Chooses {a}")
                            print("Water 🌊 Has Doused The Gun 🔫")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "g" and a == "Water"):
                            print(f"The Computer Chooses {a}")
                            print("Water 🌊 Has Doused The Gun 🔫")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "w" and a == "Water"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        else:
                            print("Enter a Valid Choice(s/w/g)")
                    except Exception as e:
                        print("Enter a Valid Choice(s/w/g)")
                print(f"Final Score of {user} is {count}")
                print(f"Final Score of Computer is {count1}")
                if (count > count1):
                    print(f"Congratulations, {user} You Have The Won The Game With {count} Points(Hard-Mode)")
                    print("You Are a Pro Gamer")
                else:
                    print(f"The Computer Has Won With {count1} Points(Hard-Mode)")
                    print("Better Luck Next Time!!")
        elif(play and user1==2):
            print(f"OK,{user} It Is ROCK-PAPER-SCISSOR Game 🪨 📄 ✂️,Best Of Luck")
            user2 = str(input("In Which Mode You Want Play The Game(Easy/Medium/Hard):-"))
            count = 0
            count1 = 0
            if (play and (user2 == 'e' or user2 == 'E')):
                print("             Welcome To Easy Mode Of  Game ROCK-PAPER-SCISSOR Game 🪨 📄 ✂️                              ")
                print("         Press 'r' For Rock or Press 'p' For Scissor or Press 's' For Scissor                        ")
                print("First To Reach 7 points will Win ")
                print("LET THE GAME BEGIN ✨ ")
                while (count < 7 and count1 < 7):
                    l1 = ["Rock", "Paper", "Scissor"]
                    a = random.choice(l1)
                    user3 = str(input("Enter Your Choice(Rock/Paper/Scissor):-"))
                    try:
                        if (user3 == "p" and a == "Rock"):
                            print(f"The Computer Chooses {a}")
                            print("The Paper 📄 Has Covered The Rock 🪨")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "r" and a == "Paper"):
                            print(f"The Computer Chooses {a}")
                            print("The Paper 📄 Has Covered The Rock 🪨")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "r" and a == "Rock"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "r" and a == "Scissor"):
                            print(f"The Computer Chooses {a}")
                            print("The Rock 🪨 Has Smashed the Scissor ✂️ ")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "s" and a == "Rock"):
                            print(f"The Computer Chooses {a}")
                            print("The Rock 🪨 Has Smashed the Scissor ✂️ ")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "s" and a == "Scissor"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "s" and a == "Paper"):
                            print(f"The Computer Chooses {a}")
                            print("Scissors ✂️ Has Cut The Paper 📄 into Pieces")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "p" and a == "Scissor"):
                            print(f"The Computer Chooses {a}")
                            print("Scissors ✂️ Has Cut The Paper 📄 into Pieces")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "p" and a == "Paper"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        else:
                            print("Enter a Valid Choice(r/p/s)")
                    except Exception as e:
                        print("Enter a Valid Choice(r/p/s)")
                print(f"Final Score of {user} is {count}")
                print(f"Final Score of Computer is {count1}")
                if (count > count1):
                    print(f"Congratulations, {user} You Have The Won The Game With {count} Points(Easy-Mode)")
                    print("You Can Try Medium/Hard Mode If You Want More Challenge ⚔️")
                else:
                    print(f"The Computer Has Won With {count1} Points(Easy-Mode)")
                    print("Better Luck Next Time!!")
            elif (play and (user2 == 'm' or user2 == 'M')):
                print(
                    "             Welcome To Medium Mode Of  Game ROCK-PAPER-SCISSOR Game 🪨 📄 ✂️                              ")
                print(
                    "         Press 'r' For Rock or Press 'p' For Scissor or Press 's' For Scissor                        ")
                print("First To Reach 16 points will Win ")
                print("LET THE GAME BEGIN ✨ ")
                while (count < 16 and count1 < 16):
                    l1 = ["Rock", "Paper", "Scissor"]
                    a = random.choice(l1)
                    user3 = str(input("Enter Your Choice(Rock/Paper/Scissor):-"))
                    try:
                        if (user3 == "p" and a == "Rock"):
                            print(f"The Computer Chooses {a}")
                            print("The Paper 📄 Has Covered The Rock 🪨")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "r" and a == "Paper"):
                            print(f"The Computer Chooses {a}")
                            print("The Paper 📄 Has Covered The Rock 🪨")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "r" and a == "Rock"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "r" and a == "Scissor"):
                            print(f"The Computer Chooses {a}")
                            print("The Rock 🪨 Has Smashed the Scissor ✂️")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "s" and a == "Rock"):
                            print(f"The Computer Chooses {a}")
                            print("The Rock 🪨 Has Smashed the Scissor ✂️")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "s" and a == "Scissor"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "s" and a == "Paper"):
                            print(f"The Computer Chooses {a}")
                            print("Scissors ✂️ Has Cut The Paper 📄 into Pieces")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "p" and a == "Scissor"):
                            print(f"The Computer Chooses {a}")
                            print("Scissors ✂️ Has Cut The Paper 📄 into Pieces")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "p" and a == "Paper"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        else:
                            print("Enter a Valid Choice(r/p/s)")
                    except Exception as e:
                        print("Enter a Valid Choice(r/p/s)")
                print(f"Final Score of {user} is {count}")
                print(f"Final Score of Computer is {count1}")
                if (count > count1):
                    print(f"Congratulations, {user} You Have The Won The Game With {count} Points(Medium-Mode)")
                    print("You Are on Your Way To Become Pro")
                else:
                    print(f"The Computer Has Won With {count1} Points(Medium-Mode)")
                    print("Better Luck Next Time!!")
            elif (play and (user2 == 'h' or user2 == 'H')):
                print(
                    "             Welcome To Hard Mode Of  Game ROCK-PAPER-SCISSOR Game 🪨 📄 ✂️                              ")
                print(
                    "         Press 'r' For Rock or Press 'p' For Scissor or Press 's' For Scissor                        ")
                print("First To Reach 22 points will Win ")
                print("LET THE GAME BEGIN ✨ ")
                while (count < 22 and count1 < 22):
                    l1 = ["Rock", "Paper", "Scissor"]
                    a = random.choice(l1)
                    user3 = str(input("Enter Your Choice(Rock/Paper/Scissor):-"))
                    try:
                        if (user3 == "p" and a == "Rock"):
                            print(f"The Computer Chooses {a}")
                            print("The Paper 📄 Has Covered The Rock 🪨")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "r" and a == "Paper"):
                            print(f"The Computer Chooses {a}")
                            print("The Paper 📄 Has Covered The Rock 🪨")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "r" and a == "Rock"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "r" and a == "Scissor"):
                            print(f"The Computer Chooses {a}")
                            print("The Rock 🪨 Has Smashed the Scissor ✂️")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "s" and a == "Rock"):
                            print(f"The Computer Chooses {a}")
                            print("The Rock 🪨 Has Smashed the Scissor ✂️")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "s" and a == "Scissor"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "s" and a == "Paper"):
                            print(f"The Computer Chooses {a}")
                            print("Scissors ✂️ Has Cut The Paper 📄 into Pieces")
                            print(f"{user} Has Won")
                            count = count + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "p" and a == "Scissor"):
                            print(f"The Computer Chooses {a}")
                            print("Scissors ✂️ Has Cut The Paper 📄 into Pieces")
                            print("Computer Has Won")
                            count1 = count1 + 1
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        elif (user3 == "p" and a == "Paper"):
                            print("It is a Draw")
                            print(f"{user} Score:- {count}")
                            print(f"Computer Score:- {count1}")
                        else:
                            print("Enter a Valid Choice(r/p/s)")
                    except Exception as e:
                        print("Enter a Valid Choice(r/p/s)")
                print(f"Final Score of {user} is {count}")
                print(f"Final Score of Computer is {count1}")
                if (count > count1):
                    print(f"Congratulations, {user} You Have The Won The Game With {count} Points(Hard-Mode)")
                    print("You Are a Pro Gamer")
                else:
                    print(f"The Computer Has Won With {count1} Points(Hard-Mode)")
                    print("Better Luck Next Time!!")
        else:
            print("Enter '1' For FOR Snake-Water-Gun Game Or Enter '2' For Rock-Paper-Scissor Game ")
    except Exception as e:

        print("Pls,Enter a Valid Symbol(1 or 2)")
