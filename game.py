import scores
from compute import compute
from rps import rps
from scores import tabulate

score = []
userplays = []
complays = []
game_over = False
while not game_over:
    inp = input('Rock, Paper, or Scissors?')
    comp = compute()
    wl, inp, comp = rps(inp, comp)

    score.append(wl)
    userplays.append(inp)
    complays.append(comp)

    if wl == 1:
        print('You won!')
    if wl == 2:
        print('Darn, you lost!')
    if wl == 0:
        print("Dang, it's a tie!")
    again = input("Play again?")
    if again == 'y':
        pass
    else:
        game_over = True
test = scores.tabulate(score, userplays, complays)
# winpercent = score.count(1) / len(score)
# cwinpercent = score.count(2) / len(score)
# rusercount = userplays.count('r')
# pusercount = userplays.count('p')
# susercount = userplays.count('s')
# rcompcount = complays.count('r')
# pcompcount = complays.count('p')
# scompcount = complays.count('s')
# games = len(userplays)
# print('User   |         R         |         P         |        S         |         W%         |')
# print('Player |', rusercount*100 / games, '% |', pusercount*100 / games, '% |', susercount*100 / games, '% |', winpercent*100,'% |')
# print('Player |', pcompcount*100 / games, '% |', pcompcount*100 / games, '% |', scompcount*100 / games, '% |', cwinpercent*100,'% |')
