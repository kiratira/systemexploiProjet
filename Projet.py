"""
Alexio Goossens et Youri Iacono 20/12/2020
"""

from math import *
import matplotlib.pyplot as plt


b0 = 100
a2 = 1
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
K = b0/a0

# Caclule du A2(s^2)
A2 = a2/a0

# Calcule du A1(s)
A1 = a1/a0

# Calcule du A0
A0 = a0/a0

# Calcule du T
T = sqrt(A2)
valeur = T * 2

# Calcule du KSI
KSI = A1/valeur

Module.append(K)

# Boucle pour calculer 10000 points du graphique
while i < 10000:

    # Calcule du Gain avec la formule du SO2
    valeur1 = (1 - (pow(w, 2) * pow(T, 2)))**2
    valeur2 = 2 * pow(w, 2) * pow(KSI, 2) * pow(T, 2)
    module = sqrt(valeur1 + valeur2)
    Module.append(module)

    # On ajoute un element à la fin du tableau
    gain = log10(K) * 20 - log10(Module[i]) * 20
    Gain.append(gain)

    # Calcule de la Phase avec la formule du SO2
    valeur5 = 2 * w * KSI * T
    valeur6 = 1 - (pow(w, 2) * pow(T, 2))

    # On fait l'arctg des 2 valeurs (résultat en rad/s)
    valeur7 = -atan2(valeur5, valeur6)

    # On convertie les rad/s en degrés
    phase = degrees(valeur7)

    # On ajoute un element à la fin du tableau
    Phase.append(phase)
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
