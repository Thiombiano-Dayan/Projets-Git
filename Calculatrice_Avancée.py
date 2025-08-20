import tkinter as tk
from math import *

# ==== FONCTION DE LA FENÊTRE D'ACCUEIL ====
def accueil():
    root = tk.Tk()
    root.title("Menu de la Calculatrice")
    root.geometry("320x300")
    root.resizable(False, False) # Empêche l'utilisateur de redimentionner la fenêtre d'accueil

    titre = tk.Label(root, text="Choisissez le type de calculatrice :", font=("Times New Roman", 16, "bold"))
    titre.grid(row=0, column=0, columnspan=2, pady=20)

    # Bouton calculatrice simple
    btn_simple = tk.Button(root, text="Calculatrice Simple", width=25, height=2,
                           command=lambda: [root.destroy(), calculatrice_simple()])
    btn_simple.grid(row=1, column=0, columnspan=2, pady=10)

    # Bouton calculatrice avancée
    btn_avancee = tk.Button(root, text="Calculatrice Avancée", width=25, height=2,
                            command=lambda: [root.destroy(), calculatrice_avancee()])
    btn_avancee.grid(row=2, column=0, columnspan=2, pady=10)

    # Bouton calculatrice trigonométrique
    btn_trigo = tk.Button(root, text="Calculatrice Trigonométrique", width=25, height=2,
                          command=lambda: [root.destroy(), calculatrice_trigo()])
    btn_trigo.grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()


# ==== FONCTIONS CALCULATRICES ====
def calculatrice_simple():
    fenetre = tk.Tk()
    fenetre.title("Calculatrice Simple")
    fenetre.geometry("300x400")
    

    # Zone d'affichage
    entree = tk.Entry(fenetre, width=20, font=("Arial", 18), borderwidth=5, relief="ridge")
    entree.grid(row=0, column=0, columnspan=4, pady=10)

    # Fonction pour ajouter du texte

    def bouton_click(val):
        entree.insert(tk.END, val)

    def effacer():
        entree.delete(0, tk.END)

    def calculer():
        try:
            res = eval(entree.get())
            entree.delete(0, tk.END)
            entree.insert(tk.END, res)
        except:
            entree.delete(0, tk.END)
            entree.insert(tk.END, "Erreur")

    # Boutons
    boutons = [
        ('7',1,0), ('8',1,1), ('9',1,2), ('+',1,3),
        ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
        ('1',3,0), ('2',3,1), ('3',3,2), ('*',3,3),
        ('0',4,0), ('.',4,1), ('/',4,2), ('=',4,3)
    ]

    for (txt, r, c) in boutons:
        if txt == "=":
            tk.Button(fenetre, text=txt, width=5, height=2, command=calculer)\
                .grid(row=r, column=c, padx=5, pady=5)
        else:
            tk.Button(fenetre, text=txt, width=5, height=2, command=lambda t=txt: bouton_click(t))\
                .grid(row=r, column=c, padx=5, pady=5)

    tk.Button(fenetre, text="Effacer", width=5, height=2, command=effacer)\
        .grid(row=5, column=0, columnspan=4, sticky="we", padx=5, pady=5)
    tk.Button(fenetre, text="Retour au menu", width=20, height=2, command=lambda: [fenetre.destroy(), accueil()])\
        .grid(row=6, column=0, columnspan=4)

    fenetre.mainloop()


