import matplotlib.pyplot as plt
import numpy as np
import math

#DataSO1 = [b0,a1,a0,T,K,f,s]
class data:
    b0 = 0.0
    a2 = 0.0
    a1 = 0.0
    a0 = 0.0
    T = 0.0
    K = 0.0
    ksi = 0.0
    f = 0.0
    s = 0.0

def bode1(fct):
    print("Bode1")

def black1(data):
    Tjw = data.K / 1 + data.s * data.T
    mag = 20*np.log10(np.abs(Tjw))
    phase = np.arctan2(np.imag(Tjw),np.real(Tjw))*180/np.pi
    print("flag")
    plt.figure()
    plt.plot(phase,mag)
    plt.xlabel("Phase")
    plt.ylabel("Mag")
    plt.title("Black S01")
    plt.show
    print("flag2")
    
def niq1(fct):
    print("niq1")
    
def bode2(fct):
    print("bode2")
    
def black2(fct):
    print("black2")
    
def niq2(fct):
    print("niq2")


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
    else:
        bode2(dataG)
        black2(dataG)
        niq2(dataG)

#=======================MAIN================================================

dataG = data()
dataG.f = np.logspace(-2,4,1000)
dataG.s = 1.0j*(2*np.pi*dataG.f)

while 1:
    getInputData(dataG)
    computeDataSO1(dataG) if(data.a2 == 0 ) else compcomputeDataSO2(dataG)

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