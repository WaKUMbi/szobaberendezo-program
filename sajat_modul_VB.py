
import tkinter as tk


class ButorVB:
    def __init__(self, szelesseg, melyseg, tipus):
        self.szelesseg = szelesseg
        self.melyseg = melyseg
        self.tipus = tipus

    def terulet_VB(self):
        return self.szelesseg * self.melyseg


class AsztalVB(ButorVB):
    def __init__(self):
        super().__init__(1.20, 0.70, "Asztal")


class SzekVB(ButorVB):
    def __init__(self):
        super().__init__(0.45, 0.45, "Szék")


class KanapeVB(ButorVB):
    def __init__(self):
        super().__init__(2.00, 0.90, "Kanapé")


class AgyVB(ButorVB):
    def __init__(self):
        super().__init__(2.00, 1.60, "Ágy")


class SzekrenyVB(ButorVB):
    def __init__(self):
        super().__init__(1.20, 0.60, "Szekrény")


class KomodVB(ButorVB):
    def __init__(self):
        super().__init__(0.80, 0.40, "Komód")


def butor_lista_VB():
    return [
        AsztalVB(),
        SzekVB(),
        KanapeVB(),
        AgyVB(),
        SzekrenyVB(),
        KomodVB()
    ]


def szoba_terulet_VB(szelesseg, hossz):
    return szelesseg * hossz


def butorok_osszes_terulete_VB(butorok_mennyiseggel):
    osszeg = 0

    for butor, mennyiseg in butorok_mennyiseggel:
        osszeg += butor.terulet_VB() * mennyiseg

    return osszeg


def szelloesseg_VB(szoba_terulet, butor_terulet):
    if szoba_terulet <= 0:
        return 0

    return (
        (szoba_terulet - butor_terulet)
        / szoba_terulet
        * 100
    )


def elfer_VB(szoba_terulet, butor_terulet, kivant_szelloesseg):

    if szoba_terulet <= 0:
        return False

    if butor_terulet > szoba_terulet:
        return False

    tenyleges = szelloesseg_VB(
        szoba_terulet,
        butor_terulet
    )

    return tenyleges >= kivant_szelloesseg
