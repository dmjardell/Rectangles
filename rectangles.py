import tkinter as tk

windowTitle = "Rectangles"
windowSize = "800x600"
gameArea = "800x600"
class Game:
    def __init__(self, root, gameArea, gameTitle):
        self.root = root
        self.root.gameArea(gameArea)
        self.root.gameTitle(gameTitle)
        self.canvas = tk.Canvas(root, width=gameArea.split("x")[0],height=gameArea.split("x")[1], bg="white")
        self.canvas.pack()

        self.player = Rectangle(100, 100, "blue")
        

#def key_handler(event):

class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(dx, dy)
        
        #def move(x, y):

    #code for controlling the rectangle

root = tk.Tk()
root.title(windowTitle)
root.geometry(gameArea)

canvas = tk.Canvas(root, width=gameArea.split("x")[0],height=gameArea.split("x")[1], bg="white")
canvas.pack()

rect1 = Rectangle(100,100,"blue")
canvas.create_rectangle(50, 25, rect1.width, rect1.height, fill=rect1.color)

root.mainloop()
