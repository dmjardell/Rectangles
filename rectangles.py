import tkinter as tk

windowTitle = "Rectangles"
windowSize = "800x600"
gameArea = "800x600"

class Game:
    def __init__(self, root, gameArea, gameTitle):
        self.root = root
        self.root.geometry(gameArea)
        self.root.title(gameTitle)
        self.canvas = tk.Canvas(
                root, width=gameArea.split("x")[0],
                height=gameArea.split("x")[1], bg="white")
        self.canvas.pack()

        self.player = Rectangle(400, 300, 100, 100, "blue")
        self.player.draw(self.canvas)
        self.root.bind("<KeyPress>", self.handleKeyPress)

    def handleKeyPress(self, event):
        moves = { 
            "Up": (0, -10),
            "Down": (0, 10),
            "Left": (-10, 0),
            "Right": (10, 0)
            }
        if event.keysym in moves:
            self.player.move(self.canvas, *moves[event.keysym])





class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.canvas_id = None

    def draw(self, canvas):
        if self.canvas_id:
            canvas.coords(self.canvas_id, self.x, self.y, self.x + self.width,
                          self.y + self.height)
        else:
            self.canvas_id = canvas.create_rectangle(
                    self.x, self.y, self.x + self.width,
                    self.y + self.height, fill=self.color)
    def move(self, canvas, dx, dy):
        canvas.move(self.canvas_id, dx, dy)


root = tk.Tk()
game = Game(root, gameArea, windowTitle)
root.mainloop()
