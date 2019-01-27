import random 
from FormatFunctions import formatPoints

def displayScore(count, playerScore, npcScore, name):
    print("  ")
    interation = 0
    round = formatPoints(count)
    plPoints = formatPoints(playerScore)
    npcPoints = formatPoints(npcScore)
    #   being lazy
    while interation <3:
        if interation == 1:
            print("--" + name + "---------------Round------------------Winner--")
            print("--------" + plPoints + "-----------------------------"+round+"----------------------"+npcPoints+"----")
        else:
            print("---------------------------------------------------------------------")
            print("---------------------------------------------------------------------")        
        interation += 1
    
    print(" ")

def rockPaperScissors():
    answer = input("Rock (R), Paper (P), Scissors (S): ")
    while answer != 'R' and answer != "r" and answer != "P" and answer != "p" and answer != "S" and answer != "s":
        answer = input("Rock (R), Paper (P), Scissors (S): ")

    print(" ")
    return answer


def startRound():
    answer = rockPaperScissors()
    options = ["R", "P", "S"]    
    npcAnswer = random.choice(options)
    if str.upper(answer) == npcAnswer:
        print("TIE!")
        print("1, 2, 3 Shoot! ")
        return "TIE"
    elif str.upper(answer) == "R" :
        if npcAnswer == "P":
            # npc wins
            print("You: Rock")
            print("Me: Paper")
            print("Awww too bad! Maybe next time")
            return "NPC"
        else:
            #player wins
            print("You: Rock")
            print("Me: Scissors")
            print("Eh, you got luckily this time!")
            return "Player"

    elif str.upper(answer) == "P" :
        if npcAnswer == "S":
            # npc wins
            print("You: Paper")
            print("Me: Scissors")
            print("Awww too bad! Maybe next time")
            return "NPC"
        else:
            #player wins
            print("You: Paper")
            print("Me: Rock")
            print("Eh, you got luckily this time!")
            return "Player"

    elif str.upper(answer) == "S" :
        if npcAnswer == "R":
            # npc wins
            print("You: Scissors")
            print("Me: Rock")
            print("Awww too bad! Maybe next time")
            return "NPC"
        else:
            #player wins
            print("You: Scissors")
            print("Me: Paper")
            print("Eh, you got luckily this time!")
            return "Player" 
    else:
        return ""



def startGame():
    count = 0
    playerScore = 0
    npcScore = 0
    name = "Private Saggy Nipples"
    while playerScore < 10 and npcScore < 10:
        winner = startRound()
        if winner == "NPC":
            count += 1
            npcScore +=1
            displayScore(count, playerScore, npcScore, name)
        elif winner == "Player":
            count +=1
            playerScore +=1
            displayScore(count, playerScore, npcScore, name)

    nextGame = "Y"
    if playerScore == 10:
        nextGame = input("No fair! I want a rematch!! (Continue playing?? Y/N ")
    else:
        nextGame = input("Ha! Suck on that Hoosier! (Continue playing?? Y/N ")

    while nextGame !="Y" and nextGame !="y" and nextGame !="N" and nextGame !="n":
        nextGame = input("Sorry. I didn't get that. Did you want to keep playing? Y/N ")
    
    count = 0
    playerScore = 0
    npcScore = 0
    return str.upper(nextGame)

