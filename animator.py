import time

class animatedList:
    def __init__(self, l):
        self.theList = l
        self.highlighted = [False] * len(l)

    def show(self):
        print '\n' * 50
        for i, highlighted in zip(self.theList, self.highlighted):
            print ('-' if highlighted else 'I') * i
        time.sleep(0.4)

    def highlight(self, startIndex, endIndex = None):
        if endIndex != None:
            self.__highlightRange(startIndex, endIndex)
        else:
            self.__highlightSingle(startIndex)
    # how long should bars stay highlighted?
    # possibly use different colours instead of bool
            
    def __highlightRange(self, startIndex, endIndex):
        for i in xrange(startIndex, endIndex + 1):
            self.highlighted[i] = True
            self.show()
            
    def __highlightSingle(self, index):
        self.highlighted[index] = True
        self.show()
    
    def unhighlight(self, index):
        self.highlighted[index] = False