from art import logo
import os
print(f"{logo}\nWelcome to the secret auction program")

players = []
exitFlag = 0

def addPlayer(playerName, playerBid):
    players.append(
        {
            "name": playerName,
            "bid" : playerBid,
        }
    )

def winnerPlayer():
    highestBidderIndex = 0
    
    if len(players) > 1:
        for index in range(1, len(players)):
            if players[index]["bid"] > players[highestBidderIndex]["bid"]:
                highestBidderIndex = index
    
    return highestBidderIndex        
            

while(not exitFlag):
    playerName = input("What is your name?: ")
    playerBid = int(input("What is your bid?: $"))
    response = input("Are there other bidders? yes/no: ").lower()
    
    addPlayer(playerName, playerBid)
    
    if(response != "yes"):
        exitFlag = 1
    
    #clear the terminal 
    os.system("clear")

winnerIndex = winnerPlayer()
print(f"The winner of the auction is : {players[winnerIndex]['name']} with an offer of ${players[winnerIndex]['bid']}")