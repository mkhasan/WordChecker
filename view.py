
from tkinter import Tk, Entry, W, E, N, S, PhotoImage, Checkbutton, Button, Radiobutton, \
        Menu, Frame, Label, LEFT, RIGHT, TOP, BOTTOM, NW, NE, SW, CENTER

import tkinter as tk

from conf import Conf
from finder import Finder




FONT_SIZE_NORMAL = 12
FONT_SIZE_SMALL = 8

FONT_NAME_LARGE = 'TkDefaultFont'
FONT_NAME_NORMAL = 'TkDefaultFont'
FONT_NAME_SMALL = 'TkDefaultFont'

#root = Tk()



class View:
    def __init__(self, _root, _finder):
        self.root = _root
        self.finder = _finder
        #Frame.__init__(self, root)
        #button1 = Button(self.root, text="Quit", command=root.quit, anchor=W)
        #button1.pack()
        self.Display()

    def Display(self):
        frame = Frame(self.root,bg="red")
        """
        if we use frame = Frame(root,bg="red", width=500, height = 100).pack() instead then frame will get 
        a value of Frame wich is not packed. As a result anything likeLabel(frame, text="hello", anchor=W, bg="green").pack()
        will not give proper result 
        
        """
        frame.pack(fill="x")


        padX = 200
        WIDTH = 8

        """
         = Frame(frame, bg="yellow")
        left.pack(side=CENTER, padx=(padX,0))

        right = Frame(frame, bg="yellow")
        right.pack(side=RIGHT, padx=(0, padX))

        frame.pack(fill="x")

        """
        self.word = tk.StringVar()

        #self.kor.set("")
        label1 = Label(frame, textvariable = self.word, width=WIDTH, font=(FONT_NAME_LARGE, Conf.FONT_SIZE_LARGE), anchor=CENTER, bg="green")
        label1.pack(pady=(50,50))

        """
        self.eng = tk.StringVar()

        label2 = Label(right, textvariable = self.eng, width=WIDTH, font=(FONT_NAME_LARGE, Conf.FONT_SIZE_LARGE), anchor=W, bg="green")
        label2.pack(pady=(50,50))

        """

        btnFrame = Frame(frame, bg="yellow")
        btnFrame.pack(side=TOP, fill="x")

        Button(btnFrame, text="Next", command=self.PrintNext).pack(side=LEFT, anchor=W, padx=(padX, 0))

        Button(btnFrame, text="Flip", command=self.Flip).pack(side=RIGHT, anchor=E, padx=(0, padX))

        control = Frame(self.root, bg="cyan")

        control.pack(fill="x", side=BOTTOM)

        padX = 200
        reload = Frame(control)
        reload.pack(side = LEFT, padx=(padX,0))

        group = Frame(reload)
        group.pack(side = LEFT)

        self.isRandom = tk.IntVar()    # v should be self v to make it persistent

        Radiobutton(group, text="In Seq", padx=20, variable=self.isRandom, value=1).pack(anchor=W)
        Radiobutton(group, text="Random", padx=20, variable=self.isRandom, value=2).pack(anchor=W)

        self.isRandom.set(self.finder.isRandom+1)
        reloadBtn = Button(reload, text="Reset", command=self.Reset, anchor=W, bg="green").pack(side=RIGHT, anchor=CENTER)


        Button(control, text="Quit", command=self.root.quit).pack(side=RIGHT, padx=(0,100))

        #button = Button(frame, text="click me", side=RIGHT).pack()

        self.PrintNext()

    def PrintNext(self):
        self.flip = 0
        self.wordMeaning = self.finder.GetNext()
        self.Show()

    def Show(self):
        self.word.set(self.wordMeaning[self.flip+1])

    def Flip(self):
        self.flip = 1-self.flip
        self.Show()

    def Reset(self):
        place = self.isRandom.get()
        if place == Conf.SEQ_PLACE:
            isRandom = False
        elif place == Conf.RANDOM_PLACE:
            isRandom = True

        print(isRandom)

        self.finder.Reset(isRandom)
        self.PrintNext()


root = Tk()

def run():
    #SCREEN_WIDTH = root.winfo_screenwidth()
    #SCREEN_HEIGHT = root.winfo_screenheight()



    root.geometry("%dx%d" % (640, 380))

    root.configure(background="WHITE")

    root.resizable(False, False)

    root.title("Word Checker")

    finder = Finder(Conf.START_WITH_RANDOMNESS)
    view = View(root, finder)

    #view.Display()


    root.bind("<Key>", key)

    root.mainloop()




#    print('Exiting main program')


def key(event):
    print("pressed", repr(event.char))
    if event.char == 'q' or event.char == 'Q' or event.char == chr(27):
        root.quit()
        pass


if __name__ == '__main__':
    run()



