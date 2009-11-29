import Tkinter
import copy
from time import sleep

class animatedList:
    def __init__(self, l):
        self.theList = l
        self.highlighted = [False] * len(l)
        self.states = []
        self.root = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(self.root, background="white")
        self.canvas.pack(expand=1, fill = "both")

    def show(self):
        windowWidth = 20 + len(self.theList) * 25
        windowHeight = max(self.theList) + 20
        self.root.minsize(windowWidth, windowHeight)
        for state in self.states:
            self.canvas.delete(Tkinter.ALL)
            for i in xrange(len(state.theList)):
                x = 10 + i * 25
                c = "blue" if state.highlighting[i] else "white"
                self.canvas.create_rectangle(x, windowHeight - 10, x + 20, windowHeight - 10 - state.theList[i], fill=c)
            self.root.update()
            sleep(0.4)

    def highlight(self, startIndex, endIndex=None):
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

