import numpy
import random

liste=[(0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3),(3,3),(3,2),(3,1),(3,0)] # Cette liste représente les indices du serpentin. On choisit de faire un serpentin pour faciliter les fusions

def joue_ligne(ligne): # Fonction permettant de réaliser le déplacement des nombres à l'intérieur d'une ligne
    res = []
    for n in ligne:
        if n == 0:
            continue
        if len(res) == 0:
            res.append(n)
        else:
            prev = res[-1]
            if prev == n:
                res[-1] = 2 * n
            else: 
                res.append(n)
    while len(res) < len(ligne):
        res.append(0)
    return res

def joue(mat, direction): # Permet de passer d'une grille à une autre en fonction de la direction
    if direction == 0:                                              # 0 : gauche
        lines = [joue_ligne(mat[i, :]) for i in range(4)]
        mat = numpy.array(lines)
        return mat
    elif direction == 1:                                            # 1 : haut
        lines = [joue_ligne(mat[:, i]) for i in range(4)]
        mat = numpy.array(lines)
        return mat.T
    elif direction == 2:                                            # 2 : droite
        lines = [list(reversed(joue_ligne(mat[i, ::-1]))) for i in range(4)]
        mat = numpy.array(lines)
        return mat
    elif direction == 3:                                            # 3 : bas
        lines = [list(reversed(joue_ligne(mat[::-1, i]))) for i in range(4)]
        mat = numpy.array(lines)
        return mat.T

def eval_situation(mat): #Affecte un score à une situation donnée
    cond = True
    score = 0
    i = 0
    while mat[liste[i]]!=0 and cond: # Explore la grille dans l'ordre du serpentin
        cond=mat[liste[i]]>=mat[liste[i+1]]  # Vérifie que la suite est décroissante
        score+=mat[liste[i]]**2 # On ajoute au score le carré de la case pour favoriser les fusions de cases
        i+=1 
    return score/(compte(mat)**0.01) # On divise par compte(mat) pour favoriser les grilles avec beaucoup de cases vides et puissance 0.01 car c'est l'exposant qui donne le meilleur résultat

def compte(mat): # Compte le nombre de cases pleines de la grille
    compteur=0
    for i in liste:
        if mat[i]!=0:
            compteur+=1
    return compteur


def strategy_2048(game, state=None, moves=None): # Renvoie le meilleur mouvement à effectuer selon notre stratégie
    max1,max2,imax=0,0,0 
    for i in [1,0,2,3]: # Test les différentes directions possibles pour le premier mouvement (on commence par haut car c'est plus efficace empiriquement)
        mat = joue(game,i) # On crée la nouvelle matrice
        buf1 = eval_situation(mat) # On évalue le score de cette matrice
        if game[(0,0)] <= mat[(0,0)]: # On vérifie que la première case n'a pas bougé
            for j in [1,0,2,3]: # Test les différentes directions possibles pour le deuxième mouvement
                buf2 = eval_situation(joue(mat,j)) # On évalue le score de la matrice après ce deuxième mouvement
                if buf2 > max2: # On conserve l'indice qui assure le meilleur score après 2 coups
                    max1,max2,imax = buf1,buf2,i        
                if buf2 == max2: # Si il y a égalité après 2 coups, alors conserve l'indice qui assure le meilleur score après 1 coup
                    if buf1 > max1:                     
                        max1,max2,imax = buf1,buf2,i    
    return imax
    
