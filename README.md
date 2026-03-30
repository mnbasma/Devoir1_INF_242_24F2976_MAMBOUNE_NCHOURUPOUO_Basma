# SURFACE REPRÉSENTATIVE DE DIFFÉRANTE FONCTIONS À PLUSIEURS VARIABLES

## Description
Ce projet python a pour but d'appliquer les notions abordées par rapport au fontions à plusieurs variables et permettre leur visualisatin tridimentionnelle. L'objectif est d'illustrer graphiquement à l'aide des outils de codage (VSCode dans notre cas) comment l'IMC, la fonction 1, 2 et 3 évoluent en fontion de leurs variables.
        
## 📐 Analyse Mathématique et Domaines de Définition

Pour chaque fonction visualisée, nous avons défini son domaine de définition ($D_f$) dans l'ensemble $\mathbb{R}^2$ :

1. **Le Cône** : $f(x,y) = \sqrt{x^2 + y^2}$
   - **Condition** : La quantité sous la racine doit être $\geq 0$. Comme $x^2 + y^2$ est une somme de carrés, elle est toujours positive.
   - **Domaine** : $D_f = \mathbb{R}^2$

2. **Les Ondes Circulaires** : $f(x,y) = \sin(\sqrt{x^2 + y^2})$
   - **Condition** : La fonction sinus est définie sur $\mathbb{R}$.
   - **Domaine** : $D_f = \mathbb{R}^2$

3. **La Gaussienne Modifiée** : $f(x,y) = (x^2 + 3y^2)e^{-x^2 - y^2}$
   - **Condition** : Les polynômes et l'exponentielle sont définis partout sur $\mathbb{R}$.
   - **Domaine** : $D_f = \mathbb{R}^2$

4. **Le Sinus Cardinale 2D (Modifié)** : $f(x,y) = \frac{\sin x + \sin y}{xy}$
   - **Condition** : Le dénominateur ne doit pas être nul ($xy \neq 0$), ce qui implique $x \neq 0$ et $y \neq 0$.
   - **Domaine** : $D_f = \{ (x, y) \in \mathbb{R}^2 \mid x \neq 0 \text{ et } y \neq 0 \}$

5. **L'Indice de Masse Corporelle (IMC)** : $f(T, M) = \frac{M}{T^2}$
   - **Condition** : Physiquement, la taille ($T$) et la masse ($M$) doivent être strictement positives.
   - **Domaine** : $D_f = ]0 ; +\infty[ \times ]0 ; +\infty[$

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
