
# if i have to check a dict which contains multiple keys and and check if the values of those keys matches the users input how do i do that if my values are a list?


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
    global players
    global currentPlayer
    players = {}
    try:
        i = 1
        numberOfPlayers = int(input("Enter number of players(2-4): "))
        isPlayerNumberOkay = checkNumberOfPlayers(numberOfPlayers)

        if not isPlayerNumberOkay:
            return
        
        while i <= numberOfPlayers:
            playerName = input(f"Enter Name of the player{i}: ")
            players[f"player{i}"] = playerName
            i += 1
            
        currentPlayer = players["player1"]
        return True
    except Exception as e :
        print(f"An error occured in player input {e}")
        return False
        

def checkPlayerConfirmation(statement):
    global answers
    answers = ("yes","no","y","n")
    
    try:
        while True:
            userAnswer = input(f"{statement} (Y/N): ").lower()

            print(userAnswer)

            if userAnswer not in answers:
                print("Type in Yes (Y) or no (N)")
                continue
            elif userAnswer == "y" or userAnswer == "yes":
                return True
            else:
                return False
            
    except Exception as e:
        print(f"An error occured in player Confirmation {e}")
        return False
    

def switchPlayer(currentPlayer):

    print(f"current player is {currentPlayer}")
    if currentPlayer == players["player1"]:
        currentPlayer = players["player2"]
    elif currentPlayer == players["player2"]:
        currentPlayer = players["player3"]
    elif currentPlayer == players["player3"]:
        currentPlayer = players["player4"]
    elif currentPlayer == players["player4"]:
         currentPlayer = players["player1"]





while True:
    isPlayerInputOkay = checkPlayerInput()
    if isPlayerInputOkay:
        isPlayerReady = checkPlayerConfirmation("Proceed to game? ")
        if isPlayerReady:
            print(players)
            
            while True:
                print(f"current player is {currentPlayer}")
                confirmSwitch = checkPlayerConfirmation("Switch Player ")
                if confirmSwitch:
                    switchPlayer(currentPlayer)
                    print(currentPlayer)
                    continue
                else:
                    currentPlayer = ''
                    print("Thank you!")
                    break
            break


        else:
           players.clear()
           print("Thank You! See you next time")
           break

    else:
        print("Something's Wrong")
        continue

   
    
    
    

        



