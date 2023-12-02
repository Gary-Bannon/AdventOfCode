file1 = open('/home/gary/codevent23/AdventOfCode/Day2/input.txt', 'r')
string = file1.read()
list = string.split('\n')

possibleGames = []

for game in list:
    if game == '':
        pass
    else:
        GameNo = 0
        red = 0
        green = 0
        blue = 0

        gameSplit = game.split(';')

        gameIndex = game.find('Game')
        if ((game[gameIndex + 7]).isdigit()) == True:
            gameNumber = ''
            gameNumber = game[5:8]
            GameNo = int(gameNumber)
        elif ((game[gameIndex + 6]).isdigit()) == True:
            gameNumber = ''
            gameNumber = game[5:7]
            GameNo = int(gameNumber)
        else:
            gameNumber = ''
            gameNumber = game[5]
            GameNo = int(gameNumber)
            
        def findBallCount(colour, input):
            number = ''
            count = 0
        
            index = i.find(input)
            doubleDigit = index - 3
            singleDigit = index - 2

            if index == -1:
                pass
            elif index != -1 & ((i[doubleDigit]).isdigit() == True):
                number = i[doubleDigit] + i[singleDigit]
                count = int(number)
            elif index != -1:
                count = int(i[singleDigit])
            if colour == 0:
                colour = count
           
            count = max(count, colour)
            return count

        for i in gameSplit:
            if findBallCount(blue, 'blue') == 0:
                pass
            else:
                blue = findBallCount(blue, 'blue')

            if findBallCount(red, 'red') == 0:
                pass
            else:
                red = findBallCount(red, 'red')
            
            if findBallCount(green, 'green') == 0:
                pass
            else:
                green = findBallCount(green, 'green')

        print(blue, 'blue')
        print(red, 'red')
        print(green, 'green')
        
        power = blue*red*green
        
        possibleGames.append(power)

print(possibleGames)
        
print(sum(possibleGames))

    

    



