#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# COSTE Elio, COURTOIS Thibaut, DENIEL Théo, NAIME Mathieu
# Tuesday, 15 December 2020 
# Informatique - projet 
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Ce projet consiste en une implémentation simpliste d'un jeu d'échecs, avec \
seulement quelques fonctionnalités."""

import random

def convertit_coup(coup):
    """Convertit la notation algébrique en coordonnées utilisables."""
    coordonnees = ((), ())
    return coordonnees

def coup_valide(plateau, coup):
    """Retourne True si le coup demandé est valide, False sinon."""
    est_valide = True
    
    # Vérifie si le coup est légal

    return est_valide

def jouer_coup(plateau, coup):
    """Joue le coup demandé sur l'échiquier."""

    # Joue le coup

    return plateau

def afficher_plateau(plateau, trait):
    """Affiche l'échiquier sous la perspective de la couleur qui a le trait."""
    # Si c'est aux Noirs de jouer, on renverse l'échiquier
    if not trait:
        pass
    for i in plateau:
        for j in i:
            print(j, end='')
        print()
    

def demo():
    input("Appuyez sur ENTREE pour commencer une nouvelle partie.")

    # Position de départ.
    plateau = [
        ['R', 'N', 'B', 'Q', 'K', 'B', 'K', 'R'], 
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 
        ['.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.'], 
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], 
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]

    trait = 0
    running = True
    while running:
        trait = 0 if trait == 1 else 1
        coup = convertit_coup(demander_entree("Trait aux {} : ".format(trait), coup_valide))
        jouer_coup(plateau, coup)


if __name__ == "__main__":
    demo()