def calculatrice_avancee():
    import math
    fen = tk.Tk()
    fen.title("Calculatrice Avancée")
    fen.geometry("420x400")

    entree = tk.Entry(fen, width=25, font=("Arial", 18), borderwidth=5, relief="ridge")
    entree.grid(row=0, column=0, columnspan=5, pady=10)

    def bouton_click(val):
        entree.insert(tk.END, val)

    def effacer():
        entree.delete(0, tk.END)

    def calculer():
        try:
            res = eval(entree.get())
            entree.delete(0, tk.END)
            entree.insert(tk.END, res)
        except Exception:
            entree.delete(0, tk.END)
            entree.insert(tk.END, "Erreur")

    # Fonctions avancées
    def ln():
        try:
            valeur = float(entree.get())
            entree.delete(0, tk.END)
            entree.insert(tk.END, math.log(valeur))
        except:
            entree.delete(0, tk.END)
            entree.insert(tk.END, "Erreur")

    def exp():
        try:
            valeur = float(entree.get())
            entree.delete(0, tk.END)
            entree.insert(tk.END, math.exp(valeur))
        except:
            entree.delete(0, tk.END)
            entree.insert(tk.END, "Erreur")

    def log():
        try:
            valeur = float(entree.get())
            entree.delete(0, tk.END)
            entree.insert(tk.END, math.log10(valeur))
        except:
            entree.delete(0, tk.END)
            entree.insert(tk.END, "Erreur")

    def fact():
        try:
            valeur = int(entree.get())
            entree.delete(0, tk.END)
            entree.insert(tk.END, math.factorial(valeur))
        except:
            entree.delete(0, tk.END)
            entree.insert(tk.END, "Erreur")

    boutons = [
        ('%',1,0), ('**',1,1), ('//',1,2), ('(',1,3), (')',1,4),
        ('7',2,0), ('8',2,1), ('9',2,2), ('+',2,3), ('-',2,4),
        ('4',3,0), ('5',3,1), ('6',3,2), ('*',3,3), ('/',3,4),
        ('1',4,0), ('2',4,1), ('3',4,2), ('0',4,3), ('.',4,4)
    ]

    for (txt, r, c) in boutons:
        tk.Button(fen, text=txt, width=5, height=2, command=lambda t=txt: bouton_click(t))\
            .grid(row=r, column=c, padx=5, pady=5)
    
    # Boutons fonctions avancées
    tk.Button(fen, text="ln", width=5, height=2, command=ln).grid(row=1, column=5)
    tk.Button(fen, text="exp", width=5, height=2, command=exp).grid(row=2, column=5)
    tk.Button(fen, text="log", width=5, height=2, command=log).grid(row=3, column=5)
    tk.Button(fen, text="!", width=5, height=2, command=fact).grid(row=4, column=5)

    fonct_avancee = [ ('ln',1,5), ('exp',2,5), ('log',3,5) ]

    for (txt, r, c) in fonct_avancee:
        tk.Button(fen, text=txt, width=8, height=2, command=lambda t=txt+'(': bouton_click(t))\
            .grid(row=r, column=c, padx=5, pady=5)
        
    tk.Button(fen, text="=", width=10, height=2, command=calculer)\
        .grid(row=5, column=3, columnspan=2, padx=5, pady=5)

    tk.Button(fen, text="Effacer", width=10, height=2, command=effacer)\
        .grid(row=5, column=0, columnspan=3, padx=5, pady=5)
    tk.Button(fen, text="Retour au menu", width=20, height=2, command=lambda: [fen.destroy(), accueil()])\
        .grid(row=6, column=1, columnspan=4)

    fen.mainloop()


def calculatrice_trigo():
    fen = tk.Tk()
    fen.title("Calculatrice Trigonométrique")
    fen.geometry("300x400")

    entree = tk.Entry(fen, width=20, font=("Arial", 18), borderwidth=5, relief="ridge")
    entree.grid(row=0, column=0, columnspan=6, pady=10)

    def bouton_click(val):
        entree.insert(tk.END, val)

    def effacer():
        entree.delete(0, tk.END)

    def calculer():
        try:
            res = eval(entree.get())
            entree.delete(0, tk.END)
            entree.insert(tk.END, res)
        except:
            entree.delete(0, tk.END)
            entree.insert(tk.END, "Erreur")

    fonctions = [
        ('sin',1,0), ('cos',1,1), ('tan',1,2),
        ('asin',2,0), ('acos',2,1), ('atan',2,2),
        ('sinh',3,0), ('cosh',3,1), ('tanh',3,2),
        ('asinh',4,0), ('acosh',4,1), ('atanh',4,2)
    ]

    for (txt, r, c) in fonctions:
        tk.Button(fen, text=txt, width=8, height=2, command=lambda t=txt+'(': bouton_click(t))\
            .grid(row=r, column=c, padx=5, pady=5)

    tk.Button(fen, text="=", width=10, height=2, command=calculer)\
        .grid(row=5, column=1, columnspan=3, padx=5, pady=5)

    tk.Button(fen, text="Effacer", width=10, height=2, command=effacer)\
        .grid(row=5, column=0, columnspan=2, padx=5, pady=5)
    tk.Button(fen, text="Retour au menu", width=20, height=2, command=lambda: [fen.destroy(), accueil()])\
        .grid(row=6, column=0, columnspan=3)

    fen.mainloop()


# Lancer le menu principal
accueil()
