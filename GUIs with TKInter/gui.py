from tkinter import *

class Gui(Tk):
  # initialise window
    def __init__(self):
        super().__init__()

    # set window attributes
        self.geometry("334x173")
        self.title("Newsletter")
        self.configure(bg="#E0E0E0")

        self.fframe()
        self.fheading_label1()
        self.fheading_label2()
        self.finput_label()
        self.finput_box()
        self.fsubscribe_button()

    # add window components by
    # ...creating an object of the component stored in an attribute
    def fframe(self):
        #create
        self.frame = Frame()
        self.frame.place(x=10,y=10)
        #style
        self.frame.configure(bg="#F0F0F0",
                            height="153",
                            width="314")

    def fheading_label1(self):
        #create
        self.heading_label1 = Label()
        self.heading_label1.place(x=30, y=18)
        #style
        self.heading_label1.configure(font="Arial 14",
                                    text="RECEIVE OUR NEWSLETTER")

    def fheading_label2(self):
        #create
        self.heading_label2 = Label()
        self.heading_label2.place(x=11, y=65)
        #style
        self.heading_label2.configure(font="Arial 9",
                                    text="Please enter your email below to receive our newsletter.")

    def finput_label(self):
        #create
        self.input_label = Label()
        self.input_label.place(x=20, y=110)
        #style
        self.input_label.configure(font="Arial 9",
                                    text="Email:")

    def finput_box(self):
        #create
        self.input_box = Entry()
        self.input_box.place(x=70, y=110)
        #style
        self.input_box.configure(font="Arial 9",
                                    width="26")

    def fsubscribe_button(self):
        #create
        self.subscribe_button = Button()
        self.subscribe_button.place(x=12, y=140)
        #style
        self.subscribe_button.configure(font="Arial 9",
                                    text="Subscribe",
                                    width="43",
                                    bg="#F0E0E0")

    # ...assigning any event handlers to the component

  # handle events
  # (callback functions to handle events will go here)