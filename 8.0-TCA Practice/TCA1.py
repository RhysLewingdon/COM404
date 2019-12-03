
from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # load resources
        self.default_image = PhotoImage(file="bike.gif")

        # set window properties
        self.title("Newsletter")
        self.configure(bg="#ccc", padx=10, pady=10)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_subscribe_button()
        self.__add_default_image()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure( bg="#eee", 
                                    padx=10, 
                                    pady=10)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(   bg="#eee",
                                        font="Arial 18",
                                        text="RECEIVE OUR NEWSLETTER",
                                        padx=10,
                                        pady=10)

    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(   bg="#eee",
                                            text="Please enter your email below to receiver our newsletter.",
                                            padx=10,
                                            pady=10)

    def __add_default_image(self):
        self.default_image_label = Label(self.outer_frame)
        self.default_image_label.grid(row=2, column=2)
        self.default_image_label.configure( image=self.default_image,
                                            padx=10,
                                            pady=10)

    def __add_email_label(self):
        self.email_label = Label(self.outer_frame)
        self.email_label.grid(row=2, column=0, sticky=E)
        self.email_label.configure( text="Email:",
                                    padx=10,
                                    pady=10)

    def __add_email_entry(self):
        self.email_entry = Entry(self.outer_frame)
        self.email_entry.grid(row=2, column=1, sticky=W)
        self.email_entry.configure(width=30)

    def __add_subscribe_button(self):
        self.subscribe_button = Button(self.outer_frame)
        self.subscribe_button.grid(row=3, column=0, columnspan=2, sticky=N+E+S+W)
        self.subscribe_button.configure(bg="#fee",
                                        text="Subscribe")


# main.py

#from gui import Gui

my_gui = Gui()
my_gui.mainloop()