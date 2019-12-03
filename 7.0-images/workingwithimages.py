from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.ambulance_image = PhotoImage(file="ambulance.gif")
        self.bike_image = PhotoImage(file="bike.gif")
        self.plane_image = PhotoImage(file="plane.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_transport_label()
        self.add_ambulance_image_label()
        self.add_bike_image_label()
        self.add_plane_image_label()

    def add_transport_label(self):
        self.add_transport_label = Label()
        self.add_transport_label.grid(row=0, column=0, columnspan=3)
        self.add_transport_label.configure(font = "Arial 14", text = "TRANSPORT")
        
    def add_ambulance_image_label(self):
        self.ambulance_image_label = Label()
        self.ambulance_image_label.grid(row=1, column=0)
        self.ambulance_image_label.configure(image=self.ambulance_image,
                                             height=60,
                                             width=60)
        self.ambulance_image_label.bind("<Button-1>", self.ambulance_clicked)

    def add_bike_image_label(self):
        self.bike_image_label = Label()
        self.bike_image_label.grid(row=1, column=1)
        self.bike_image_label.configure(image=self.bike_image,
                                             height=60,
                                             width=60)
        self.bike_image_label.bind("<Button-1>", self.bike_clicked)
 
    def add_plane_image_label(self):
        self.plane_image_label = Label()
        self.plane_image_label.grid(row=1, column=2)
        self.plane_image_label.configure(image=self.plane_image,
                                             height=60,
                                             width=60)
        self.plane_image_label.bind("<Button-1>", self.plane_clicked)

    def ambulance_clicked(self, event):
        messagebox.showinfo("Ambulance title.", "Ambulance.")

    def bike_clicked(self, event):
        messagebox.showinfo("Bike title.", "Bike.")
    
    def plane_clicked(self, event):
        messagebox.showinfo("Plane title.", "Plane.")
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()