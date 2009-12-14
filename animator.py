# scale the bars if possible/necessary
# scatter graph?

import Tkinter
import copy
from time import sleep

theGui = None

class Gui:
    def __init__(self):
        self.representations = []
        self.root = Tkinter.Tk()
        buttonFrame = Tkinter.Frame(self.root, height=40, width = 300)
        buttonFrame.pack_propagate(0)
        #playButton = Tkinter.Button(buttonFrame, text="Play/Pause", command=self.__togglePlay)
        #playButton.pack(fill="both", expand=1)
        #stepButton = Tkinter.Button(buttonFrame, text="Step forward", command=self.__step)
        #stepButton.pack(fill="both", expand=1)
        #backButton = Tkinter.Button(buttonFrame, text="Step backwards", command=self.__stepBack)
        #backButton.pack(fill="both", expand=1)
    
    def add(self, representation):
        self.representations.append(representation)
        representation.setGui(self)
    
    def run(self):
        for i in xrange(10000):
            for rep in self.representations:
                rep.showState(i)
            sleep(0.3)

class Representation:
    def __init__(self, al):
        self.isPlaying = True
        self.states = al.states
        self.stateIndex = 0
    
    def __play(self):
        while self.stateIndex < len(self.states):
            if  self.isPlaying:
                self.__showState(self.states[self.stateIndex])
                self.stateIndex += 1
            sleep(0.1)
            self.theGui.root.update()
    
    def __togglePlay(self):
        self.isPlaying = not self.isPlaying
    
    def __step(self):
        self.isPlaying = False
        self.stateIndex += 1
    
    def __stepBack(self):
        self.isPlaying = False
        self.stateIndex -= 1
    
    def setGui(self, gui):
        self.theGui = gui
        self.canvas = Tkinter.Canvas(self.theGui.root, background="white")
        self.canvas.pack(expand=1, fill="both")


class BarChart(Representation):
    def show(self):
        self.windowWidth = 20 + len(self.states[0].theList) * 25
        self.windowHeight = max(self.states[0].theList) + 20
        self.theGui.root.minsize(self.windowWidth, self.windowHeight)
        while True:
            if self.stateIndex == len(self.states) - 1:
                self.isPlaying = False
            self.__showState(self.states[self.stateIndex])
            if self.isPlaying:
                sleep(0.2)
                self.stateIndex += 1

    def showState(self, index):
        if index >= len(self.states):
            return
        self.__showState(self.states[index])

    def __showState(self, state):
        self.windowWidth = 20 + len(self.states[0].theList) * 25
        self.windowHeight = max(self.states[0].theList) + 20
        self.theGui.root.minsize(self.windowWidth, self.windowHeight) #move me somewhere else
        self.canvas.delete(Tkinter.ALL)
        for i in xrange(len(state.theList)):
            x = 10 + i * 25
            c = state.highlighting[i]
            self.canvas.create_rectangle(x, self.windowHeight - 10, 
                x + 20, self.windowHeight - 10 - state.theList[i], fill=c)
        self.theGui.root.update()
    
class AnimatedList:
    def __init__(self, l):
        self.theList = l
        self.highlighted = ["white"] * len(l)
        self.states = []

    def show(self):
        barChart = BarChart(self.states)
        barChart.show()
        #self.windowWidth = 20 + len(self.theList) * 25
        #self.windowHeight = max(self.theList) + 20
        #root.minsize(self.windowWidth, self.windowHeight)
        #while True:
            #if self.stateIndex == len(self.states) - 1:
                #self.isPlaying = False
            #self.__showState(self.states[self.stateIndex])
            #if self.isPlaying:
                #sleep(0.2)
                #self.stateIndex += 1

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
    
    def unhighlight(self, index=None):
        if index is None:
            self.__highlightRange(0, len(self.theList), "white")
        else:
            self.highlighted[index] = "white"
        self.__update()
    
    def swap(self, x, y):
        xColour, yColour = self.highlighted[x], self.highlighted[y]
        self.__highlightSingle(x, "red")
        self.__highlightSingle(y, "red")
        self.__update()
        self.theList[x], self.theList[y] = self.theList[y], self.theList[x]
        self.__update()
        self.__highlightSingle(x, xColour)
        self.__highlightSingle(y, yColour)
        
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