
'''
hashtag = "#"

for i in range(7):
    print(hashtag)
    hashtag += "#"
'''

'''
def somme(liste):

    """
    Fonction qui permet d'additioner les éléments de la liste
    """
    

    result = 0 


    for nb in liste :
        result += nb

    return result 

listnb = [1, 3, 5, 7, 9]

print(somme(listnb))



def moyenne(liste2):

    """
    Fonction qui permet d'effectuer la moyenne des éléments d'une liste
    """

    
    
    result = 0
    for nb in liste2 :
        result += nb
        result2 = result / (len(liste2))
    
    return somme(liste2) / len(liste2)



listnb2 = [10,12,14,16,18,20]

print(moyenne(listnb2))
'''

'''
for i in range (1,101):


    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Fuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Fuzz")
    else:
        print(i)
'''


'''
list = [1, "test", 0.9867, "Python, c'est génial !"]

newList = []

for i in range(len(list)):

    list[-(i+1)]
    newList.append(list[-(i+1)])

print(newList)
'''

'''
mon_dict = {"nom": "Gayerie", "prenom": "David"}

userRequest = input("De quel mot voulez vous la définition ?")


if userRequest in mon_dict :
    print(mon_dict[userRequest])
else :
    print("Nous n'avons pas ce mot dans le dictionnaire")
'''


from random import randint


liste = [randint(1,100) for _ in range(1000)]


print(liste)
print(len(liste))

