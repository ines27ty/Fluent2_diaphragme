# Tracé des profils de vitesse et de pression à partir des fichiers .xy de fluent

# Lecture des fichiers .xy 
# Ouvrir le fichier
with open("data_ines.txt", 'r') as fichier:
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

