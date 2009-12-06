import random
from animatorGui import animatedList

def bubbleSort(l):
    al = animatedList(l)
    swapped = True
    while swapped:
        swapped = False
        for i in xrange(0, len(l) - 1):
            al.highlight(i)
            al.highlight(i + 1)
            if al[i] > al[i + 1]:
                al[i], al[i + 1] = al[i + 1], al[i]
                swapped = True
            al.unhighlight(i)
        if not swapped:
            break
    al.show()

bubbleSort([random.randint(1, 50) for i in range(20)])

