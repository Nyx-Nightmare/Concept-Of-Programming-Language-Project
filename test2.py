from pythonGraph import *

WINDOW_WIDTH  = 1800
WINDOW_HEIGHT = 800

pythonGraph.open_window(WINDOW_WIDTH,WINDOW_HEIGHT)
pythonGraph.set_window_title("Rocket Simulation test2")
pythonGraph.clear_window("BLACK")

Rocket = draw_image('files/rocket.png',140,645,50,55)
LaunchLand = draw_rectangle(0,700,300,800,'GREEN',True)
Sea = draw_rectangle(300,720,1800,800,'LIGHT_BLUE',True)
Boat = draw_image('files/boat.png',600,680,100,50)

pythonGraph.wait_for_close()