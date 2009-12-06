from animatorGui import animatedList

def binarySearch(l, n):
    al = animatedList(l)
    minimum, maximum = 0, len(al) - 1
    while minimum <= maximum:
        current = (minimum + maximum) / 2
        al.highlight(current, colour="red")
        if al[current] == n:
            al.highlight(current, colour="green")
            break
        elif al[current] < n:
            minimum = current + 1
        elif al[current] > n:
            maximum = current - 1
        al.unhighlight(current)
    al.show()

binarySearch(range(5, 150, 5), 13)