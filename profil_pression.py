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
P_lam_e= []
x_lam_e = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    P_lam_e.append(float(values[0]))
    x_lam_e.append(float(values[1]))

# Ouvrir le fichier
with open("pressure_200000_entree.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
P_turb_e= []
x_turb_e = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    P_turb_e.append(float(values[0]))
    x_turb_e.append(float(values[1]))

# Tracé du profil de pression d'entrée
plt.figure(0.1)
#plt.plot(P_lam_e,x_lam_e,'r',label='P_lam')
plt.plot(P_turb_e,x_turb_e,'r',label='P_turb')
plt.xlabel('P')
plt.ylabel('y')
plt.grid()
plt.title("Profil de pression à l'entrée")
plt.legend()


# Ligne 0.19
# Ouvrir le fichier
with open("pressure_0.5_line_0.19.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
P_lam_19= []
x_lam_19 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    P_lam_19.append(float(values[0]))
    x_lam_19.append(float(values[1]))

# Ouvrir le fichier
with open("pressure_200000_0.19.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
P_turb_19= []
x_turb_19 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    P_turb_19.append(float(values[0]))
    x_turb_19.append(float(values[1]))

# Tracé du profil de pression à la ligne 0.19 m
plt.figure(1.1)
#plt.plot(P_lam_19,x_lam_19,'r',label='P')
plt.plot(P_turb_19,x_turb_19,'r',label='P')
plt.xlabel('P')
plt.ylabel('y')
plt.grid()
plt.title("Profil de pression à la ligne 0.19 m")
plt.legend()


#Ligne orifice
# Ouvrir le fichier
with open("pressure_0.5_line_orifice.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
P_lam_or= []
x_lam_or = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    P_lam_or.append(float(values[0]))
    x_lam_or.append(float(values[1]))

# Ouvrir le fichier
with open("pressure_200000_orifice.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
P_tur_or= []
x_tur_or = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    P_tur_or.append(float(values[0]))
    x_tur_or.append(float(values[1]))

# Tracé du profil de pression à la ligne de l'orifice
plt.figure(2.1)
#plt.plot(P_lam_or,x_lam_or,'r',label='P')
plt.plot(P_tur_or,x_tur_or,'r',label='P')
plt.xlabel('P')
plt.ylabel('y')
plt.grid()
plt.title("Profil de pression à la ligne de l'orifice")
plt.legend()

#Ligne 0.21 m 
# Ouvrir le fichier
with open("pressure_0.5_line_021.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
P_lam_21= []
x_lam_21 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    P_lam_21.append(float(values[0]))
    x_lam_21.append(float(values[1]))

# Ouvrir le fichier
with open("pressure_200000_0.21.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
P_tur_21= []
x_tur_21 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    P_tur_21.append(float(values[0]))
    x_tur_21.append(float(values[1]))

# Tracé du profil de pression à la ligne 0.21 m
plt.figure(3)
#plt.plot(P_lam_21,x_lam_21,'r',label='P')
plt.plot(P_tur_21,x_tur_21,'r',label='P')
plt.xlabel('P')
plt.ylabel('y')
plt.grid()
plt.title("Profil de pression à la ligne 0.21 m")
plt.legend()

# Line 0.25 m

# Ouvrir le fichier
with open("pressure_0.5_line_0.25.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
P_lam_25= []
x_lam_25 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    P_lam_25.append(float(values[0]))
    x_lam_25.append(float(values[1]))

# Ouvrir le fichier
with open("pressure_200000_0.25.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
P_tur_25= []
x_tur_25 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    P_tur_25.append(float(values[0]))
    x_tur_25.append(float(values[1]))


# Tracé du profil de pression à la ligne 0.25 m
plt.figure(4)
#plt.plot(P_lam_25,x_lam_25,'r',label='P')
plt.plot(P_tur_25,x_tur_25,'r',label='P')
plt.xlabel('P')
plt.ylabel('y')
plt.grid()
plt.title("Profil de pression à la ligne 0.25 m")
plt.legend()

# Ligne 0.3 m 
# Ouvrir le fichier
with open("pressure_0.5_line_0.3.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
P_lam_30= []
x_lam_30 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    P_lam_30.append(float(values[0]))
    x_lam_30.append(float(values[1]))


# Ouvrir le fichier
with open("pressure_200000_0.3.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
P_tur_30= []
x_tur_30 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    P_tur_30.append(float(values[0]))
    x_tur_30.append(float(values[1]))

# Tracé du profil de pression à la ligne 0.30 m
plt.figure(5)
#plt.plot(P_lam_30,x_lam_30,'r',label='P')
plt.plot(P_tur_30,x_tur_30,'r',label='P')
plt.xlabel('P')
plt.ylabel('y')
plt.grid()
plt.title("Profil de pression à la ligne 0.30 m")
plt.legend()


# Tracé des profils de pression de toutes les lignes laminaire
plt.figure(6)
plt.plot(P_lam_e,x_lam_e,label='P_lam')
plt.plot(P_lam_19,x_lam_19,label='P_lam')
plt.plot(P_lam_or,x_lam_or,label='P_lam')
plt.plot(P_lam_21,x_lam_21,label='P_lam')
plt.plot(P_lam_25,x_lam_25,label='P_lam')
plt.plot(P_lam_30,x_lam_30,label='P_lam')
plt.xlabel('P')
plt.ylabel('y')
plt.grid()
plt.title("Profil de pression laminaire")
plt.legend()

# Tracé des profils de pression de toutes les lignes turbulentes
plt.figure(7)
plt.plot(P_turb_e,x_turb_e,label='P_turb')
plt.plot(P_turb_19,x_turb_19,label='P_turb')
plt.plot(P_tur_or,x_tur_or,label='P_turb')
plt.plot(P_tur_21,x_tur_21,label='P_turb')
plt.plot(P_tur_25,x_tur_25,label='P_turb')
plt.plot(P_tur_30,x_tur_30,label='P_turb')
plt.xlabel('P')
plt.ylabel('y')
plt.grid()
plt.title("Profil de pression turbulente")
plt.legend()

plt.show()