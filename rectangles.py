import tkinter as tk

WINDOWTITLE = "Rectangles"
WINDOWSIZE = "800x600"
GAMEAREA = "800x600"

class Game:
    def __init__(self, root, GAMEAREA, gameTitle):
        self.root = root
        self.root.geometry(GAMEAREA)
        self.root.title(gameTitle)
        self.canvas = tk.Canvas(
                root, width=GAMEAREA.split("x")[0],
                height=GAMEAREA.split("x")[1], bg="white")
        self.canvas.pack()
        self.objects = []

    def start(self):
        self.root.bind("<KeyPress>", self.handleKeyPress)

    def create_player(self, Rectangle):
        self.player = Rectangle
        self.player.draw(self.canvas)

    def create_object(self, obj):
        self.objects.append(obj)
        obj.draw(self.canvas)

    def handleKeyPress(self, event):
        moves = {
            "Up": (0, -10),
            "Down": (0, 10),
            "Left": (-10, 0),
            "Right": (10, 0)
            }
        if event.keysym in moves:
            if not (self.player.is_out_of_bounds(
                GAMEAREA, *moves[event.keysym])
                    or self.player.is_colliding_rect(*moves[event.keysym],
                                                     self.objects[0])):

                self.player.move(self.canvas, *moves[event.keysym])
                print(self.objects[0].x)


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
        self.x += dx
        self.y += dy
        canvas.move(self.canvas_id, dx, dy)

    def is_out_of_bounds(self, GAMEAREA, dx, dy):
        width, height = map(int, GAMEAREA.split("x"))
        if(self.x + self.width + dx >= width or self.y + self.height + dy >= height
           or self.x + dx <= 0 or self.y + dy <= 0):
            return True
        return False

    def is_colliding_rect(self, dx, dy, rect):
        if not (self.x + self.width + dx < rect.x
                or rect.x + rect.width < self.x + dx
                or self.y + self.height + dy < rect.y
                or rect.y + rect.height < self.y + dy):
            return True
        return False



root = tk.Tk()
game = Game(root, GAMEAREA, WINDOWTITLE)
game.create_player(Rectangle(400, 300, 100, 100, "blue"))
game.create_object(Rectangle(200, 50, 100, 100, "red"))
game.start()
root.mainloop()
