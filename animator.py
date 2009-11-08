import time

class animatedList:
    def __init__(self, l):
        self.theList = l
        self.highlighted = [False] * len(l)

    def show(self):
        for i, highlighted in zip(self.theList, self.highlighted):
            print ('O' if highlighted else 'X') * i
        print
        time.sleep(0.4)

    def highlight(self, startIndex, endIndex = None):
        if endIndex != None:
            self.__highlightRange(startIndex, endIndex)
        else:
            self.__highlightSingle(startIndex)
            
    def __highlightRange(self, startIndex, endIndex):
        for i in xrange(startIndex, endIndex + 1):
            self.highlighted[i] = True
            self.show()
            
    def __highlightSingle(self, index):
        self.highlighted[index] = True
        self.show()
    
    def unhighlight(self):
        for i in xrange(len(self.highlighted)):
            self.highlighted[i] = False