# ⚓ Bataille Navale — Jeu en Python

Cette version a été développé avec une **architecture orientée objet**. 
Le joueur affronte une **flotte de bateaux cachés** sur une grille (10x10) et doit les **couler** en devinant leurs positions.

### 🧩 Fonctionnalités

- Grille de jeu **Interactive** en console.
- **Système de tir** avec **vérification des coordonnées**.
- **Détection** des **touches** et des **bateaux coulés**.
- **Affichage dynamique de la grille** après chaque tir.
- **Architecture modulaire** avec classes *Boats, Grid, Game*

### 🧱 Structure du projet
- **main.py** : Point d'entrée du jeu.
- **game.py** : Logique principale du jeu.
- **grid.py** : Classe de la grille du jeu.
- **boats.py** : Classe représentant les bateaux.
- **README.md** : Documentation du projet.

### 🚀 Pour lancer le jeu
- Assurez-vous d’avoir **Python 3** installé.
- ainsi que la **bibliothèque pandas** :

      pip install pandas
- Puis exécutez :

        python main.py

### 🎮 Règles du jeu
- La **grille** est de taille **10x10**, avec des **colonnes de A à J** et des **lignes de 1 à 10**.
- Saisissez une coordonnée come B2 ou J10 pour faire feu.
- Vous pouvez quitter à tout moment avec 'quit'.
- Les symboles sur la grille :
  - **~** : case non jouée
  - **X** : touche sur un bateau
  - **O** : tir manqué

### 🧠 Architecture orientée objet
- *Boats* : gère les positions, les touches et la détection de bateau coulé.
- *Grid* : crée et met à jour la grille de jeu.
- *Game* : boucle principale, gestions des tirs et de la condition de victoire.