import turtle

'''
turtle.right(180)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
'''

'''
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
'''

'''
turtle.speed(9)
turtle.left(180)
turtle.forward(500)
turtle.left(120)
turtle.forward(100)
turtle.left(60)
turtle.forward(800)
turtle.left(45)
turtle.forward(122)
turtle.left(135)
turtle.forward(500)

turtle.right(90)
turtle.penup()
turtle.forward(30)
turtle.right(90)
turtle.pendown()
turtle.forward(500)
turtle.left(140)
turtle.forward(650)
turtle.left(85)
turtle.forward(590)
turtle.right(180)
turtle.right(45)
turtle.forward(415)
turtle.left(90)
turtle.forward(422)

turtle.done() # permet d'indiquer à la tortue que nous avons fini le dessin

'''

'''
nomDeMaVariable = "La somme de mes variable est "

number1 = 10
number2 = 20

result = number1 + number2

print(result)
print(nomDeMaVariable + str(result))
'''


'''
value = input("Quelle est votre distance parcourue en miles ?")

kmValue = float(value) * 1.6

print("Votre distance en Km est " + str(kmValue) + "Km")
'''

''''
var1 = "Je dois être en seconde position"
var2 = "Je dois être en première position"

var1,var2 = var2,var1

print(var1)
print(var2)
print(var1 + " | " + var2) 
'''

'''''
nbUtilisateur = int(input("Entrez un nombre "))

if nbUtilisateur < 0:
    # code qui s'exécute si nbUtilisateur est plus petit que 0
    print("Votre nombre est négatif")
else:
    # sinon, c'est ce code qui s'exécute
    print("Votre nombre est positif ou nul !")

'''

'''
nb1 = 9
nb2 = 8
nb3 = 7

if nb1 > nb2 and nb2 > nb3:
    # si nb1 > nb2 et nb2 > nb3 alors on exécute ce code
    print("Vous avez entrez les nombre par ordre décroissant !")
elif nb1 < nb2 and nb2 < nb3:
    # sinon, si nb1 < nb2 et nb2 < nb3 alors on exécute ce code
    print("Vous avez entrez les nombre par ordre croissant !")
else:
    # sinon, on exécute celui-ci
    print("Tout est dans le désordre !")
'''    


"""
nbUser = int(input("Entrez un nombre"))

if nbUser % 2 == 0 :
    print("Le nombre est pair")
else :
    print ("Le nombre est impair")

"""
'''
nb1 = int(input("Entrez un premier nombre"))
nb2 = int(input("Entrez un deuxième nombre"))
nb3 = int(input("Entrez un troisième nombre"))


if nb1 > nb2 and nb1 > nb3 :
    print("Le nombre le plus grand est le premier nombre")
elif nb2 > nb1 and nb2 > nb3 :
    print("Le nombre le plus grand est le deuxième nombre")
else :
    print("Le nombre le plus grand est le troisième nombre")
'''

'''
def est_pair(nb):

    if nb % 2 == 0:
        return True
    else:
        return False

    return est_pair()        

print(est_pair(16))
'''


'''
def est_pluspetit(nb1,nb2,nb3):

    if nb1 < nb2 and nb2 < nb3:
        return nb1
    elif nb2 < nb1 and nb2 < nb3:
        return nb2
    else:
        return nb3

    return est_pluspetit()

print(est_pluspetit(3,1,16))         
'''


def calculer_moyenne(nb1,nb2,nb3):

    mean = (nb1 + nb2 + nb3) / 3

    return mean


print(calculer_moyenne(6,10,14))


print(5 == "5")