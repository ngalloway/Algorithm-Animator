# allow different colours for highlighting
# play/pause/step buttons

import Tkinter
import copy
from time import sleep

class animatedList:
    
    def __init__(self, l):
        self.theList = l
        self.highlighted = ["white"] * len(l)
        self.states = []
        self.isPlaying = True
        
        self.root = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(self.root, background="white")
        self.canvas.pack(expand=1, fill = "both")
        f = Frame(root)
        f.pack_popagate(0)
        b = Button(f, text="Play/Pause")
        b.pack(fill="both", expand=1)
        

    def show(self):
        windowWidth = 20 + len(self.theList) * 25
        windowHeight = max(self.theList) + 20
        self.root.minsize(windowWidth, windowHeight)
        for state in self.states:
            self.canvas.delete(Tkinter.ALL)
            for i in xrange(len(state.theList)):
                x = 10 + i * 25
                c = state.highlighting[i]
                self.canvas.create_rectangle(x, windowHeight - 10, x + 20, windowHeight - 10 - state.theList[i], fill=c)
            self.root.update()
            sleep(0.1)
        self.root.mainloop()
    
    def __showState(self, state):
        self.canvas.delete(Tkinter.ALL)
        for i in xrange(len(state.theList)):
            x = 10 + i * 25
            c = state.highlighting[i]
            self.canvas.create_rectangle(x, windowHeight - 10, x + 20, windowHeight - 10 - state.theList[i], fill=c)
        self.root.update()
    
    def __play(self, stateIndex=0):
        while self.isPlaying and stateIndex < len(self.states):
            self.__showState(self.states[stateIndex]
            sleep(0.1)
            stateIndex += 1
        

    def highlight(self, startIndex, endIndex=None, colour="blue"):
        if endIndex != None:
            self.__highlightRange(startIndex, endIndex, colour)
        else:
            self.__highlightSingle(startIndex, colour)
        self.__update()
            
    def __highlightRange(self, startIndex, endIndex, colour):
        for i in xrange(startIndex, endIndex + 1):
            self.highlighted[i] = colour
            
    def __highlightSingle(self, index, colour):
        self.highlighted[index] = colour
    
    def unhighlight(self, index):
        self.highlighted[index] = "white"
        self.__update()
        
    def __setitem__(self, key, value):
        self.theList[key] = value
        self.__update()
    
    def __getitem__(self, key):
        return self.theList[key]
    
    def __len__(self):
        return len(self.theList)
    
    def __update(self):
        self.states.append(State(self.theList, self.highlighted))
    

class State:
    def __init__(self, l, highlighting):
        self.theList = copy.deepcopy(l)
        self.highlighting = copy.deepcopy(highlighting)

