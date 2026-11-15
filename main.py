
import tkinter as tk
from tkinter import messagebox
import sajat_modul_VB as sajat


foAblak = tk.Tk()
foAblak.title("Lakberendező")
foAblak.geometry("760x720")
foAblak.resizable(False, False)


foKerete = tk.Frame(foAblak, padx=20, pady=15)
foKerete.pack(fill="both", expand=True)


tk.Label(
    foKerete,
    text="Szobabútor-tervező",
    font=("Arial", 18, "bold")
).pack(pady=10)


# BÚTOROK KIVÁLASZTÁSA

tk.Label(
    foKerete,
    text="1. Válaszd ki a bútorokat és a mennyiségeket!",
    font=("Arial", 11, "bold")
).pack(anchor="w", pady=8)


lista_keret = tk.Frame(foKerete)
lista_keret.pack(anchor="w")


tk.Label(lista_keret, text="Bútor", width=18).grid(row=0, column=0)
tk.Label(lista_keret, text="Méret (m)", width=18).grid(row=0, column=1)
tk.Label(lista_keret, text="Mennyiség").grid(row=0, column=2)


butorok = sajat.butor_lista_VB()
mennyiseg_valtozok = []


for sor, butor in enumerate(butorok, start=1):

    tk.Label(
        lista_keret,
        text=butor.tipus
    ).grid(row=sor, column=0, pady=4)

    tk.Label(
        lista_keret,
        text=f"{butor.szelesseg:.2f} x {butor.melyseg:.2f}"
    ).grid(row=sor, column=1)

    valtozo = tk.StringVar(value="0")
    mennyiseg_valtozok.append(valtozo)

    tk.Spinbox(
        lista_keret,
        from_=0,
        to=50,
        width=8,
        textvariable=valtozo
    ).grid(row=sor, column=2)


# SZOBA MÉRETE

tk.Label(
    foKerete,
    text="2. Add meg a szoba méretét méterben!",
    font=("Arial", 11, "bold")
).pack(anchor="w", pady=12)


meret_keret = tk.Frame(foKerete)
meret_keret.pack(anchor="w")


tk.Label(meret_keret, text="Szélesség:").grid(row=0, column=0)

szelesseg_mezo = tk.Entry(meret_keret, width=10)
szelesseg_mezo.grid(row=0, column=1, padx=10)
szelesseg_mezo.insert(0, "4")


tk.Label(meret_keret, text="Hosszúság:").grid(row=0, column=2)

hossz_mezo = tk.Entry(meret_keret, width=10)
hossz_mezo.grid(row=0, column=3, padx=10)
hossz_mezo.insert(0, "5")


# SZELLŐSSÉG

tk.Label(
    foKerete,
    text="3. Mekkora szellősséget szeretnél?",
    font=("Arial", 11, "bold")
).pack(anchor="w", pady=12)


szelloesseg_valtozo = tk.IntVar(value=40)


szelloesseg_csuszka = tk.Scale(
    foKerete,
    from_=0,
    to=90,
    orient="horizontal",
    variable=szelloesseg_valtozo,
    length=300,
    label="Elvárt szabad padlófelület (%)"
)

szelloesseg_csuszka.pack(anchor="w")


# EREDMÉNY

eredmeny_keret = tk.LabelFrame(
    foKerete,
    text="Számítás eredménye",
    padx=12,
    pady=10
)

eredmeny_keret.pack(fill="x", pady=15)


eredmeny_szoveg = tk.Label(
    eredmeny_keret,
    text="Add meg az adatokat, majd indítsd el a számítást!",
    justify="left",
    wraplength=650
)

eredmeny_szoveg.pack(anchor="w")


def szamitas_VB():

    try:
        szelesseg = float(
            szelesseg_mezo.get().replace(",", ".")
        )

        hossz = float(
            hossz_mezo.get().replace(",", ".")
        )

        kivant_szelloesseg = szelloesseg_valtozo.get()

        if szelesseg <= 0 or hossz <= 0:
            raise ValueError("A szoba mérete pozitív szám legyen.")

        butorok_mennyiseggel = []

        for butor, valtozo in zip(
            butorok,
            mennyiseg_valtozok
        ):

            mennyiseg = int(valtozo.get())

            if mennyiseg < 0:
                raise ValueError("A mennyiség nem lehet negatív.")

            if mennyiseg > 0:
                butorok_mennyiseggel.append(
                    (butor, mennyiseg)
                )

    except ValueError as hiba:

        messagebox.showerror(
            "Hibás adat",
            f"Ellenőrizd az adatokat!\n{hiba}"
        )

        return


    # TERÜLETEK KISZÁMÍTÁSA

    szoba_terulet = sajat.szoba_terulet_VB(
        szelesseg,
        hossz
    )

    butor_terulet = sajat.butorok_osszes_terulete_VB(
        butorok_mennyiseggel
    )

    tenyleges_szelloesseg = sajat.szelloesseg_VB(
        szoba_terulet,
        butor_terulet
    )


    # KIVÁLASZTOTT BÚTOROK LISTÁJA

    lista_szoveg = []

    for butor, mennyiseg in butorok_mennyiseggel:

        lista_szoveg.append(
            f"{butor.tipus}: {mennyiseg} db"
        )

    if not lista_szoveg:
        lista_szoveg.append("Nincs kiválasztott bútor.")


    # EREDMÉNY MEGJELENÍTÉSE

    szoveg = (
        f"Szoba alapterülete: {szoba_terulet:.2f} m²\n"
        f"Bútorok összes területe: {butor_terulet:.2f} m²\n"
        f"Szabad padlófelület: "
        f"{szoba_terulet - butor_terulet:.2f} m²\n"
        f"Tényleges szellősség: "
        f"{tenyleges_szelloesseg:.1f}%\n"
        f"Elvárt szellősség: {kivant_szelloesseg}%\n\n"
        f"Kiválasztott bútorok:\n"
        + "\n".join(lista_szoveg)
    )


    if butor_terulet > szoba_terulet:

        szoveg += (
            "\n\nNEM FÉR EL!\n"
            "A bútorok területe nagyobb, mint a szoba területe."
        )

    elif sajat.elfer_VB(
        szoba_terulet,
        butor_terulet,
        kivant_szelloesseg
    ):

        szoveg += (
            "\n\nELFÉR!\n"
            "A kívánt szellősség teljesül."
        )

    else:

        szoveg += (
            "\n\nNEM FÉR EL A KÍVÁNT SZELLŐSSÉGGEL!\n"
            "Csökkentsd a bútorok mennyiségét, "
            "vagy válassz nagyobb szobát."
        )


    eredmeny_szoveg.config(text=szoveg)


# SZÁMÍTÁS GOMB

tk.Button(
    foKerete,
    text="Elfér-e? Számítás",
    command=szamitas_VB,
    font=("Arial", 11, "bold"),
    padx=15,
    pady=7
).pack(pady=10)


foAblak.mainloop()
