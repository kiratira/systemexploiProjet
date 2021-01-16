"""
thibaut rizzoli 08/12/2020
"""
import math, matplotlib.pyplot as plt

def decompose(A, B):
    """
    cette fonction récupère les valeurs du s^2 et du s afin de les convertir en T et en Ksi
    """
    try:
        T = A**0.5
        Ksi = B/(2*T)
        return T, Ksi
    except ZeroDivisionError :
        print ("division par zero impossible, A doit différent de 0")
    except :
        print("error")

def point(K, Ksi, w, w0):
    return K/(1+2j*Ksi*(w/w0)-(w/w0)**2)

def plot_nyquist(K = 1, A = 1, B = 1, interval = 0.0001,iterations = 100000):
    """
    cette fonction récupère les données de la fonction de transfert et les exploites afin d'obtenir une courbe de nyquist
    """
    T, Ksi = decompose(A, B)
    w0 = 1/T
    #création de la liste contenant les données
    values =[]
    w = -(iterations*interval)
    #le premier point ou w = -infini, F vaut donc 0
    values.append(0+0j)
    #calcul d'un certain nombre de points séparé d'une certaine valeur 
    while w <= (iterations*interval) :
        F = point(K, Ksi, w, w0)
        values.append(F)
        w = w+interval
    #le dernier point ou w = infini, F vaut donc 0
    values.append(0+0j)

    print("A={0}, B={1}, K={2}, T={3}, Ksi={4}".format(A, B, K, T, Ksi),end=" ")
    #subdivision des valeurs complexes en deux listes, reels et imaginaires
    xReal = [x.real for x in values]
    xImg = [x.imag for x in values]
    nyquist = plt.plot(X,Y)
    nyquist.xlabel('reels')
    nyquist.ylabel('imaginaires')
    nyquist.title("fonction de nyquist")
    return nyquist


if __name__ == "__main__":
    print("lancement de la procedure de test")
    print("decompose:", end=" ")
    T, Ksi = decompose(4,2)
    if T==2 and Ksi== 0.5:
        print("success")
    else:
        print("les valeurs ne sont pas correctes")

    print("plot_nyquist:", end=" ")
    nyquist = plot_nyquist()
    nyquist.show()
