import animator

def binarySearch(l, n):
    al = animator.AnimatedList(l)
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
    return al

def linearSearch(l, n):
    al = animator.AnimatedList(l)
    i = 0
    for i in xrange(len(al)):
        if al[i] == n:
            al.highlight(i, colour="green")
            break
        else:
            al.highlight(i, colour="red")
    return al

r1 = animator.BarChart(binarySearch(range(5, 250, 5), 13))
r2 = animator.BarChart(linearSearch(range(5, 250, 5), 13))
gui = animator.Gui()
gui.add(r1)
gui.add(r2)
gui.run()
    