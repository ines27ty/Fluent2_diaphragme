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
D0 = 0.034
Dh = D0
D1 = 0.083

# Ouvrir le fichier
with open("data.txt", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
Re1 = []
w1 = []
w0 = []
w1_simu = []
delta_P = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()         # Supprimer les espaces en début et fin de ligne
    line = line.replace('\t', ',')      # Remplacer les tabulations par des virgules
    values = line.split(',')     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    Re1.append(float(values[0]))
    w1.append(float(values[1]))
    w0.append(float(values[2]))
    w1_simu.append(float(values[3]))
    delta_P.append(float(values[4]))

# Description du modèle

# Coefficient d’effet de l'épaisseur du diaphragme
#phi_Dh = (0.25 + 0.535 * (1/Dh)**8) / (0.05 + (1/Dh)**7)
tau = 1.3

# Tracer tau en fonction de 1/Dh entre 0 et 3
#Dh = np.linspace(0,3,10)
#phi_Dh = (0.25 + 0.535 * (1/Dh)**8) / (0.05 + (1/Dh)**7)
#plt.plot(1/Dh,phi_Dh)
#plt.xlabel('1/Dh')
#plt.ylabel('phi_Dh')
#plt.show()

F1 = np.pi*D1/4
F0 = np.pi*D0/4
#G = Q*rho

w1 = [Re1[i] * mu / (D1*rho)for i in range(len(w1))]
Re0 = [w0[i] * D0 / nu for i in range(len(w1))]


zeta_simu = [delta_P[i] * 2 / (rho * w1_simu[i]**2) for i in range(len(delta_P))]
lambda_0  = 0.02

zeta1 = [0 for i in range(len(Re0))]
# Coefficient de perte de charge 
#(Re_0 > 10^5)
for i in range (len(Re0)):
    if Re0[i] >= 10**5:
        zeta1[i] = (0.5 *(1-F0/F1)**0.75 + tau*(1-F0/F1)**1.375 + (1-F0/F1)**2 + lambda_0/Dh) * (F0/F1)**2 
    else : 
        zeta1[i] = 33* (F1/F0)**2 /Re0[i]

print(zeta1)

# Tracer zeta_1 et zeta_simu en fonction de Re_0 en échelle log
plt.figure(0)
plt.semilogx(Re0,zeta1,'r',label='zeta_théorique')
plt.semilogx(Re0,zeta_simu,'b',label='zeta_simulation')
plt.xlabel('Re_0')
plt.ylabel('zeta_theorique et zeta_simulation')
plt.legend()
plt.grid()
plt.show()
