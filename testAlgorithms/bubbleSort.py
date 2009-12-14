import random
import animator

def bubbleSort(l):
    al = animator.AnimatedList(l)
    swapped = True
    while swapped:
        swapped = False
        for i in xrange(0, len(l) - 1):
            al.highlight(i)
            al.highlight(i + 1)
            if al[i] > al[i + 1]:
                al.swap(i, i+1)
                swapped = True
            al.unhighlight(i)
        if not swapped:
            break
    return al

al = bubbleSort([random.randint(1, 50) for i in range(20)])
r = animator.BarChart(al)
gui = animator.Gui()
gui.add(r)
gui.run()