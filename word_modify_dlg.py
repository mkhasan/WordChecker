from tkinter import *
from conf import Conf
from tkinter import ttk

class WordModifyDlg(Toplevel):

    def __init__(self, parent, title = None, labelWidth=20, kor="animal", eng="animal"):

        Toplevel.__init__(self, parent)

        self.transient(parent)

        if title:
            self.title(title)

        self.parent = parent

        self.result = None

        self.labelWidth = labelWidth

        self.words = (kor, eng)

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

        self.bind("<Key>", self.key)

        self.bind("<Button-1>", self.mouse_clicked)


        self.pop_up = None

        self.wait_window(self)

    #
    # construction hooks

    def mouse_clicked(self, event):
        print("left mouse clicked at " + str(event.x) + " " + str(event.y))
        if self.pop_up != None:
            print('going to destropy pop up')
            self.pop_up.destroy()
            self.pop_up = None

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

        currMsg = Label(box, text="Korean", font=(Conf.FONT_NAME_NORMAL, Conf.FONT_SIZE_NORMAL))
        currMsg.grid(row=0, column=0, sticky=W, padx=(0, 10))


        self.korStr = StringVar()
        self.engStr = StringVar()

        self.korStr.set(self.words[0])
        self.engStr.set(self.words[1])

        self.okayBtn = Button()
        okayCommand = self.register(self.check)

        self.kor = Entry(box, textvariable=self.korStr, state='readonly', width=self.labelWidth, font=(Conf.FONT_NAME_LARGE, Conf.FONT_SIZE_LARGE))
        self.kor.grid(row=0, column=1, sticky=E)

        padY = 30

        modifyMsg= Label(box, text="English", font=(Conf.FONT_NAME_NORMAL, Conf.FONT_SIZE_NORMAL))
        modifyMsg.grid(row=1, column=0, sticky=W, padx=(0, 10), pady=(padY, 0))

        modified = Entry(box, validate='key', validatecommand=(okayCommand, '%d', '%i', '%S', '%P'), width=self.labelWidth, textvariable=self.engStr, font=(Conf.FONT_NAME_LARGE, Conf.FONT_SIZE_LARGE))
        modified.grid(row=1, column=1, sticky=E, pady=(padY, 0))

        padY = 20

        self.okayBtn = Button(box, text="Okay", command=self.on_ok)
        self.okayBtn.grid(row=2, column=1, sticky=W, pady=(padY, 0))
        Button(box, text="Cancel", command=self.cancel).grid(row=2, column=1, sticky=E, pady=(padY, 0))

        self.kor.bind("<Button-3>", self.copy_selection)

        #wordLabel.bind("<Button>", lambda x: (Dialog(frame)))

        #print(type(wordLabel))

        box.pack()

    def popup_bonus(self):
        win = Toplevel(self)
        self.pop_up = win

        win.geometry("+%d+%d" % (self.winfo_rootx() + 50,
                                  self.winfo_rooty() + 50))
        win.wm_title("Window")

        l = Label(win, text="Input")
        l.grid(row=0, column=0)

        b = ttk.Button(win, text="Okay", command=self.pop_up_destroy)
        b.grid(row=1, column=0)

    def pop_up_destroy(self):
        self.pop_up.destroy
        self.pop_up = None

    def copy_selection(self, event):
        print(self.pop_up)

        if self.pop_up != None:
            self.pop_up.destroy
            return

        self.popup_bonus()
        print(str(event.x) + " " + str(event.y))
        try:
            print("my_selection: \n" + self.kor.selection_get())
        except:
            print("no selection")

    def on_ok(self):
        self.result = self.engStr.get()
        self.ok()


    def check(self, why, where, what, value):
        print(str(why) + "|" + str(where) + "|" + what + "|" + value)
        my_str = self.engStr.get()
        print(my_str)
        if value == self.words[1]:
            self.okayBtn.configure(text="Okay", fg="black")
        else:
            self.okayBtn.configure(text="Modify", fg="red")
        return True

    def key(self, event):
        print("pressed", repr(event.char))
        if event.char == chr(27):
            self.cancel()

def key(event):
    print("pressed", repr(event.char))
    if event.char == chr(27):
        root.quit()

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

    root.bind("<Key>", key)

    root.mainloop()

