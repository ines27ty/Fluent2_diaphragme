#Diaphragme à bord épais - Section circulaire
import matplotlib.pyplot as plt
import numpy as np
from math import * 
# Data : air
rho = 1.225             # masse volumique (kg/m3)
mu = 1.7894*10**-5      # viscosité dynamique (Pa.s) 
P = 101325              # pression (Pa)
g = 9.81                # accélération de la pesanteur (m/s2)
nu = mu / rho           # viscosité cinématique (m2/s)


# Données : tableur D0, D1 Re, DeltaP, zeta_simu, zeta_phi, zeta1
R0 = 0.034
R1 = 0.083
D0 = 2*R0
D1 = 2*R1
Dh = D0

tau = 1.3
l = 0.002
print("l/Dh = ", l/Dh)
# Ouvrir le fichier
with open("data_ines_1.txt", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
Re0= []
pdc_th = []
pdc_exp = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()         # Supprimer les espaces en début et fin de ligne
    line = line.replace('\t', ',')      # Remplacer les tabulations par des virgules
    values = line.split(',')     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    Re0.append(float(values[0]))
    pdc_th.append(float(values[1]))
    pdc_exp.append(float(values[2]))

# Tracé
plt.figure(0)
plt.semilogx(Re0,pdc_th,'r',label='zeta_théorique')
plt.semilogx(Re0,pdc_exp,'b',label='zeta_simulation',marker='o', linestyle='--')
plt.xlabel('Re_0')
plt.ylabel('Coeff de perte de charge zeta_1')
plt.title("F0/F1 = 0.17")
plt.legend()
plt.grid()
plt.show()
