# to fix:
# what happens if length of list changes?
# how long should bars stay highlighted?
# possibly use different colours instead of bool for highlighting

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
            
    def __highlightRange(self, startIndex, endIndex):
        for i in xrange(startIndex, endIndex + 1):
            self.highlighted[i] = True
        self.show()
            
    def __highlightSingle(self, index):
        self.highlighted[index] = True
        self.show()
    
    def unhighlight(self, index):
        self.highlighted[index] = False
    
    def __setitem__(self, key, value):
        self.theList[key] = value
    
    def __getitem__(self, key):
        return self.theList[key]
    
    def __len__(self):
        return len(self.theList)