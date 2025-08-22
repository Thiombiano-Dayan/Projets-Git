import tkinter as tk
import random

# Options possibles
CHOIX = ["Pierre", "Papier", "Ciseaux"]

score_joueur = 0
score_ordi = 0

# Fonction pour jouer un coup
def jouer(coup_joueur):
    global score_joueur, score_ordi
    coup_ordi = random.choice(CHOIX)
    label_ordi.config(text=f"Ordinateur : {coup_ordi}")

    if coup_joueur == coup_ordi:
        resultat.config(text="🤝 Égalité !", fg="blue")
    elif (coup_joueur == "Pierre" and coup_ordi == "Ciseaux") or \
         (coup_joueur == "Papier" and coup_ordi == "Pierre") or \
         (coup_joueur == "Ciseaux" and coup_ordi == "Papier"):
        resultat.config(text="🎉 Tu as gagné !", fg="green")
        score_joueur += 1
    else:
        resultat.config(text="😢 Tu as perdu !", fg="red")
        score_ordi += 1

    label_score.config(text=f"Score : Joueur {score_joueur} - {score_ordi} Ordinateur")

# Fonction pour remettre les scores à 0
def reset_score():
    global score_joueur, score_ordi
    score_joueur = 0
    score_ordi = 0
    label_score.config(text="Score : Joueur 0 - 0 Ordinateur")
    resultat.config(text="")
    label_ordi.config(text="Ordinateur : ")

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Pierre - Papier - Ciseaux")
fenetre.geometry("300x350")

# Titre
tk.Label(fenetre, text="Pierre - Papier - Ciseaux", font=("Arial", 14, "bold")).pack(pady=10)

# Boutons pour le joueur
for choix in CHOIX:
    tk.Button(fenetre, text=choix, width=10,pady=5, font=("Arial", 12),
              command=lambda c=choix: jouer(c)).pack()

# Affichage du choix de l'ordinateur
label_ordi = tk.Label(fenetre, text="Ordinateur : ", font=("Arial", 12))
label_ordi.pack(pady=10)

# Résultat
resultat = tk.Label(fenetre, text="", font=("Arial", 14))
resultat.pack(pady=10)

# Score
label_score = tk.Label(fenetre, text="Score : Joueur 0 - 0 Ordinateur", font=("Arial", 12))
label_score.pack(pady=10)

# Bouton Reset
tk.Button(fenetre, text="🔄 Reset", font=("Arial", 12, "bold"), command=reset_score).pack(pady=5)

# Boucle principale
fenetre.mainloop()
