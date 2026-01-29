
# There are four players and if they have same initials, the initial which is not presented are presented to them instead of initial let's use emoji's
from random_unicode_emoji import random_emoji


players = {}

def checkNumberOfPlayers(numberOfPlayers):
    try:
        if numberOfPlayers < 2:

            print("Minimum 2 players required")
            return False
        
        if numberOfPlayers > 4:
            print("Maximum 4 players Required")
            return False
        
        return True
    except Exception as e:
        print(f"An error occured in number of players {e}")
        return False


def checkPlayerInput():
    try:
        i = 1
        numberOfPlayers = int(input("Enter number of players(2-4): "))
        isPlayerNumberOkay = checkNumberOfPlayers(numberOfPlayers)

        if not isPlayerNumberOkay:
            return
        
        while i <= numberOfPlayers:
            playerName = input(f"Enter Name of the player{i}: ")
            players[f"player{i}"] = random_emoji()[0]
            i += 1
        return True
    except Exception as e :
        print(f"An error occured in player input {e}")
        return False
        

def checkPlayerConfirmation():
    try:
        userAnswer = input("Proceed to the game (Y/N): ").lower()

        print(userAnswer)

        if not userAnswer == "y":
            players.clear()
            return False
        else:
            print("Okay")
            return True
    except Exception as e:
        print(f"An error occured in player Confirmation {e}")
        return False




while True:
    isPlayerInputOkay = checkPlayerInput()
    if isPlayerInputOkay:
        isPlayerReady = checkPlayerConfirmation()
        if isPlayerReady:
            print(players)
            print('Good luck')
            break
        else:
            print("Thank You! See you next time")
            break

    else:
        print("Something's Wrong")
        continue

   
    
    
    

        



