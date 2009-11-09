import random
from animator import animatedList

def selectionSort(l):
    al = animatedList(l)
    for i in range(len(l)):
        al.highlight(0, i)
        minimum = i
        for j in range(i, len(l)):
            al.highlight(minimum)
            al.highlight(j)
            if l[j] < l[minimum]:
                al.unhighlight(minimum)
                minimum = j
            else:
                al.unhighlight(j)
        l[i], l[minimum]  = l[minimum], l[i]
        al.unhighlight(minimum)
        

def main():
    l = [random.randint(1, 50) for i in range(20)]
    print l
    selectionSort(l)
    print l

main()