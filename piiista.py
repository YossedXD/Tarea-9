import tkinter as tk
import math

root = tk.Tk()
root.title("Pista de Carreras - Pentágono")
root.geometry("800x600")

canvas = tk.Canvas(root, width=800, height=600, bg="gray20")
canvas.pack()

puntos_pista = [
    (400, 100),
    (650, 250),
    (550, 500),
    (250, 500),
    (150, 250),
    (400, 100)
]

for i in range(len(puntos_pista) - 1):
    x1, y1 = puntos_pista[i]
    x2, y2 = puntos_pista[i + 1]
    canvas.create_line(x1, y1, x2, y2, width=40, fill="black", capstyle=tk.ROUND)

carro = canvas.create_rectangle(380, 80, 420, 120, fill="red")

velocidad = 4
indice = 0

def mover_carro():
    global indice
    x1, y1 = puntos_pista[indice]
    x2, y2 = puntos_pista[indice + 1]
    dx = x2 - x1
    dy = y2 - y1
    dist = math.hypot(dx, dy)
    if dist != 0:
        dx /= dist
        dy /= dist
    canvas.move(carro, dx * velocidad, dy * velocidad)
    pos = canvas.coords(carro)
    cx, cy = (pos[0] + pos[2]) / 2, (pos[1] + pos[3]) / 2
    if math.hypot(x2 - cx, y2 - cy) < 8:
        indice = (indice + 1) % (len(puntos_pista) - 1)
    root.after(30, mover_carro)

mover_carro()
root.mainloop()
