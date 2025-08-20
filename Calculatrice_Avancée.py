import tkinter as tk
from math import *

# ==== FONCTION DE LA FENÊTRE D'ACCUEIL ====
def accueil():
    root = tk.Tk()
    root.title("Menu de la Calculatrice")
    root.geometry("400x300")
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