#Diaphragme à bord épais - Section circulaire
import matplotlib.pyplot as plt
import numpy as np

# Data : air
rho = 1.225 # masse volumique (kg/m3)
mu = 1.7894*10**-5 # viscosité dynamique (Pa.s) 
P = 101325 # pression (Pa)


# Description du modèle
Dh = D0

F1 = pi*D1**2/4
F0 = pi*D0**2/4

w1 = Q / F1
w0 = Q / F0

G = Q*rho

Re1 = w1 * D1 / nu
Re0 = w0 * D0 / nu

# Rugosité relative des parois de l’orifice 
Delta_barre = Delta / D0

# Coefficient d’effet de l'épaisseur du diaphragme
phi_Dh = (0.25 + 0.535 * (1/Dh)**8) / (0.05 + (1/Dh)**7)
tau = (2.4 - 1/Dh) * 10 **phi_Dh

# Coefficient de perte de charge 
#(Re_0 > 10^5)
if Re0 > 10**5:
    zeta1 = (0.5 *(1-F0/F1)**0.75 + tau*(1-F0/F1)**1.375 + (1-F1/F0)**2 + lambda_0/Dh) * (F1/F0)**2

#(Re_0 <10^5)
if Re0 < 10**5:
    zeta1quad = (0.5 *(1-F0/F1)**0.75 + tau*(1-F0/F1)**1.375 + (1-F1/F0)**2 + lambda_0/Dh) * (F1/F0)**2

# Perte de pression totale (Pa)
Delta_p = zeta1 * rho * w1**2 / 2

# Perte de charge totale de fluide (m) :
Delta_h = zeta1 * w1**2 / (2 * g)

# Coefficient de perte de pression
if 30 < Re0 < 10**5:
    zeta1 = zeta_phi* (F1/F0)**2 + eps_0 * zeta1quad
if 10 < Re0 <= 30:
    zeta1 = 33* (F1/F0)**2/Re0 + eps_0 * zeta1quad
if Re0 <= 10:
    zeta1 = 33* (F1/F0)**2/Re0

