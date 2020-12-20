"""
Alexio Goossens 20/12/2020
"""

import matplotlib.pyplot as plt
from math import *


b0 = input("Entrer la valeur de b0: ")
a2 = input("Entrer la valeur de a2: ")
a1 = input("Entrer la valeur de a1: ")
a0 = input("Entrer la valeur de a0: ")

Module=[]
Gain=[]
Phase=[]
i=0
Frequence=range(10000)
interval=0.1
w=0

K=int(b0)/int(a0)                       #Calcule de K
A2=int(a2)/int(a0)                          #Caclule du A2(s^2)
A1=int(a1)/int(a0)                              #Calcule du A1(s)
A0=int(a0)/int(a0)                                  #Calcule du A0
T=float(sqrt(A2))                                       #Calcule du T
valeur=float(T)*int(2)
KSI= float(A1)/float(valeur)                                #Calcule du KSI

Module.append(K)

while i<10000:          #Boucle pour calculer 10000 points du graphique
    
    valeur1= float((1 - (pow(w,2) * pow(T,2)))**2)          #Calcule du Gain avec la formule du SO2
    valeur2= float(2 * pow(w,2) * pow(KSI,2) * pow(T,2))
    valeur3=float(sqrt(valeur1 + valeur2))
    Module.append(valeur3)
    valeur4=float(log10(K) * 20) - float(log10(Module[i]) *20)
    Gain.append(valeur4)                                        #On ajoute un element à la fin du tableau

    valeur5=float(2*w*KSI*T)                                         #Calcule de la Phase avec la formule du SO2
    valeur6=float(1-(pow(w,2) * pow(T,2)))
    valeur7=-atan2(valeur5,valeur6)                                      #On fait l'arctg des 2 valeurs (résultat en rad/s)
    valeur8=degrees(valeur7)                                                 #On convertie les rad/s en degrés
    Phase.append(valeur8)                                                         #On ajoute un element à la fin du tableau 
    i+=1
    w=w+interval
    
Module.append(K)

plt.subplot(2,1,1)          #Graphique Frequence
plt.semilogx(Frequence,Gain)
plt.xlabel('rad/s')
plt.ylabel('dB')
plt.title("Diagramme de Bode")
plt.grid()

plt.subplot(2,1,2)          #Graphique degrés
plt.semilogx(Frequence,Phase)
plt.xlabel('rad/s')
plt.ylabel('Phase')
plt.grid()

plt.show()


