inputData = list(map(int, input().split(" ")))

numberPlayers = inputData[0]
minimumScoreWin = inputData[1]
numberPlays = inputData[2]

players = {}

for numPlayer in range(numberPlayers):
    players[input()] = 0

for play in range(numberPlays):
    numberWinners = 0
    for player in players:
        if players[player] >= minimumScoreWin:
            numberWinners += 1

    if numberWinners == numberPlayers:
        break

    currentPlay = input().split(" ")
    currentPlayer = currentPlay[0]
    currentScore = int(currentPlay[1])
    for player in players:            
        if player == currentPlayer:
            players[currentPlayer] = players[player] + currentScore
            break


someWinner = False   # Variable Bandera para saber si hubo algun ganador

for player in players:
    if players[player] >= minimumScoreWin:
        someWinner = True
        print(player, "wins!")
if not(someWinner):
    print("No winner!")
