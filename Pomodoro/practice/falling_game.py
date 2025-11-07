# A small game is a fantastic idea to practice the `Canvas`\! Let's make a simple **"Catch the Falling Square"** game. This game will involve:
#
#   * Creating a moving object (`canvas.create_rectangle`).
#   * Moving an object based on user input (`canvas.move`).
#   * Detecting collisions (simple overlap check).
#   * Updating text on the canvas (`canvas.itemconfig`).
#   * Using `window.after()` for game animation loop.
#
# Here are the step-by-step instructions:
#
# -----
#
# ## 🎮 Game Practice: Catch the Falling Square\!
#
# **Concept:** A small "player" square moves horizontally at the bottom of the screen. Larger "fruit" squares fall from the top. The player scores points by catching the fruit. If fruit hits the bottom, the player loses.
#
# ### Game Structure Breakdown
#
# 1.  **Canvas Setup:** Create the game area.
import random
from  tkinter import *



# 2.  **Player Square:** A controllable rectangle.
# Create a rectangle

# Movement step size
STEP = 10
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 500
PLAYER_SIZE = 40
PLAYER_SPEED = 20
FRUIT_SIZE = 30
FRUIT_FALL_SPEED = 5
GAME_SPEED_MS = 50

player_id = None
fruit = None
game_active = True
game_loop_timer = None
score = 0



# def move_left(event):
#     canvas.move(player, -STEP, 0)
#
#
# def move_right(event):
#     canvas.move(player, STEP, 0)
#
# # Bind arrow keys
# window.bind("<Left>", move_left)
# window.bind("<Right>", move_right)
# # 3.  **Falling Square (Fruit):** A rectangle that moves downwards automatically.
# rect2 = canvas.create_rectangle(180, 50, 220, 90, fill="dodgerblue")
#
# # Speed (pixels per frame)
# speed = 4
#
# def move_down():
#     # Move the rectangle down
#     canvas.move(rect2, 0, speed)
#
#     # Get the rectangle’s current coordinates
#     x1, y1, x2, y2 = canvas.coords(rect2)
#
#     # Stop at the bottom or reset to top (choose one)
#     if y2 < 400:
#         window.after(30, move_down)  # Move again after 30ms
#     else:
#         # Uncomment one of these lines:
#         # pass  # Stop at bottom
#         canvas.coords(rect2, 180, 0, 220, 40)  # Reset to top and keep going
#         window.after(30, move_down)
#
# move_down()

# 4.  **Movement Logic:** Functions for moving the player and the fruit.
# 5.  **Game Loop:** Uses `window.after()` to animate.
# 6.  **Collision Detection:** Check if player and fruit squares overlap.
# 7.  **Scoring & Game Over:** Update score text and handle game end.
#
# ### Instructions 🕹️
#
# ### Step 1: Initialize Game Variables and Canvas
#
# 1.  **Import Tkinter:**
#     ```python
#     from tkinter import *
#     import random # You'll need this for random fruit positions
#     ```

#       * `score = 0`
#       * `game_active = True` (boolean to control game state)
#       * `player_id = None`
#       * `fruit_id = None`
#       * `score_text_id = None` (for updating score on canvas)
#       * `game_over_text_id = None`
#       * `game_loop_timer = None` (to cancel the `window.after` loop)
# 4.  **Create Main Window:** `window = Tk()` and give it a title.
# 5.  **Create Canvas:** `canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="lightblue")`.
#
window = Tk()
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="lightblue")


canvas.pack()
# ### Step 2: Create Player and Falling Fruit
#

# 1.  **Draw Player:**
#       * Define a function `create_player()`:
def create_player():
    global player_id
    player_id = canvas.create_rectangle(180 , 400, 230, 450, fill="#FFB6C1", outline="#e2979c", )
    print("player -id",player_id)
create_player()
def create_fruit():
    global fruit
    random_x = random.randint(0,350)
    y1 = 3
    fruit = canvas.create_rectangle(random_x,y1,random_x + 50,y1+50,fill="navyblue")
    print("fruit",fruit)
create_fruit()

#           * Calculate the initial position for the player at the bottom center of the canvas.
#           * Use `canvas.create_rectangle(x1, y1, x2, y2, fill="blue")` to draw the player.
#           * Store the ID in `player_id`.
#       * Call `create_player()` in your main setup.
# 2.  **Draw Initial Fruit:**
#       * Define a function `create_fruit()`:
#           * Generate a random X-coordinate for the fruit, ensuring it stays within canvas bounds.
#           * Set its Y-coordinate to the top (`y1=0`).
#           * Use `canvas.create_rectangle(x1, y1, x2, y2, fill="red")` to draw the fruit.
#           * Store the ID in `fruit_id`.
#       * Call `create_fruit()` in your main setup.

#-----------------------------------------------------------
# 3.  **Display Score:**
#       * Use `canvas.create_text()` to display the initial score (e.g., "Score: 0") somewhere on the canvas (e.g., top-left). Store its ID in `score_text_id`.
score_text_id = canvas.create_text(50,15,text=f"Score : {score}",font=("Times New Roman",18,"bold"))

