from tkinter import Canvas


class Ball:
    def __init__(self,canvas,x,y,diameter,xvel,yvel,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter, diameter, fill=color)
        self.xvel = xvel
        self.yvel = yvel
        
    def move(self):
        coordinates = self.canvas.coords(self.image)
        #print(coordinates)

        if(coordinates[2]>= (self.canvas.winfo_width()) or coordinates[0]<0):
            self.xvel = -self.xvel
        if(coordinates[3]>= (self.canvas.winfo_height()) or coordinates[1]<0):
            self.yvel = -self.yvel

        self.canvas.move(self.image, self.xvel,self.yvel)
        
        
        
        
        
