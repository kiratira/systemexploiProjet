"""
Alexio Goossens et Youri Iacono 20/12/2020
"""

import matplotlib.pyplot as plt
from math import *


b0 = 1
a1 = 2
a0 = 3

Module = []
Gain = []
Phase = []
i = 0
Frequence = range(10000)
interval = 0.1
w = 0

# Calcule de K
K = int(b0)/int(a0)

# Calcule du A1(s)
A1 = int(a1)/int(a0)

# Calcule du A0
A0 = int(a0)/int(a0)


Module.append(K)

# Boucle pour calculer 10000 points du graphique
while i < 10000:

    # Calcule du Gain avec la formule du SO1
    valeur1=float((pow(A1,2) * pow(w,2)))
    valeur2=float(sqrt(A0 + valeur1))
    Module.append(valeur2)
    valeur3=float(log10(K) * 20) - float(log10(Module[i]) * 20)

    # On ajoute un element à la fin du tableau
    Gain.append(valeur3)

    # On fait l'arctg des 2 valeurs (résultat en rad/s)
    valeur4 = -atan2(w * A1, A0)

    # On convertie les rad/s en degrés
    valeur5 = degrees(valeur4)

    # On ajoute un element à la fin du tableau
    Phase.append(valeur5)
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
