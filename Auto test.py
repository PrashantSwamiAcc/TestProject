import scores
from rps import rps
from compute import compute
from scores import tabulate

tests = int(input('How many tests?'))
count = 0
score = []
userplays = []
complays = []

while count <= tests:
    inp = compute()
    comp = compute()
    wl, inp, comp = rps(inp, comp)
    score.append(wl)
    userplays.append(inp)
    complays.append(comp)
    count += 1

test = scores.tabulate(score, userplays, complays)