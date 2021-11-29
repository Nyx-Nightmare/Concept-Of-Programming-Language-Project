from tkinter import *
import tkinter as tk
import random
import math
import time

# width of the animation window
window_width = 1800
# height of the animation window
window_height = 800
# initial x position of the rocket
rocket_start_xpos = 50
# initial y position of the rocket
rocket_start_ypos = 350
# initial x position of the boat
boat_start_xpos = 500
# initial y position of the boat
boat_start_ypos = 450
# initial x position of the pad
pad_start_xpos = 0
# initial y position of the pad
pad_start_ypos = 300
# the pixel movement of ball for each iteration
velocity = 0
# terrain start x
terrian_start_x = 0
# terrain start y
terrian_start_y = 454
# terrain height
terrian_height = 410
# terrain width
terrian_width = 211
# water start x
water_start_x = 0
# water start y
water_start_y = 510
# water height
water_height = 600
# water width
water_width = window_width
# delay between successive frames in seconds
animation_refresh_seconds = 0.16
# initial angel
angle = 0
# gravity
g = 9.81


def CreateWindow():
    window = tk.Tk()
    window.geometry(f'{window_width}x{window_height}')
    window.config(bg='gray12')
    return window


def CreatCanvas(window):
    def StartSimulation():
        v = textArea.get(1.0, "end-1c")
        a = textArea2.get(1.0, "end-1c")
        velocity = int(v)
        angle = int(a)
        window.update()
        StartAnimation(window, canvas, velocity, angle)

    def StartAnimation(window, canvas, v, a):

        rocket = PhotoImage(file='files/rocket.png')
        rocketMove = canvas.create_image(rocket_start_xpos, rocket_start_ypos,
                                         anchor=NW, image=rocket)
        Stime = 0
        global rocket_moveX, rocket_moveY
        rocket_moveX = 0
        rocket_moveY = 0
        #gets the size of the canvas
        canvasW, canvasH = canvas.size()
        #checks if it hits the boat or the edge of the water 
        while (rocket_moveX != boat_start_xpos and rocket_moveY != boat_start_ypos) and (rocket_moveY != water_height):
            print(Stime)
            rocket_moveX = int(v*math.cos(a))*Stime
            rocket_moveY = -int(v*math.sin(a)*Stime - g*math.pow(Stime, 2)*(1/2)) 
            canvas.move(rocketMove, rocket_moveX, rocket_moveY)
            time.sleep(animation_refresh_seconds)
            window.update()
            Stime += 1

        if rocket_moveX == boat_start_xpos and rocket_moveY == boat_start_ypos:
                result.config(text="SUCCESS")
                
        else:
            result.config(text="FAIL")

    def RestSimulation():
        
        global rocket_start_xpos, rocket_start_ypos, boat_start_xpos, boat_start_ypos, rocket_moveX, rocket_moveY
        rocket_start_xpos = 50
        rocket_start_ypos = 350
        boat_start_xpos = 500
        boat_start_ypos = 450
        rocket_moveX = 0
        rocket_moveY = 0
        result.config(text="")
        window.update()
        CreatCanvas(window)

    controlPanel = tk.Frame(window)
    controlPanel.grid()

    entryPanel = tk.Frame(controlPanel, width=100, height=20)
    entryPanel.grid(row=1, column=2)
    entryPanel.columnconfigure(0, weight=10)
    entryPanel.grid_propagate(False)

    entryPanel2 = tk.Frame(controlPanel, width=100, height=20)
    entryPanel2.grid(row=2, column=2)
    entryPanel2.columnconfigure(0, weight=10)
    entryPanel2.grid_propagate(False)

    label1 = tk.Label(controlPanel, text="Velocity")
    label1.grid(row=1, column=1)

    textArea = tk.Text(entryPanel)
    textArea.grid(row=1, column=2)

    label2 = tk.Label(controlPanel, text="Angle")
    label2.grid(row=2, column=1)

    textArea2 = tk.Text(entryPanel2)
    textArea2.grid(row=2, column=2)

    label3 = tk.Label(controlPanel, text="Result   ")
    label3.grid(row=3, column=1)

    result = tk.Label(controlPanel, text="")
    result.grid(row=3, column=2)

    start = tk.Button(controlPanel, text="Start", command=StartSimulation)
    start.grid(row=4, column=1)

    reset = tk.Button(controlPanel, text="Reset", command=RestSimulation)
    reset.grid(row=4, column=2)

    canvas = tk.Canvas(window, width=window_width, height=window_height)
    canvas.configure(bg="gray12")

    boat = PhotoImage(file='files/boat.png')

    boatxpos = random.randint(terrian_width, window_width-boat_start_xpos)

    launchpad = PhotoImage(file='files/launchpad.png')

    rocket = PhotoImage(file='files/rocket.png')

    canvas.create_image(boatxpos, boat_start_ypos, anchor=NW, image=boat)
    canvas.create_image(rocket_start_xpos, rocket_start_ypos,
                        anchor=NW, image=rocket)
    canvas.create_image(pad_start_xpos, pad_start_ypos,
                        anchor=NW, image=launchpad)
    canvas.create_rectangle(terrian_start_x, terrian_start_y, terrian_width,
                            terrian_height+pad_start_ypos,  outline="#00C957", fill="#00C957")
    canvas.create_rectangle(water_start_x, water_start_y, water_width,
                            water_height+pad_start_ypos,  outline="#00CED1", fill="#00CED1")
    canvas.grid(row=10, columnspan=100)
    window.mainloop()
    return canvas


initiate_window = CreateWindow()
initiate_canvas = CreatCanvas(initiate_window)
