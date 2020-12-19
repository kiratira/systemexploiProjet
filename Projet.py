import matplotlib.pyplot as plt
import numpy as np


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

def checkSO(fct): #WIP
    for x in fct:
        if(x == "/"): break
        elif(x == "s"): return 2
    return 1

def data1(fct):
    b0check = False
    a1check = False
    b0 = ""
    a0 = ""
    a1 = ""
    for x in fct:
        if(not b0check and not a1check):
            if(x != "/" and x != " "): b0 += str(x)
            elif(x == "/"): 
               b0check = True
               continue
       
        if(b0check and not a1check):
            if(x != " " and x != "/"): a1 += str(x)
            elif(x == " "): 
                a1check = True
                continue
            
        elif(b0check and a1check):
            if(x != " "): a0 += str(x)
            
    data = [b0,a1,a0]  
    return data

def data2(fct):
    b0check = False
    a2check = False
    a1check = False
    b0= ""
    a0= ""
    a1= ""
    a2= ""
    for x in fct:
        if(not b0check and not a2check and not a1check):
            if(x != "/" and x != " "): b0 += str(x)
            elif(x == "/"): 
                b0check = True
                continue

        if(b0check and not a2check and not a1check):
            if(x != " " and x != "/"): a2 += str(x)
            elif(x == " "):
                print("Flag")
                a2check = True
                continue
            
        elif(b0check and a2check and not a1check):
            if(x != " "): a1 += str(x)
            elif(x == " "): 
                a1check = True
                continue
        
        elif(b0check and a2check and a1check):
            if(x != " "): a0 += str(x)
            
    data = [b0,a2,a1,a0]  
    return data

while 1:
    fct = input("Entrer la fonction: ")
    #choix du SO1 ou SO2
    SO = checkSO(fct)
    print("Votre est " + fct + """ 
    Cette Fonction est un SO""" + str(SO))
    #Extraction des donnes
    data = data2(fct)
    print(data)
    #Utilisation des fonctions de plot SO1 ou SO2

    exit = input("Appuyer sur '1' pour recommencer, sinon sur n'importe quelle touche")
    if(not exit):break

    if(SO == 1):
        bode1(fct)
        black1(fct)
        niq1(fct)
    elif(SO == 2):
        bode2(fct)
        black2(fct)
        niq2(fct)