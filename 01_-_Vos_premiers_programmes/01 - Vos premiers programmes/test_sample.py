import pytest

# content of test_sample.py

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5



def somme(liste):

    """
    Fonction qui permet d'additioner les éléments de la liste
    """
    

    result = 0 


    for nb in liste :
        result += nb

    return result 

listnb = [1, 3, 5, 7, 9]

def test():
    assert somme(listnb) == 24
