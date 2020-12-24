"""
Alexio Goossens et Youri Iacono 20/12/2020
"""

from math import *
import matplotlib.pyplot as plt

b0 = 100
a2 = 1
a1 = 2
a0 = 3

# Calcule de K (Gain statique)
K = b0 / a0

# Caclule du A2(s^2)
A2 = a2 / a0

# Calcule du A1(s)
A1 = a1 / a0

# Calcule du A0
A0 = a0 / a0

# Calcule du T (Constante temporelle du SO2)
T = sqrt(A2)

# Calcule du KSI (Coefficient d'amortissement du SO2)
KSI = A1 / (T * 2)

# Boucle pour calculer les xier échantillon du graphique
Gain = []
Phase = []
nombre_echantillon = 10000
Frequence = range(nombre_echantillon)
interval = 0.1
w = 0

i = 0
while i < nombre_echantillon:
    # Calcule du Gain avec la formule du SO2
    module = sqrt((1 - (pow(w, 2) * pow(T, 2))) ** 2
                  + 2 * pow(w, 2) * pow(KSI, 2) * pow(T, 2))

    # On ajoute un element à la fin du tableau
    gain = log10(K) * 20 - log10(module) * 20
    Gain.append(gain)

    # Calcule de la Phase avec la formule du SO2
    phase_imaginaires = 2 * w * KSI * T
    phase_reels = 1 - (pow(w, 2) * pow(T, 2))

    # On fait l'arctg des 2 valeurs (résultat en rad/s)
    # Et on convertie les rad/s en degrés
    phase = degrees(-atan2(phase_imaginaires, phase_reels))

    # On ajoute un element à la fin du tableau
    Phase.append(phase)

    # # Code pour vérifier les valeurs de la boucle quand la boucle vaut i
    # if i == 0:
    #     print(f"Module : {module}, Gain : {gain}, Phase : {phase}")

    w += interval
    i += 1

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
