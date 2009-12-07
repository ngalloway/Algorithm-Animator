import random
import animator

def selectionSort(l):
    al = animator.AnimatedList(l)
    for i in range(len(al)):
        al.highlight(0, i, colour="green")
        minimum = i
        for j in range(i, len(al)):
            #al.highlight(minimum, colour="red")
            al.highlight(j)
            if al[j] < al[minimum]:
                al.unhighlight(minimum)
                minimum = j
                al.highlight(minimum, colour="red")
            else:
                al.unhighlight(j)
        al.unhighlight(minimum)
        al[i], al[minimum]  = l[minimum], l[i]
        al.unhighlight(minimum)
    return al
    #al.show()
        

def main():
    l1 = [random.randint(5, 50) for i in range(20)]
    r1 = animator.BarChart(selectionSort(l1))
    l2 = [random.randint(5, 50) for i in range(20)]
    r2 = animator.BarChart(selectionSort(l2))
    gui = animator.Gui()
    gui.add(r1)
    gui.add(r2)
    gui.run()
    

main()
