# SURFACE REPRÉSENTATIVE DE DIFFÉRANTE FONCTIONS À PLUSIEURS VARIABLES

## Description
Ce projet python a pour but d'appliquer les notions abordées par rapport au fontions à plusieurs variables et permettre leur visualisatin tridimentionnelle. L'objectif est d'illustrer graphiquement à l'aide des outils de codage (VSCode dans notre cas) comment l'IMC, la fonction 1, 2 et 3 évoluent en fontion de leurs variables.

## 📐 Analyse Mathématique et Domaines de Définiton

Pour chaque fonction visualisée, nous avons déterminé son domaine de définition (Df) :

1. **Le Cône** : f(x,y) = racine_carrée(x² + y²)
   - **Condition** : Toujours définie car x² + y² est toujours positif.
   - **Domaine** : Df = R² (tous les nombres réels).

2. **Les Ondes Circulaires** : f(x,y) = sin(racine_carrée(x² + y²))
   - **Domaine** : Df = R².

3. **La Gaussienne Modifiée** : f(x,y) = (x² + 3y²) * exp(-x² - y²)
   - **Domaine** : Df = R².

4. **Le Sinus Cardinale 2D** : f(x,y) = (sin x + sin y) / (x * y)
   - **Condition** : Le dénominateur ne doit pas être nul.
   - **Domaine** : Df = Tous les points (x, y) sauf quand x = 0 ou y = 0.

5. **L'Indice de Masse Corporelle (IMC)** : IMC = Masse / (Taille²)
   - **Condition** : La taille et la masse doivent être supérieures à 0.
   - **Domaine** : Taille > 0 et Masse > 0.

## Fontionnalités
* **Calcul automatisée**: Utilisation de la formule IMC= masse (kg)/taille^2(m) pour la fontion IMC

* **Visualisation 3D**: Génération s'une surface interactive avec 'Matplotib' pour chacune de ces fonctions


## Installation
Pour éxécuter ce code, installez les dépendances nécessaires
```bash
pip install numpy matplotlib
```
## STRUCTURE DU PROJET
* fonction_IMC.py: code source permettant de donner la surface représentative de l'IMC avec des valeurs aléatoires
* devoir_de_data_science_1.py: code source permettant de donner la surface représentative de la 1ère fontion donnée
* devoir_de_data_science_2.py: code source permettant de donner la surface représentative de la 2ème fontion donnée
* devoir_de_data_science_3.py: code source permettant de donner la surface représentative de la 3ème fontion donnée

## Cadre du projet
Ce travail a été réalisé dans le cadre de la consolidation d'une séance de cours de data sciences sur la manipulation des fonctions à plusieurs variables
