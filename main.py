import tkinter as tk
import sajat_modul_VB as sajat

foAblak = tk.Tk()
foAblak.title("Lakberendező")
foAblak.geometry("1280x720")

vezerlopanel = tk.Frame(foAblak)
vezerlopanel.pack(side="left", padx=10, pady=10)

canvas = tk.Canvas(foAblak, width=980, height=700, bg="white")
canvas.pack(side="right", pady=20, padx=20)

asztalok=[]
def uj_asztal_VB():
    darab= len(asztalok)
    asztal = sajat.AsztalVB()
    asztalok.append(asztal)
    canvas.create_rectangle(
        asztal.x0,
        asztal.y0,
        asztal.x1,
        asztal.y1,
        fill=asztal.color,
        outline="black",
        tags=("butor_VB","asztal_VB")

    )

gomb = tk.Button(
    foAblak,
    text="Új asztal",
    command=uj_asztal_VB
)

gomb.pack(pady=10)

kivalasztott = None
elozo_x = 0
elozo_y = 0

def kattintas(esemeny):
    global kivalasztott, elozo_x, elozo_y
    talalatok = canvas.find_overlapping(
        esemeny.x - 1, esemeny.y - 1,
        esemeny.x + 1, esemeny.y + 1
    )

    butorok = [
        elem for elem in talalatok
        if "butor_VB" in canvas.gettags(elem)
    ]

    kivalasztott = butorok[-1] if butorok else None

    elozo_x = esemeny.x
    elozo_y = esemeny.y

def mozgas(esemeny):
    global elozo_x, elozo_y
    if kivalasztott is not None:
        dx = esemeny.x - elozo_x
        dy = esemeny.y - elozo_y

        x0, y0, x1, y1 = canvas.coords(kivalasztott)

        uj_hely = [
            x0 + dx,
            y0 + dy,
            x1 + dx,
            y1 + dy
        ]
        belefer = sajat.canvas_hatar_VB(
            *uj_hely, 980, 700
        )

        nincs_utkozes = True

        for masik in canvas.find_withtag("butor_VB"):
            if masik == kivalasztott:
                continue

            masik_hely = canvas.coords(masik)

            if sajat.utkozes_VB(uj_hely, masik_hely):
                nincs_utkozes = False
                break

        if belefer and nincs_utkozes:
            canvas.move(kivalasztott, dx, dy)

        elozo_x = esemeny.x
        elozo_y = esemeny.y

def elengedes(esemeny):
    global kivalasztott
    kivalasztott = None

canvas.bind("<Button-1>", kattintas)
canvas.bind("<B1-Motion>", mozgas)
canvas.bind("<ButtonRelease-1>", elengedes)








foAblak.mainloop()

