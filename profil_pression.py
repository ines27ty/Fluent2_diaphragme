import matplotlib.pyplot as plt
import numpy as np
from math import * 

# Tracé des profils de vitesse et de pression à partir des fichiers .xy de fluent
import matplotlib.pyplot as plt
import numpy as np
from math import *

# Entrée
# Ouvrir le fichier
with open("pressure_0.5_entree.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
P_lam= []
x_lam = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    P_lam.append(float(values[0]))
    x_lam.append(float(values[1]))


# Tracé du profil de pression d'entrée
plt.figure(0)
plt.plot(P_lam,x_lam,'r',label='P')
plt.xlabel('P')
plt.ylabel('x')
plt.title("Profil de pression à l'entrée")
plt.legend()
plt.show()

