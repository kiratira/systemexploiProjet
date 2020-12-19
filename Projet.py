import matplotlib.pyplot as plt
import numpy as np

while 1:
    fct = input("Entrer la fonction: ")
    #choix du SO1 ou SO2
    SO = checkSO(fct)
    print("Votre est " + fct + """ 
    Cette Fonction est un """ + SO)
    #Utilisation des fonctions de plot SO1 ou SO2

    exit = input("Appuyer sur '1' pour recommencer, sinon sur n'importe quelle touche")
    if(exit):break

    if(SO == 1):
        bode1(fct)
        black1(fct)
        niq1(fct)
    elif(SO == 2):
        bode2(fct)
        black2(fct)
        niq2(fct)



def bode1(fct):
    print("Bode1")

def black1(fct):
    print("black1")
    
def niq1(fct):
    print("niq1")
    
def bode2(fct):
    print("bode2")
    
def black2(fct):
    print("black2")
    
def niq2(fct):
    print("niq2")

def checkSO(fct):
    print("Result")