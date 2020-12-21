"""
Alexio Goossens et Youri Iacono 20/12/2020
"""

import matplotlib.pyplot as plt
from math import *


b0 = input("Entrer la valeur de b0: ")
a2 = input("Entrer la valeur de a2: ")
a1 = input("Entrer la valeur de a1: ")
a0 = input("Entrer la valeur de a0: ")

Module = []
Gain = []
Phase = []
i = 0
Frequence = range(10000)
interval = 0.1
w = 0

# Calcule de K
K = int(b0)/int(a0)

# Caclule du A2(s^2)
A2 = int(a2)/int(a0)

# Calcule du A1(s)
A1 = int(a1)/int(a0)

# Calcule du A0
A0 = int(a0)/int(a0)

# Calcule du T
T = float(sqrt(A2))
valeur = float(T)*int(2)

# Calcule du KSI
KSI = float(A1)/float(valeur)

Module.append(K)

# Boucle pour calculer 10000 points du graphique
while i < 10000:

    # Calcule du Gain avec la formule du SO2
    valeur1 = float((1 - (pow(w, 2) * pow(T, 2)))**2)
    valeur2 = float(2 * pow(w, 2) * pow(KSI, 2) * pow(T, 2))
    valeur3 = float(sqrt(valeur1 + valeur2))
    Module.append(valeur3)
    valeur4 = float(log10(K) * 20) - float(log10(Module[i]) * 20)

    # On ajoute un element à la fin du tableau
    Gain.append(valeur4)

    # Calcule de la Phase avec la formule du SO2
    valeur5 = float(2 * w * KSI * T)
    valeur6 = float(1 - (pow(w, 2) * pow(T, 2)))

    # On fait l'arctg des 2 valeurs (résultat en rad/s)
    valeur7 = -atan2(valeur5, valeur6)

    # On convertie les rad/s en degrés
    valeur8 = degrees(valeur7)

    # On ajoute un element à la fin du tableau
    Phase.append(valeur8)
    i += 1
    w = w + interval

Module.append(K)

# Graphique Frequence (Bode)
plt.subplot(3, 1, 1)
plt.semilogx(Frequence, Gain)
plt.xlabel('rad/s')
plt.ylabel('dB')
plt.title("Diagramme de Bode")
plt.grid()

# Graphique degrés (Bode)
plt.subplot(3, 1, 2)
plt.semilogx(Frequence, Phase)
plt.xlabel('rad/s')
plt.ylabel('Phase')
plt.grid()

# Graphique Black
plt.subplot(3, 1, 3)
plt.plot(Phase, Gain)
plt.xlabel('Phase')
plt.ylabel('dB')
plt.grid()

plt.show()
