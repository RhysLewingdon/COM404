from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources 520x520
        self.umbrella_image = PhotoImage(file="umbrella.gif")
        
        # set window attributes
        self.configure(height=1000,
                       width=1500)

        # set animation attributes
        self.umbrella_x_pos = 490
        self.umbrella_y_pos = 0
        self.umbrella_x_change = 1
        self.umbrella_y_change = 1
        
        # add components
        self.add_umbrella_image_label() 
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        if self.umbrella_x_pos > 980:
            self.umbrella_x_change = -1

        if self.umbrella_y_pos > 510:
            self.umbrella_y_change = -1

        if self.umbrella_x_pos < 0:
            self.umbrella_x_change = 1

        if self.umbrella_y_pos < 0:
            self.umbrella_y_change = 1
        
        self.umbrella_x_pos = self.umbrella_x_pos + self.umbrella_x_change

        self.umbrella_x_pos = self.umbrella_x_pos + self.umbrella_x_change
        self.umbrella_y_pos = self.umbrella_y_pos + self.umbrella_y_change
        self.umbrella_image_label.place(x=self.umbrella_x_pos, 
                                    y=self.umbrella_y_pos)
        self.after(10, self.tick)

    # the umbrella image
    def add_umbrella_image_label(self):
        self.umbrella_image_label = Label()
        self.umbrella_image_label.place(x=self.umbrella_x_pos,
                                    y=self.umbrella_y_pos)
        self.umbrella_image_label.configure(image=self.umbrella_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop()