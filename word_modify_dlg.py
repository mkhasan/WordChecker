from tkinter import *
from conf import Conf

class WordModifyDlg(Toplevel):

    def __init__(self, parent, title = None, labelWidth=20, word="animal"):

        Toplevel.__init__(self, parent)

        self.transient(parent)

        if title:
            self.title(title)

        self.parent = parent

        self.result = None

        self.labelWidth = labelWidth

        self.word = word

        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)


        self.Display()

        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("%dx%d" % (400, 200))

        self.initial_focus.focus_set()

        self.wait_window(self)

    #
    # construction hooks

    def body(self, master):
        # create dialog body.  return widget that should have
        # initial focus.  this method should be overridden

        pass

    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons

        box = Frame(self)

        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    #
    # standard button semantics

    def ok(self, event=None):

        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        self.cancel()

    def cancel(self, event=None):

        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()

    #
    # command hooks

    def validate(self):

        return 1 # override

    def apply(self):

        pass # override

    def Display(self):

        box = Frame(self)
        currMsg = Label(box, text="Current", font=(Conf.FONT_NAME_NORMAL, Conf.FONT_SIZE_NORMAL))
        currMsg.grid(row=0, column=0, sticky=W, padx=(0, 10))


        self.currStr = StringVar()
        self.modifiedStr = StringVar()

        self.currStr.set(self.word)
        self.modifiedStr.set(self.word)

        current = Label(box, textvariable=self.currStr, width=self.labelWidth, font=(Conf.FONT_NAME_LARGE, Conf.FONT_SIZE_LARGE), anchor=W, bg="white")
        current.grid(row=0, column=1, sticky=E)

        padY = 30

        modifyMsg= Label(box, text="Modified", font=(Conf.FONT_NAME_NORMAL, Conf.FONT_SIZE_NORMAL))
        modifyMsg.grid(row=1, column=0, sticky=W, padx=(0, 10), pady=(padY, 0))

        modified = Entry(box, width=self.labelWidth, textvariable=self.modifiedStr, font=(Conf.FONT_NAME_LARGE, Conf.FONT_SIZE_LARGE))
        modified.grid(row=1, column=1, sticky=E, pady=(padY, 0))

        padY = 20
        Button(box, text="Okay", command=self.on_ok).grid(row=2, column=1, sticky=W, pady=(padY, 0))
        Button(box, text="Cancel", command=self.cancel).grid(row=2, column=1, sticky=E, pady=(padY, 0))


        #wordLabel.bind("<Button>", lambda x: (Dialog(frame)))

        #print(type(wordLabel))

        box.pack()

    def on_ok(self):
        self.result = self.modifiedStr.get()
        self.ok()




if __name__ == '__main__':
    root = Tk()

    root.geometry("%dx%d" % (640, 290))

    root.configure(background="WHITE")

    root.resizable(False, False)

    root.title("Word Checker")

    test = WordModifyDlg(root, "test")

    print(test.result)

    if test.result == None:
        print("got None")

    root.mainloop()
