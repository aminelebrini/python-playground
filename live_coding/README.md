# Live coding : analyse et visualisation de données

Atelier pratique d'analyse de transactions commerciales avec **Python**,
**Pandas**, **Matplotlib** et **Seaborn**.

Le projet explore les catégories de produits, les méthodes de paiement, les
montants des transactions, les remises et les corrélations. Les résultats sont
présentés sous forme de graphiques et d'exemples pédagogiques dans un notebook.

## Sommaire

- [Données](#données)
- [Contenu du projet](#contenu-du-projet)
- [Installation](#installation)
- [Exécuter l'analyse](#exécuter-lanalyse)
- [Ouvrir le notebook](#ouvrir-le-notebook)
- [Notions abordées](#notions-abordées)
- [Technologies](#technologies)

## Données

Le fichier utilisé par le projet est [`project1_df.csv`](project1_df.csv).
Il s'agit d'un jeu de données de transactions issues d'un site e-commerce.

Si le fichier CSV n'est pas présent, il peut être téléchargé depuis la source
Kaggle :

**[Télécharger le jeu de données sur Kaggle](https://www.kaggle.com/datasets/shrishtimanja/ecommerce-dataset-for-data-analysis)**

Après téléchargement, placez le fichier CSV dans le dossier `live_coding` et
conservez le nom `project1_df.csv`.

## Contenu du projet

| Fichier | Description |
| --- | --- |
| [`main.py`](main.py) | Script principal d'analyse et de visualisation |
| [`project1_df.csv`](project1_df.csv) | Jeu de données des transactions |
| [`presentation.ipynb`](presentation.ipynb) | Notebook pédagogique sur Matplotlib et Seaborn |
| [`generate_notebook.py`](generate_notebook.py) | Script de génération du notebook |
| `bar.png`, `hist.png`, `subplots.png` | Exemples de graphiques générés |
| `ven/` | Environnement virtuel local |

## Installation

Depuis le dossier `live_coding`, créez un environnement virtuel puis installez
les dépendances :

```bash
python3 -m venv ven
source ven/bin/activate
python -m pip install --upgrade pip
python -m pip install pandas matplotlib seaborn jupyter
```

Si l'environnement `ven/` existe déjà, activez-le simplement :

```bash
source ven/bin/activate
```

## Exécuter l'analyse

```bash
cd live_coding
source ven/bin/activate
python main.py
```

Le script affiche les résultats dans le terminal et génère plusieurs
visualisations avec Matplotlib et Seaborn.

## Ouvrir le notebook

Pour lancer le notebook pédagogique :

```bash
jupyter notebook presentation.ipynb
```

Pour le régénérer à partir du script Python :

```bash
python generate_notebook.py
```

## Notions abordées

- Chargement et exploration d'un fichier CSV avec Pandas
- Vérification des dimensions, des types et des valeurs manquantes
- Agrégation avec `value_counts()` et `groupby()`
- Graphiques Matplotlib : barres, courbes, histogrammes et nuages de points
- Graphiques Seaborn : `countplot`, `barplot`, `histplot`, `boxplot` et `scatterplot`
- Calcul et représentation d'une matrice de corrélation avec une heatmap
- Interprétation des ventes, des remises et des moyens de paiement

## Structure du dataset

Les principales colonnes utilisées sont :

| Colonne | Description |
| --- | --- |
| `Purchase Date` | Date et heure de la transaction |
| `Product Category` | Catégorie du produit |
| `Gross Amount` | Montant avant remise |
| `Discount Amount (INR)` | Montant de la remise |
| `Net Amount` | Montant net de la transaction |
| `Purchase Method` | Moyen de paiement |
| `Gender`, `Age Group` | Informations démographiques |
| `Location` | Ville de la transaction |

## Technologies

- Python 3
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook
