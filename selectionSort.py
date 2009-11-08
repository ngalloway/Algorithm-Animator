import random
from animator import animatedList

def selectionSort(l):
    al = animatedList(l)
    for i in range(len(l)):
        al.unhighlight()
        al.highlight(0, i)
        minimum = i
        for j in range(i, len(l)):
            al.highlight(minimum)
            al.highlight(j)
            if l[j] < l[minimum]:
                minimum = j
            unhighlight[
        #animator.swap(l, minimum, i)
        l[i], l[minimum]  = l[minimum], l[i]

def main():
    l = [random.randint(1, 30) for i in range(20)]
    print l
    selectionSort(l)
    print l

main()