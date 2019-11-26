from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.cacti_image = PhotoImage(file="cacti.gif")
        self.cactinames_image = PhotoImage(file="cactinames.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_cactusleaves_label()
        #self.add_cacti_image_label()
        self.add_flip_button()
        #self.add_cactinames_image_label()

    def add_cactusleaves_label(self):
        self.add_cactusleaves_label = Label()
        self.add_cactusleaves_label.grid(row=0, column=0)
        self.add_cactusleaves_label.configure(font = "Arial 20", text = "Cactus Leaves")

    def add_cacti_image_label(self):
        self.cacti_image_label = Label()
        self.cacti_image_label.grid(row=1, column=0)
        self.cacti_image_label.configure(image=self.cacti_image,
                                             height=655,
                                             width=500)

    def add_cactinames_image_label(self):
        self.cactinames_image_label = Label()
        self.cactinames_image_label.grid(row=1, column=0)
        self.cactinames_image_label.configure(image=self.cactinames_image,
                                             height=655,
                                             width=500)

    def add_flip_button(self):
        self.add_flip_button = Button()
        self.add_flip_button.grid(row=2, column=0)
        self.add_flip_button.configure(font = "Arial 16", text = "FLIP", width=20)

        self.add_flip_button.bind("<ButtonRelease-1>", self.add_flip_button1_clicked)
        self.add_flip_button.bind("<ButtonRelease-3>", self.add_flip_button3_clicked)

    def add_flip_button1_clicked(self, event):
        self.add_cacti_image_label()

    def add_flip_button3_clicked(self, event):
        self.add_cactinames_image_label()

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
