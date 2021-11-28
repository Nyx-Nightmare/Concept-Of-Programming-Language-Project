from tkinter import *
import tkinter as tk
import time

# width of the animation window
window_width = 800
# height of the animation window
window_height = 600
# initial x position of the ball
rocket_start_xpos = 50
# initial y position of the ball
rocket_start_ypos = 50
# the pixel movement of ball for each iteration
velocity = 0
# delay between successive frames in seconds
animation_refresh_seconds = 0.01


def CreateWindow():
    window = tk.Tk()

    def StartSimulation():
        inp = textArea.get(1.0, "end-1c")
        velocity = inp
        StartAnimation(window, initiate_canvas, velocity)

    def RestSimulation(result):
        result.config(text="")

    def StartAnimation(w, c, v):
        inp = "text"
        print(inp)

    window.geometry(f'{window_width}x{window_height}')
    window.config(bg='gray2')

    controlPanel = tk.Frame(window)
    controlPanel.grid()
    controlPanel.config(bg='gainsboro')

    entryPanel = tk.Frame(controlPanel, width=100, height=20)
    entryPanel.grid(row=1, column=2)
    entryPanel.columnconfigure(0, weight=10)
    entryPanel.grid_propagate(False)

    label1 = tk.Label(controlPanel, text="Velocity")
    label1.grid(row=1, column=1)

    textArea = tk.Text(entryPanel)
    textArea.grid(row=1, column=2)

    label2 = tk.Label(controlPanel, text="Result   ")
    label2.grid(row=2, column=1)

    result = tk.Label(controlPanel, text="")
    result.grid(row=2, column=2)

    start = tk.Button(controlPanel, text="Start", command=StartSimulation)
    start.grid(row=3, column=1)

    reset = tk.Button(controlPanel, text="Reset", command=RestSimulation)
    reset.grid(row=3, column=2)

    window.mainloop()


def CreatCanvas(window):
    canvas = tk.Canvas(window)
    canvas.configure(bg="gray2")
    boat = PhotoImage(file='files/boat.png')
    canvas.create_image(20, 20, anchor=NW, image=boat)
    canvas.pack(fill="both", expand=True)
    return canvas


initiate_window = CreateWindow()
initiate_canvas = CreatCanvas(initiate_window)
