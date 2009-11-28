import random
from animatorGui import animatedList

def selectionSort(l):
    al = animatedList(l)
    for i in range(len(al)):
        al.highlight(0, i)
        minimum = i
        for j in range(i, len(al)):
            al.highlight(minimum)
            al.highlight(j)
            if al[j] < al[minimum]:
                al.unhighlight(minimum)
                minimum = j
            else:
                al.unhighlight(j)
        al[i], al[minimum]  = l[minimum], l[i]
        al.unhighlight(minimum)
    al.show()
        

def main():
    l = [random.randint(5, 50) for i in range(20)]
    print l
    selectionSort(l)
    print l

main()