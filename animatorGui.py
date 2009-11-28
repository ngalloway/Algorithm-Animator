import Tkinter
import copy
from time import sleep
import threading
import Queue

class animatedList:
    def __init__(self, l):
        self.theList = l
        self.highlighted = [False] * len(l)
        self.states = []

    def show(self):
        elementNo = len(self.theList)
        root = Tkinter.Tk()
        root.minsize(20 + len(self.theList) * 25, 300)
        canvas = Tkinter.Canvas(root, background="white")
        canvas.pack(expand=1, fill="both")
        for state in self.states:
            canvas.delete(Tkinter.ALL)
            for i in xrange(len(state.theList)):
                x = 10 + i * 25
                c = "blue" if state.highlighting[i] else "white"
                canvas.create_rectangle(x, 200, x + 20, 200 - state.theList[i], fill=c)
            root.update()
            sleep(0.4)
        root.mainloop()

    def highlight(self, startIndex, endIndex = None):
        if endIndex != None:
            self.__highlightRange(startIndex, endIndex)
        else:
            self.__highlightSingle(startIndex)
        self.update()
            
    def __highlightRange(self, startIndex, endIndex):
        for i in xrange(startIndex, endIndex + 1):
            self.highlighted[i] = True
            
    def __highlightSingle(self, index):
        self.highlighted[index] = True
    
    def unhighlight(self, index):
        self.highlighted[index] = False
        self.update()
        
    def __setitem__(self, key, value):
        self.theList[key] = value
        self.update()
    
    def __getitem__(self, key):
        return self.theList[key]
    
    def __len__(self):
        return len(self.theList)
    
    def update(self):
        self.states.append(State(self.theList, self.highlighted))

class State:
    def __init__(self, l, highlighting):
        self.theList = copy.deepcopy(l)
        self.highlighting = copy.deepcopy(highlighting)