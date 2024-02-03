import matplotlib.pyplot as plt
import numpy as np
from math import * 

# Tracé des profils de vitesse et de vitesse à partir des fichiers .xy de fluent
import matplotlib.pyplot as plt
import numpy as np
from math import *

# Entrée
# Ouvrir le fichier
with open("vitesse_0.5_entree.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
V_lam_e= []
x_lam_e = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    V_lam_e.append(float(values[0]))
    x_lam_e.append(float(values[1]))

# Ouvrir le fichier
with open("vitesse_200000_entree.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
V_turb_e= []
x_turb_e = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    V_turb_e.append(float(values[0]))
    x_turb_e.append(float(values[1]))

# Tracé du Profil de vitesse laminaire d'entrée
plt.figure(0.1)
plt.plot(V_lam_e,x_lam_e,'r',label='V_lam')
plt.xlabel('V')
plt.ylabel('y')
#plt.title("Profil de vitesse turbulent à l'entrée")
plt.title("Profil de vitesse laminaire à l'entrée")
plt.grid()
 


# Ligne 0.19
# Ouvrir le fichier
with open("vitesse_0.5_line_0.19.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
V_lam_19= []
x_lam_19 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    V_lam_19.append(float(values[0]))
    x_lam_19.append(float(values[1]))

# Ouvrir le fichier
with open("vitesse_200000_0.19.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
V_turb_19= []
x_turb_19 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    V_turb_19.append(float(values[0]))
    x_turb_19.append(float(values[1]))

# Tracé du Profil de vitesse laminaire à la ligne 0.19 m
plt.figure(1.1)
plt.plot(V_lam_19,x_lam_19,'r',label='P')
#plt.plot(V_turb_19,x_turb_19,'r',label='P')
plt.xlabel('V')
plt.ylabel('y')
#plt.title("Profil de vitesse turbulent à la ligne 0.19 m")
plt.title("Profil de vitesse laminaire à la ligne 0.19 m")
plt.grid()
 


#Ligne orifice
# Ouvrir le fichier
with open("vitesse_0.5_orifice.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
V_lam_or= []
x_lam_or = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    V_lam_or.append(float(values[0]))
    x_lam_or.append(float(values[1]))

# Ouvrir le fichier
with open("vitesse_200000_orifice.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
V_tur_or= []
x_tur_or = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    V_tur_or.append(float(values[0]))
    x_tur_or.append(float(values[1]))

# Tracé du Profil de vitesse laminaire à la ligne de l'orifice
plt.figure(2.1)
plt.plot(V_lam_or,x_lam_or,'r',label='P')
#plt.plot(V_tur_or,x_tur_or,'r',label='P')
plt.xlabel('V')
plt.ylabel('y')
#plt.title("Profil de vitesse turbulent à la ligne de l'orifice")
plt.title("Profil de vitesse laminaire à la ligne de l'orifice")
plt.grid()

#Ligne 0.21 m 
# Ouvrir le fichier
with open("vitesse_0.5_line_021.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
V_lam_21= []
x_lam_21 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    V_lam_21.append(float(values[0]))
    x_lam_21.append(float(values[1]))

# Ouvrir le fichier
with open("vitesse_200000_0.21.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
V_tur_21= []
x_tur_21 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    V_tur_21.append(float(values[0]))
    x_tur_21.append(float(values[1]))

# Tracé du Profil de vitesse laminaire à la ligne 0.21 m
plt.figure(3)
plt.plot(V_lam_21,x_lam_21,'r',label='P')
#plt.plot(V_tur_21,x_tur_21,'r',label='P')
plt.xlabel('V')
plt.ylabel('y')
#plt.title("Profil de vitesse turbulent à la ligne 0.21 m")
plt.title("Profil de vitesse laminaire à la ligne 0.21 m") 
plt.grid()

# Line 0.25 m

# Ouvrir le fichier
with open("vitesse_0.5_line_0.25.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
V_lam_25= []
x_lam_25 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    V_lam_25.append(float(values[0]))
    x_lam_25.append(float(values[1]))

# Ouvrir le fichier
with open("vitesse_200000_0.25.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
V_tur_25= []
x_tur_25 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    V_tur_25.append(float(values[0]))
    x_tur_25.append(float(values[1]))


# Tracé du Profil de vitesse laminaire à la ligne 0.25 m
plt.figure(4)
plt.plot(V_lam_25,x_lam_25,'r',label='P')
#plt.plot(V_tur_25,x_tur_25,'r',label='P')
plt.xlabel('V')
plt.ylabel('y')
#plt.title("Profil de vitesse turbulent à la ligne 0.25 m")
plt.title("Profil de vitesse laminaire à la ligne 0.25 m")
plt.grid()

# Ligne 0.3 m 
# Ouvrir le fichier
with open("vitesse_0.5_line_0.3.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
V_lam_30= []
x_lam_30 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    V_lam_30.append(float(values[0]))
    x_lam_30.append(float(values[1]))


# Ouvrir le fichier
with open("vitesse_200000_0.30.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
V_tur_30= []
x_tur_30 = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    V_tur_30.append(float(values[0]))
    x_tur_30.append(float(values[1]))

# Tracé du Profil de vitesse laminaire à la ligne 0.30 m
plt.figure(5)
plt.plot(V_lam_30,x_lam_30,'r',label='P')
#plt.plot(V_tur_30,x_tur_30,'r',label='P')
plt.xlabel('V')
plt.ylabel('y')
#plt.title("Profil de vitesse turbulent à la ligne 0.30 m")
plt.title("Profil de vitesse laminaire à la ligne 0.30 m")
plt.grid()


# Ligne sortie 
# Ouvrir le fichier
with open("vitesse_0.5_sortie.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
V_lam_s= []
x_lam_s = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    V_lam_s.append(float(values[0]))
    x_lam_s.append(float(values[1]))


# Ouvrir le fichier
with open("vitesse_200000_orifice.xy", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
V_tur_s= []
x_tur_s = []

# Parcourir chaque ligne du fichier
for line in lines:
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    V_tur_s.append(float(values[0]))
    x_tur_s.append(float(values[1]))

# Tracé du Profil de vitesse laminaire à la sortie
plt.figure(6)
plt.plot(V_lam_s,x_lam_s,'r',label='P')
#plt.plot(V_tur_s,x_tur_s,'r',label='P')
plt.xlabel('V')
plt.ylabel('y')
#plt.title("Profil de vitesse turbulent à la sortie")
plt.title("Profil de vitesse laminaire à la sortie")
plt.grid()
plt.show()