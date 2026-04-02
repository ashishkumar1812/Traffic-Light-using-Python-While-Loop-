import tkinter as tk
from PIL import Image, ImageTk
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def show_light(color, time_left):
    path = os.path.join(BASE_DIR, f"{color}.png")
    img = ImageTk.PhotoImage(Image.open(path))
    image_label.config(image=img)
    image_label.image = img
    timer_label.config(text=f"Time Left: {time_left}s")

# Define full cycle
cycle = (
    [("green", i) for i in range(15, 0, -1)] +
    [("yellow", i) for i in range(5, 0, -1)] +
    [("red", i) for i in range(15, 0, -1)] +
    [("yellow", i) for i in range(5, 0, -1)]
)

index = 0

def run_traffic():
    global index

    color, time_left = cycle[index]
    show_light(color, time_left)

    index += 1
    if index >= len(cycle):
        index = 0  # restart cycle

    root.after(1000, run_traffic)

# UI
root = tk.Tk()
root.title("Traffic Light Signal Program")
root.geometry("700x700")

image_label = tk.Label(root)
image_label.pack(pady=20)

timer_label = tk.Label(root, font=("Arial", 20))
timer_label.pack(pady=20)

run_traffic()
root.mainloop()