import tkinter as tk

WINDOWTITLE = "Rectangles"
WINDOWSIZE = "800x600"
GAMEAREA = "800x600"
WIDTH, HEIGHT = 800, 600

class GameGUI:
    def __init__(self, game):
        self.root = tk.Tk()
        self.game = game
        self.root.geometry(GAMEAREA)
        self.root.title(WINDOWTITLE)
        self.canvas = tk.Canvas(width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()
        self.root.bind("<KeyPress>", self.handle_key_press)
        self.running = True

    def handle_key_press(self, event):
        moves = {
            "Up": (0, -10),
            "Down": (0, 10),
            "Left": (-10, 0),
            "Right": (10, 0)
            }
        if event.keysym in moves:
            print(f"Attempting to move player:{self.game.player.player_name}:{event.keysym}")
            if not (self.game.player.is_out_of_bounds(GAMEAREA, *moves[event.keysym])
                    or self.game.check_collisions(self.game.player, *moves[event.keysym])):
                print("move")
                self.game.player.move(self.canvas, *moves[event.keysym])
            else:
                print("Collision or out of bounds detected")
        print(f"{self.game.player.player_name}({self.game.player.x}, {self.game.player.y})")

    # Render all of the games' objects
    def render(self):
        if not self.game.objects:
            print("GameGUI.render() -> There are no objects to render.")
            return
        for obj in self.game.objects:
            obj.draw(self.canvas)


class Game:
    def __init__(self, game_area, game_title):
        self.objects = []
        self.game_area = game_area
        self.game_title = game_title

    def create_player(self, Player):
        self.player = Player
        self.objects.append(self.player)

    def create_object(self, obj):
        self.objects.append(obj)

    def check_collisions(self, this_object, dx, dy):
        for obj in self.objects:
            # Check if obj is the same object as this_object which would trigger a collision with it self
            if obj is this_object:
                continue
            if this_object.is_colliding_rect(dx, dy, obj):
                return True

        return False


class Rectangle:
    def __init__(self, *, x, y, width, height, color):
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
        if (self.x + self.width + dx >= width
           or self.y + self.height + dy >= height
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

class Player(Rectangle):
    def __init__(self, *, player_name, **kwargs):
        super().__init__(**kwargs)
        self.player_name = player_name


game = Game(GAMEAREA, WINDOWTITLE)
game.create_player(Player(x=400, y=300, width=100, height=100, color="blue", player_name="Player"))
game.create_object(Rectangle(x=200, y=50, width=100, height=100, color="red"))
game.create_object(Rectangle(x=90, y=500, width=50, height=90, color="red"))
gui = GameGUI(game)
gui.render()
gui.root.mainloop()
