
from tkinter import Tk, Entry, W, E, N, S, PhotoImage, Checkbutton, Button, Radiobutton, \
        Menu, Frame, Label, LEFT, RIGHT, TOP, BOTTOM, NW, NE, SW, CENTER

import tkinter as tk

from tkinter import ttk

from conf import Conf
from finder import Finder

from word_modify_dlg import *

from native_cpp import *


#FONT_SIZE_NORMAL = 12
#FONT_SIZE_SMALL = 8

#FONT_NAME_LARGE = 'TkDefaultFont'
#FONT_NAME_NORMAL = 'TkDefaultFont'
#FONT_NAME_SMALL = 'TkDefaultFont'

#root = Tk()


class ChangeWord:
    def __init__(self, root, parent):
        self.root = root
        self.parent = parent
        #self.parent.wm_attributes("-disable", True)
        #self.parent.()

        self.Display()

    def Display(self):

        #win = tk.Toplevel()
        self.root.wm_title("Window")

        l = tk.Label(self.root, text="Input")
        l.grid(row=0, column=0)

        b = tk.Button(self.root, text="Okay", command=self.Destroy)
        b.grid(row=1, column=0)

    def Destroy(self):
        #self.parent.wm_attributes("-disable", False)
        #root.grab_release()
        root.destroy()



class View:
    def __init__(self, _root, _finder):
        self.root = _root
        self.finder = _finder
        #Frame.__init__(self, root)
        #button1 = Button(self.root, text="Quit", command=root.quit, anchor=W)
        #button1.pack()
        self.Display()

    def Display(self):

        frame = Frame(self.root)
        self.mainFrm = frame
        """
        if we use frame = Frame(root,bg="red", width=500, height = 100).pack() instead then frame will get 
        a value of Frame wich is not packed. As a result anything likeLabel(frame, text="hello", anchor=W, bg="green").pack()
        will not give proper result 
        
        """
        frame.pack(fill="x")


        padX = 200
        WIDTH = 20
        HEIGHT = 10

        """
         = Frame(frame, bg="yellow")
        left.pack(side=CENTER, padx=(padX,0))

        right = Frame(frame, bg="yellow")
        right.pack(side=RIGHT, padx=(0, padX))

        frame.pack(fill="x")

        """

        self.repeatingText = tk.StringVar()
        self.repeatingText.set("")
        Label(frame, textvariable=self.repeatingText, width = 10
              , font=(Conf.FONT_NAME_SMALL, Conf.FONT_SIZE_SMALL), fg="red").pack(fill="none", expand=True, pady=(20, 10))    # place the widget at the middle


        self.word = tk.StringVar()

        #self.kor.set("")
        #wordLabel = Label(frame, textvariable = self.word, width=WIDTH, font=(Conf.FONT_NAME_LARGE, Conf.FONT_SIZE_LARGE), anchor=CENTER, bg="white")
        #wordLabel.pack(pady=(0,50))

        #wordLabel.bind("<Button>", lambda x: (Dialog(frame)))

        #print(type(wordLabel))


        self.word.set("hello")
        btn_color = "white"
        style = ttk.Style()
        style.configure('TButton', padding=(0,5), background=btn_color, borderwidth=-1, highlightthickness='20', relief="flat", font=(Conf.FONT_NAME_LARGE, Conf.FONT_SIZE_LARGE), width=WIDTH)
        style.map("TButton",
                  #foreground=[('pressed', 'red'), ('active', 'blue')],
                  background=[('pressed', '!disabled', 'white'), ('active', 'white')],
                  highlightcolor=[('focus', 'green'),
                                  ('!focus', 'red')],
                  relief=[('pressed', 'sunken'),
                          ('!pressed', 'flat')]
                  )


        backbutton = ttk.Button(frame, command=self.ModifyWord, textvariable=self.word)
        backbutton.pack(pady=(0, 50))
        """
        self.eng = tk.StringVar()

        label2 = Label(right, textvariable = self.eng, width=WIDTH, font=(FONT_NAME_LARGE, Conf.FONT_SIZE_LARGE), anchor=W, bg="green")
        label2.pack(pady=(50,50))

        """

        btnFrame = Frame(frame)
        btnFrame.pack(side=TOP, fill="x")
        """
        uisng side = TOP annchor W, E does not work in the next case...in that case second button goes below to the 
        first one
        """

        padY = 50
        padX = 197

        Button(btnFrame, text="Prev", command=self.ClickPrev(), height=1).pack(side=LEFT, anchor=E,
                                                                             padx=(padX, 0), pady=(0, padY))

        Button(btnFrame, text="Next", command=self.ClickNext, height=1).pack(side=RIGHT, anchor=W,
                                                                             padx=(0, padX), pady=(0, padY))


        btn = Button(btnFrame, text="Flip", command=self.Flip)
        btn.pack(side=TOP, anchor=CENTER, pady=(0, padY))

        #self.root.config(state="disabled")

        """    
        self.root.update()
        height = nextCmdBtn.winfo_height()
        print("height is %d" % height)
        """

        control = Frame(self.root)





        padY = 10
        control.pack(fill="both", side=TOP)

        padX = 200
        reload = Frame(control)
        reload.pack(side = LEFT, padx=(padX,0))

        group = Frame(reload)
        group.pack(side = LEFT)

        self.isRandom = tk.IntVar()    # v should be self v to make it persistent

        Radiobutton(group, text="In Seq", padx=20, variable=self.isRandom, value=1).pack(anchor=W)
        Radiobutton(group, text="Random", padx=20, variable=self.isRandom, value=2).pack(anchor=W)

        self.isRandom.set(self.finder.isRandom+1)
        reloadBtn = Button(reload, text="Reset", command=self.Reset, anchor=W).pack(side=RIGHT, anchor=CENTER)


        #Button(control, text="Quit", command=self.root.quit).pack(side=RIGHT, padx=(0,50))

        Frame(self.root, height = 60).pack(fill="x")
        #testFrm.pack(fill="x")
        #btn = Button(testFrm, text="Test")
        #btn.pack(fill="y")

        #button = Button(frame, text="click me", side=RIGHT).pack()

        self.PrintNext(False)


    def ModifyWord(self):
        (words, index) = self.finder.GetCurr()
        dlg = WordModifyDlg(self.mainFrm, "Modify", word=words[2])

        if dlg.result != None and words[2] != dlg.result:
            print("goint to modify")


    def WordToChange(self, event):
        print("mouse clicked at x=" + str(event.x) + " y=" + str(event.y))
        #self.popup_bonus()
        #win = tk.Toplevel(root)
        #win.grab_set()
        #ChangeWord(win, root)
        #root.wait_window(win)
        #win.grab_set()
        self.open_toplevel_window()

        #Dialog(root)

    def open_toplevel_window(self):
        self.top = Toplevel(self.root)
        # this forces all focus on the top level until Toplevel is closed
        self.top.grab_set()

        def replace_text():
            self.text.delete(1.0, END)
            self.text.insert(END, "Text From\nToplevel")

        top_button = Button(self.top, text="Replace text in main window",
                            command=replace_text)
        top_button.pack()

    def popup_bonus(self):
        win = tk.Toplevel()
        win.wm_title("Window")

        l = tk.Label(win, text="Input")
        l.grid(row=0, column=0)

        b = tk.Button(win, text="Okay", command=win.destroy)
        b.grid(row=1, column=0)

    def ClickNext(self):
        self.PrintNext(True)
    def ClickPrev(self):
        self.PrintNext(True, False)

    def PrintNext(self, showRepeatingMsg, forward = True):
        self.flip = 0
        (self.wordMeaning, index)= self.finder.GetNext(forward)
        flag = index == 0 and showRepeatingMsg;
        self.Show(flag)

    def Show(self, flag):
        self.word.set(self.wordMeaning[self.flip+1])
        if flag:
            self.repeatingText.set("Repeating...")
        else:
            self.repeatingText.set("")


    def Flip(self):

        self.flip = 1-self.flip
        self.Show(False)

    def Reset(self):
        place = self.isRandom.get()
        if place == Conf.SEQ_PLACE:
            isRandom = False
        elif place == Conf.RANDOM_PLACE:
            isRandom = True

        #print(isRandom)

        self.finder.Reset(isRandom)
        self.PrintNext(False)


