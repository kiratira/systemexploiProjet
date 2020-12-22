import matplotlib.pyplot as plt
import numpy as np
from math import * 

#DataSO1 = [b0,a1,a0,T,K,f,s]
class data:
    b0 = 0.0
    a2 = 0.0
    a1 = 0.0
    a0 = 0.0
    T = 0.0
    K = 0.0
    ksi = 0.0
    f = range(100000)
    interval = 0.1
    iteration = 100000

    phaseBL2 = []
    gainBL2 = []
    phaseBL1 = []
    gainBL1 = []
    phaseBO2 = []
    gainBO2 = []
    phaseBO1 = []
    gainBO1 = []
    nicR1 = []
    nicR2 = []
    nicI1 = []
    nicI2 = []



def bode1(fct):
    print("Bode1")

def black1(data):
    pass
    
def niq1(fct):
    print("niq1")
    
def bode2(data):
    Module = []
    Gain = []
    Phase = []
    i = 0
    w = 0

    Module.append(data.K)
    while i < data.iteration:
        # Calcule du Gain avec la formule du SO2
        Module.append(float(sqrt((((1 - w**2 * data.T**2))**2) + (2 * w**2 * data.ksi**2 * data.T**2))))

        # On ajoute un element à la fin du tableau
        Gain.append(float(log10(data.K) * 20 - log10(Module[i]) * 20))

        # On fait l'arctg de la Phase avec la formule du SO2 (résultat en rad/s)
        artg = -atan2(float(2 * w * data.ksi * data.T), float(1 - w**2 * data.T**2))

        # On ajoute un element à la fin du tableau, en convertisant les rad/s en degrés
        Phase.append(degrees(artg))
        i+=1
        w += data.interval

    return Gain,Phase
    
def black2(data):
    Module = []
    Gain = []
    Phase = []
    i = 0
    w = 0

    Module.append(data.K)
    while i < 100000:
        # Calcule du Gain avec la formule du SO2
        Module.append(float(sqrt((((1 - w**2 * data.T**2))**2) + (2 * w**2 * data.ksi**2 * data.T**2))))

        # On ajoute un element à la fin du tableau
        Gain.append(float(log10(data.K) * 20 - log10(Module[i]) * 20))

        # On fait l'arctg de la Phase avec la formule du SO2 (résultat en rad/s)
        artg = -atan2(float(2 * w * data.ksi * data.T), float(1 - w**2 * data.T**2))

        # On ajoute un element à la fin du tableau, en convertisant les rad/s en degrés
        Phase.append(degrees(artg))
        i+=1
        w += data.interval

    Module.append(data.K)
    return Gain,Phase
    
def niq2(data):
    values = []

    w0 = 1/data.T
    #création de la liste contenant les données   
    w = -(data.iteration*data.interval)

    #le premier point ou w = -infini, F vaut donc 
    values.append(0+0j)

    #calcul d'un certain nombre de points séparé d'une certaine valeur 
    while w <= (data.iteration*data.interval) :
        values.append(data.K/(1+2j*data.ksi*(w/w0)-(w/w0)**2))
        w = w+data.interval

    #le dernier point ou w = infini, F vaut donc 0
    values.append(0+0j)
    xReal = [x.real for x in values]
    xIm = [x.imag for x in values]

    return xReal, xIm



def computeDataSO1(data):  
    data.T = data.a1/data.a0
    data.K = data.b0/data.a0
    runPlot(1)


def computeDataSO2(data):  
    data.T = (data.a2/data.a0)**0.5
    data.K = data.b0/data.a0
    data.ksi = 0.5*((data.a1**2 /data.a0*data.a2)**0.5)
    runPlot(2)

def getInputData(data):
    data.b0 = float(input("Entrer b0 = "))     
    data.a2 = float(input("Entrer a2 = "))        
    data.a1 = float(input("Entrer a1 = "))        
    data.a0 = float(input("Entrer a0 = "))

def runPlot(SO):
    if(SO == 1):
        bode1(dataG)
        black1(dataG)
        niq1(dataG)
        showPlot(dataG, 1)
        
    else:
        dataG.gainBO2, dataG.phaseBO2 = bode2(dataG)
        dataG.gainBL2, dataG.phaseBL2 = black2(dataG)
        dataG.nicR2, dataG.nicI2 = niq2(dataG)
        showPlot(dataG, 2)

def showPlot(data, SO):
    if(SO == 1):
        pass
    else :
        # Graphique Frequence (Bode)
        plt.subplot(2, 1, 1)
        plt.semilogx(data.f, data.gainBO2)
        plt.xlabel('rad/s')
        plt.ylabel('dB')
        plt.title("Diagramme de Bode")
        plt.grid()
        

        # Graphique degrés (Bode)
        plt.subplot(2, 1, 2)
        plt.semilogx(data.f, data.phaseBO2)
        plt.xlabel('rad/s')
        plt.ylabel('Phase')
        plt.grid()
        plt.figure()

        # Graphique Black
        plt.subplot(1, 1, 1)
        plt.plot(data.phaseBL2, data.gainBL2)
        plt.xlabel('Phase')
        plt.ylabel('dB')
        plt.title("Black")
        plt.grid()
        plt.figure()

        #Graphique Nic
        plt.subplot(1,1,1)
        plt.plot(data.nicR2,data.nicI2)
        plt.xlabel('reels')
        plt.ylabel('imaginaires')
        plt.title("fonction de nyquist")
    
        plt.show()


#=======================MAIN================================================

dataG = data()


while 1:
    getInputData(dataG)
    computeDataSO1(dataG) if(dataG.a2 == 0 ) else computeDataSO2(dataG)

    #Utilisation des fonctions de plot SO1 ou SO2

    exit = int(input("Appuyer sur '1' pour recommencer, sinon sur n'importe quelle touche"))
    if(exit != 1):break