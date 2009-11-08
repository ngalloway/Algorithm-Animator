import random
from animator import animatedList

def main():
    l = [random.randint(1, 20) for i in xrange(20)]
    al = animatedList(l)
    al.show()

main()