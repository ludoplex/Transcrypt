from random import *

result = ''

def output (any):
    result += any + '<br>\n'

for fixedSeed in (False, True):
    if fixedSeed:
        seed (3)
    else:
        seed ()

    output(f"------ {'fixed seed' if fixedSeed else 'auto seed'} ------")

    output ('--- randint in [10, 20] ---')
    for _ in range (20):
        output (randint (10, 20))

    output ('<br>\n--- choice ---')
    for _ in range (20):
        output (choice ([1, 2, 3, 4, 5]))

    output ('<br>\n--- random ---')
    for _ in range (20):
        output (random ())

    output ('<br>\n--- shuffle ---')
    aList = [0, 1, 2, 3, 4, 5, 6]
    output (aList)
    for _ in range (7):
        shuffle (aList)
        output (aList)

    output ('<br>\n')

document.getElementById ('output') .innerHTML = result
