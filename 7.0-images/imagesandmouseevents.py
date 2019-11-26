from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.map_image = PhotoImage(file="map.gif")
        self.bus_image = PhotoImage(file="bus.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.map_frame = Frame()
        self.map_frame.configure(width=400, height=400)

        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0, y=0)
        self.map_image_label.configure(image=self.map_image)

        self.bus_image_label = Label(self.map_frame)
        self.bus_image_label.place(x=10, y=10)
        self.bus_image_label.configure(image=bus_image)

        def map_image_label(self):
            self.map_image_label = Label()
            self.map_image_label.configure(image=self.map_image)

        def bus_image_label(self):
            self.bus_image_label = Label()
            self.bus_image_label.configure(image=self.bus_image)

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()