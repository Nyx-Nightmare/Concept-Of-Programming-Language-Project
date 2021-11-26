# ---------------------------------------------------------------------
# Rocket Landing Simulator
# Gate Check: 1
# ---------------------------------------------------------------------
import random, math
from typing import Tuple
from pythonGraph import *

# CONSTANTS
WINDOW_WIDTH  = 1800
WINDOW_HEIGHT = 800

# Performance Variables

# Simulation Variables

# Terrain
GROUND_HIEGHT = 100
GROUND_WIDTH = 200
WATER_HEIGHT = 300
Y_COORDINATE = []

# Rocket
global Rocket_X_Coordinate , Rocket_Y_Coordinate , Rocket_X_Velocity , Rocket_Y_Velocity , Rocket_Height , Rocket_Width
Rocket_X_Coordinate = 0
Rocket_Y_Coordinate = 0
Rocket_X_Velocity = 0
Rocket_Y_Velocity = 0
Rocket_Height = 50
Rocket_Width = 50

# Boat (i.e., Landing Pad)
global B_X_Coordinate , B_Y_Coordinate , B_Initial_X , B_Initial_Y , B_Velocity , B_Initial_V , B_Width , B_Height
B_X_Coordinate = 0
B_Y_Coordinate = 0
B_Initial_X = 0
B_Initial_Y = 0
B_Velocity = 0
B_Initial_V = 0
B_Width = 200
B_Height = 50

# --------------------------------------------------------------
# Initializes the Simulation
# --------------------------------------------------------------
def initialize_simulation(generate_new_scenario):
    initialize_terrain(True)
    initialize_boat(True)
    initialize_rocket(True)
     

# --------------------------------------------------------------
# Initializes the Terrain
# --------------------------------------------------------------
def initialize_terrain(generate_new_scenario):
    global GROUND_HIEGHT , GROUND_WIDTH , WATER_WIDTH , WATER_HEIGHT
    GROUND_WIDTH = random.randint(100,WINDOW_WIDTH*0.2)
    GROUND_HIEGHT = random.randint(100,WINDOW_HEIGHT*0.3)
    WATER_WIDTH = WINDOW_WIDTH - GROUND_WIDTH
    WATER_HEIGHT = random.randint(50,GROUND_HIEGHT-10)


# --------------------------------------------------------------
# Initializes the Boat
# --------------------------------------------------------------
def initialize_boat(generate_new_scenario):
    global B_X_Coordinate , B_Y_Coordinate , B_Initial_X , B_Initial_Y , B_Velocity , B_Initial_V , B_Width , B_Height
    if(generate_new_scenario):
        B_Initial_X = random.randint(GROUND_WIDTH,WINDOW_WIDTH-B_Width)
        B_Initial_Y = WINDOW_HEIGHT - WATER_HEIGHT - B_Height
        B_Initial_V = random.randint(-2,2)
    B_X_Coordinate = B_Initial_X
    B_Y_Coordinate = B_Initial_Y
    B_Velocity = B_Initial_V

# --------------------------------------------------------------
# Initializes the Rocket
# --------------------------------------------------------------
def initialize_rocket(generate_new_scenario):
    global Rocket_X_Coordinate, Rocket_Y_Coordinate, Rocket_X_Velocity, Rocket_Y_Velocity
    Rocket_X_Coordinate = (GROUND_WIDTH / 2) - (Rocket_Width / 2)
    Rocket_Y_Coordinate = WINDOW_HEIGHT - GROUND_HIEGHT - Rocket_Height
    Rocket_X_Velocity = 0.0
    Rocket_Y_Velocity = 0.0


# --------------------------------------------------------------
# Draws all of the in game objects
# --------------------------------------------------------------
def erase_objects():
    clear_window("BLACK")


# --------------------------------------------------------------
# Draws all of the in game objects
# --------------------------------------------------------------
def draw_objects():
    draw_terrain()
    draw_rocket()
    draw_hud()
    draw_boat()
    
  

# --------------------------------------------------------------
# Draws the Terrain
# --------------------------------------------------------------
def draw_terrain():
    # GROUND
    # x width , y hight
    x1 = 0
    y1 = WINDOW_HEIGHT - GROUND_HIEGHT
    x2 = GROUND_WIDTH
    y2 = WINDOW_HEIGHT
    draw_rectangle(x1,y1,x2,y2,'GREEN',True)
    # WATER
    x1 = GROUND_WIDTH
    y1 = WINDOW_HEIGHT - WATER_HEIGHT
    x2 = WINDOW_WIDTH
    y2 = WINDOW_HEIGHT
    draw_rectangle(x1,y1,x2,y2,'LIGHT_BLUE',True)
   

# --------------------------------------------------------------
# Draws the Boat
# --------------------------------------------------------------
def draw_boat():
    draw_image('files/boat.png',B_X_Coordinate,B_Y_Coordinate,B_Width,B_Height)


# --------------------------------------------------------------
# Draws the Rocket (and Thrusters)
# --------------------------------------------------------------
def draw_rocket():
    draw_image('files/rocket.png',Rocket_X_Coordinate,Rocket_Y_Coordinate,Rocket_Width,Rocket_Height)


# --------------------------------------------------------------
# Draws the On Screen Text
# --------------------------------------------------------------
def draw_hud():
    pass


# --------------------------------------------------------------
# Updates all animated objects
# --------------------------------------------------------------
def update_objects():
    pass


# --------------------------------------------------------------
# Updates the Rocket
# --------------------------------------------------------------
def update_rocket():
    pass


# --------------------------------------------------------------
# Updates the Landing Pad / Boat
# --------------------------------------------------------------
def update_boat():
    pass


# --------------------------------------------------------------
# Checks for Manual (or eventually) AI Input
# --------------------------------------------------------------
def get_input():
    pass


# --------------------------------------------------------------
# Detects if the Rocket has hit the ground or a boundry
# --------------------------------------------------------------
def is_simulation_over():
    return False


# --------------------------------------------------------------
# Analyzes the Results of the Simulation
# --------------------------------------------------------------
def analyze_results():
    pass
        

# -----------------------------------------------------
# "Main Program"
# -----------------------------------------------------
pythonGraph.open_window(WINDOW_WIDTH, WINDOW_HEIGHT)
pythonGraph.set_window_title("CS110Z (S20) Rocket Simulator - Mahmoud Shawish")  

# Initializes the Simulation At Least Once
initialize_simulation(True)
    
# Main "Game Loop"
while pythonGraph.window_not_closed():
    if is_simulation_over() == False:
        erase_objects()
        draw_objects()
        get_input()
        update_objects()
    else:
        analyze_results()
        initialize_simulation(False)
        
    pythonGraph.update_window()