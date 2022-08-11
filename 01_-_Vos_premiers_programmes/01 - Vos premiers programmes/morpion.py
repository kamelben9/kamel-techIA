

# Grille

list1 = ["-" , "-" , "-" ]
list2 = ["-" , "-" , "-" ]
list3 = ["-" , "-" , "-" ]

listM = [list1,list2,list3]



def afficher_grille(grille):

    """
    Fonction qui permet d'afficher la grille du jeu lorsque celui-ci commence
    """

    for elt in listM:
        print(elt)


def modif_grille(grille,joueur,commande):

    '''
    Fonction qui permet de modifier la grille et remplace les caractères vides par l'entrée utlisateur
    '''

    if commande[0] in grille and commande[1] in range(3):
        if grille[commande[0]][int(commande[1])] == "-":
            grille[commande[0]][int(commande[1])] == joueur
            return grille
    return False

    if commande == "A1":
        grille[0][0]
    elif commande == "A2":
        grille[1][0]
    elif commande == "A3":
        grille[2][0]
    elif commande == "B1":
        grille[0][1]
    elif commande == "B2":
        grille[1][1]
    elif commande == "B3":
        grille[2][1]
    elif commande == "C1":
        grille[0][2]
    elif commande == "C2":
        grille[1][2]
    elif commande == "C3":
        grille[2][2]

def verif_grille(grille):

    '''
    Fonction qui permet de vérifier si l'intégralité de la grille de jeu est remplie
    '''
    for ligne in listM:
        for case in ligne:
            if case == "-":
                return False

    return True


def est_gagnante(grille):

    '''
    Fonction qui permet de connaître la situation à la fin du jeu
    '''


    colonneA = [listM[0][0],listM[1][0],listM[2][0]]
    colonneB = [listM[0][1] ,listM[1][1] ,listM[2][1]]
    colonneC = [listM[0][2] ,listM[1][2] ,listM[2][2]]
    
    ligneA = [listM[0][0] ,listM[0][1] ,listM[0][2]]
    ligneB = [listM[1][0] ,listM[1][1] ,listM[1][2]]
    ligneB = [listM[2][0] ,listM[2][1] ,listM[2][2]]

    diagonale1 = [listM[0][0] ,listM[1][1],listM[2][2]]
    diagonale2 = [listM[0][2] ,listM[1][1] ,listM[2][0]]


    #lignes
    for ligne in listM:
        if (ligne[0] == ligne[1] == ligne[2]) and (ligne[0] != "-"):
           return True


    #colonnes
    for i in range(3):
        if listM[0][i] == listM[1][i] == listM[2][i] and listM[0][i] != "-":
            return True


    #diagonales
    if (listM[0][0] == listM[1][1] == listM[2][2]):
        return True
    elif (listM[0][2] == listM[1][1] == listM[2][0]):
        return True


    return False



afficher_grille(listM)
verif_grille(listM)





