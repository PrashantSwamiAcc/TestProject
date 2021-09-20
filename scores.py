def tabulate(score,userplays, complays):
    winpercent = score.count(1) / len(score)
    cwinpercent = score.count(2) / len(score)
    rusercount = userplays.count('r')
    pusercount = userplays.count('p')
    susercount = userplays.count('s')
    rcompcount = complays.count('r')
    pcompcount = complays.count('p')
    scompcount = complays.count('s')
    games = len(userplays)
    print('User   |         R         |         P         |        S         |         W%         |')
    print('Player |', rusercount * 100 / games, '% |', pusercount * 100 / games, '% |', susercount * 100 / games, '% |',
          winpercent * 100, '% |')
    print('Computer|', pcompcount * 100 / games, '% |', pcompcount * 100 / games, '% |', scompcount * 100 / games, '% |',
          cwinpercent * 100, '% |')