import inspect

def test(a, b, c):
    return a+b+c

root = Tk()

finder = Finder(Conf.START_WITH_RANDOMNESS)
view = View(root, finder)
def run():
    #SCREEN_WIDTH = root.winfo_screenwidth()
    #SCREEN_HEIGHT = root.winfo_screenheight()

    hi = hello('Hasan')
    #print(hi.greet())

    mySplit = split("my_goodness how are you \n \r")

    #print(type(root.wm_attributes()))


    kor = "NULL"
    str = "test"
    kor = mySplit.kor
    eng = mySplit.eng
    #print("kor is %s %s" % (kor, eng))

    root.geometry("%dx%d" % (640, 290))

    root.configure(background="WHITE")

    root.resizable(False, False)

    root.title("Word Checker")

    #root['state'] = 'disabled'

    #print(tk.ttk.Style.configure().keys())

    func = tk.ttk.Style().configure

    print(ttk.Style().lookup("TButton", "border"))
    #view.Display()


    root.bind("<Key>", key)
    root.bind('<Left>', leftKey)
    root.bind('<Right>', rightKey)

    root.mainloop()




#    print('Exiting main program')

def leftKey(event):
    #print ("Left key pressed")
    view.ClickPrev()

def rightKey(event):
    #print ("Right key pressed")
    view.ClickNext()

def key(event):
    #print("pressed", repr(event.char))
    if event.char == 'q' or event.char == 'Q' or event.char == chr(27):
        root.quit()
    elif event.char == 'f':
        view.Flip()


if __name__ == '__main__':
    run()



