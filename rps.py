def rps(input, computer):
    win = 1
    lose = 2
    tie = 0
    if input == 'r' or input == 'p' or input == 's':
        if input == computer:
            return tie, input, computer
        elif input == "r":
            if computer == "s":
                return win, input, computer
            else:
                return lose, input, computer
        elif input == "p":
            if computer == "r":
                return win, input, computer
            else:
                return lose, input, computer
        elif input == "s":
            if computer == "p":
                return win, input, computer
            else:
                return lose, input, computer
    else:
        print('Invalid Input')
