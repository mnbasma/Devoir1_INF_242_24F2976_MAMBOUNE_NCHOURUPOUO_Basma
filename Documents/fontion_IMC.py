import numpy as np
import matplotlib.pyplot as plt

#génération de 100 valeurs aléatoires
tailles = np.random.uniform(1.4, 2.0, 100)
masses = np.random.uniform(45, 110, 100)

#pour que le graphique soit lisible
tailles.sort()
masses.sort()
x, y = np.meshgrid(tailles, masses)

#calcul de l'IMC
z = y / (x**2)

#affichage
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(tailles, masses, masses/(tailles**2), c='red', marker='o')
    
# surface 
surf = ax.plot_surface (x, y, z, cmap='magma')

ax.set_title("IMC générer avec des valeuurs aléatoire")
ax.set_xlabel("taille (m)")
ax.set_ylabel("masse(kg)")

plt.show()