# ### Step 3: Player Movement (Keyboard Bindings)

#
# 1.  **Movement Functions:**
#       * Define `move_player_left(event)`:
def move_player_left(event):
    global player_id
    player_coords = canvas.coords(player_id)
    if player_coords[0] > 0:
        canvas.move(player_id, -PLAYER_SPEED, 0)

def move_player_right(event):
    global player_id
    player_coords = canvas.coords(player_id)
    if player_coords[2] < 400:
        canvas.move(player_id, PLAYER_SPEED, 0)


window.bind("<Left>", move_player_left)
window.bind("<Right>", move_player_right)
#           * Get the current coordinates of the player using `canvas.coords(player_id)`.
#           * Check if the player is not at the far left edge.
#           * If not, use `canvas.move(player_id, -PLAYER_SPEED, 0)` to move it left.
#       * Define `move_player_right(event)`:
#           * Similar to left, but check the right edge and use `canvas.move(player_id, PLAYER_SPEED, 0)`.
# 2.  **Bind Keys:**
#       * Use `window.bind("<Left>", move_player_left)` to bind the left arrow key.
#       * Use `window.bind("<Right>", move_player_right)` to bind the right arrow key.
#
# ### Step 4: Game Logic (Main Game Loop)
#
# 1.  **Define `game_loop()`:** This will be called repeatedly.
# 2.  **Check Game State:**
#       * If `game_active` is `False`, use `canvas.after_cancel(game_loop_timer)` and return (stop the loop).
# 3.  **Move Fruit:**
#       * Use `canvas.move(fruit_id, 0, FRUIT_FALL_SPEED)` to make the fruit fall.

# 4.  **Get Coordinates for Collision:**
#       * Get `player_coords = canvas.coords(player_id)`
#       * Get `fruit_coords = canvas.coords(fruit_id)`
# 5.  **Collision Detection:**
def game_loop():
    global game_active,fruit,FRUIT_FALL_SPEED,score
    if game_active == False:
        #canvas.after_cancel(game_loop_timer)
        return
    print("fruit FALL",FRUIT_FALL_SPEED)
    canvas.move(fruit,0, FRUIT_FALL_SPEED)
    player_coords = canvas.coords(player_id)
    fruit_coords = canvas.coords(fruit)
    horiz_check =(fruit_coords[0] <= player_coords[2]) and (fruit_coords[2] >= player_coords[0])
    if fruit_coords[3] >= player_coords[1] and horiz_check:#(fruit_coords[0],fruit_coords[2]) == range(player_coords[0],player_coords[2]):
        score += 1
        canvas.itemconfig(score_text_id, text=f"Score: {score}")
        canvas.delete(fruit)
        create_fruit()

    elif fruit_coords[3] >= CANVAS_HEIGHT:
        game_active = False
        game_over_text_id = canvas.create_text(200,250,text="GAME OVER",font=("Areial",24,"bold"))

        window.after_cancel()
        return

    game_loop_timer = window.after(GAME_SPEED_MS, game_loop)




#       * **Check if caught:** If `fruit_coords[3]` (bottom of fruit) is greater than or equal to `player_coords[1]` (top of player) AND the fruit's horizontal range (`fruit_coords[0]` to `fruit_coords[2]`) overlaps with the player's horizontal range (`player_coords[0]` to `player_coords[2]`):
#           * Increment `score`.
#           * Update score text: `canvas.itemconfig(score_text_id, text=f"Score: {score}")`.
#           * Delete old fruit: `canvas.delete(fruit_id)`.
#           * Create new fruit: `create_fruit()`.
#       * **Check if missed (hit bottom):** If `fruit_coords[3]` (bottom of fruit) is greater than `CANVAS_HEIGHT`:
#           * Set `game_active = False`.
#           * Display "GAME OVER\!" text on the canvas: `game_over_text_id = canvas.create_text(...)`.
#           * Cancel the game loop (`window.after_cancel`).
# 6.  **Schedule Next Loop:** `game_loop_timer = window.after(GAME_SPEED_MS, game_loop)`.
#
# ### Step 5: Start Game and Run Main Loop
#
# 1.  **Start Game:**
def start_game():
    score = 0
    game_active = True
    # create_player()
    # create_fruit()
    game_loop()
start = Button(text="Start",command=start_game)
#       * Define a function `start_game()`:
#           * Reset `score = 0`, `game_active = True`.
#           * Call `create_player()` and `create_fruit()`.
#           * Call `game_loop()` to begin the animation.
# 2.  **Add Start/Reset Button (Optional but good):**
#       * Create a `Button` labeled "Start Game" that calls `start_game()`.
# 3.  **Pack/Grid Widgets:** Place your canvas and button(s).
start.pack()
# 4.  **`window.mainloop()`:** Run the Tkinter event loop.
window.mainloop()
# -----
#
# This game will be a fantastic way to consolidate many `Canvas` concepts. It also introduces event binding and game loop structures common in simple GUI games. Good luck to your kid, and have fun building it\!