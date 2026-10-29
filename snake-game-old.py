import tkinter
import random
from PIL import Image, ImageTk


ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#game window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False,False)

canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT,
                        borderwidth = 0 , highlightthickness = 1)
canvas.pack()
canvas.update()

# --- BACKGROUND IMAGE SETUP ---
# Load and resize background image
bg_image_pil = Image.open("Snake_bg.jpg") # Open your background file - change name here
bg_image_pil = bg_image_pil.resize((WINDOW_WIDTH, WINDOW_HEIGHT)) # Resize to fit game window
bg_photo = ImageTk.PhotoImage(bg_image_pil) # Convert to Tkinter photo image


#building game

snake = Tile(5*TILE_SIZE, 5*TILE_SIZE) #snake's head
food = Tile(15*TILE_SIZE, 15*TILE_SIZE) #food

snake_body = [] #snale tiles
vel_x = 0
vel_y = 0
game_over = False 

def change_direction(e): #event
    # print(e, e.keysym)
    global vel_x, vel_y, game_over
    
    if game_over :
        return
    
    if (e.keysym == "Up" and vel_y == 0 ):
        vel_x = 0
        vel_y = -1
    elif (e.keysym == "Down" and vel_y == 0 ):
        vel_x = 0
        vel_y = 1
    elif (e.keysym == "Left" and vel_x == 0):
        vel_x = -1
        vel_y = 0
    elif (e.keysym == "Right" and vel_x == 0):
        vel_x = 1
        vel_y = 0

def move():
    global snake, food, snake_body, game_over
    
    if game_over :
        return
    
    """ if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True
        return """
    
    if snake.x < 0 :
        snake.x = ROWS * TILE_SIZE
    if snake.x > ROWS * TILE_SIZE :
        snake.x = 0
    if snake.y > COLS * TILE_SIZE :
        snake.y = 0
    if snake.y < 0:
        snake.y = COLS * TILE_SIZE
    
    
    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y :
            game_over = True
            return 
    
    #collision
    if (snake.x == food.x and snake.y == food.y):
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS-1)*TILE_SIZE
        food.y = random.randint(0, ROWS-1)*TILE_SIZE
        
    #update snake body
    for i in range (len(snake_body)-1,-1,-1):
        tile = snake_body[i]
        if (i == 0):
            tile.x , tile.y = snake.x , snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y
        
    
    snake.x += vel_x*TILE_SIZE
    snake.y += vel_y*TILE_SIZE


   
def draw():
    global snake
    
    move()
    
    canvas.delete("all")
    
    #!!! THIS LINE WAS MISSING - THIS DRAWS YOUR BACKGROUND!!!
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)
    
    #draw food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE,
                            fill = "red")
    
    #draw snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE,
                            fill = "lime green")
    
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE,
                                fill = "green")
   
    
    window.after(100, draw) #300 milisec = 0.1 sec -> 10 fps
    

draw()


window.bind("<KeyRelease>", change_direction)
window.mainloop() #keeps the window open