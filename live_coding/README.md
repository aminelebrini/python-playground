# Live coding : analyse et visualisation de données

Ce dossier contient un atelier pratique consacré à l'analyse de données avec
Pandas, Matplotlib et Seaborn.

Le projet utilise un jeu de données de transactions commerciales situé dans
`project1_df.csv`. L'analyse explore les catégories de produits, les méthodes
de paiement, les montants des transactions, les remises et les corrélations,
puis représente les résultats avec plusieurs graphiques.

## Contenu du dossier

| Fichier | Description |
| --- | --- |
| `main.py` | Script complet d'analyse et de visualisation |
| `project1_df.csv` | Jeu de données des transactions |
| `presentation.ipynb` | Notebook pédagogique sur Matplotlib et Seaborn |
| `generate_notebook.py` | Script de génération du notebook |
| `bar.png`, `hist.png`, `subplots.png` | Images de visualisation produites pendant l'atelier |
| `ven/` | Environnement virtuel local du projet |

## Notions abordées

- Chargement et exploration d'un fichier CSV avec Pandas
- Vérification des dimensions, types, statistiques et valeurs manquantes
- Agrégation avec `value_counts()` et `groupby()`
- Graphiques Matplotlib : barres, courbes, histogrammes et nuages de points
- Graphiques Seaborn : countplot, barplot, histplot, boxplot et scatterplot
- Calcul et représentation d'une matrice de corrélation avec une heatmap
- Interprétation de résultats liés aux ventes, aux remises et aux moyens de paiement

## Installation

Depuis ce dossier, créez ou activez un environnement virtuel :

```bash
python3 -m venv ven
source ven/bin/activate
python -m pip install --upgrade pip
python -m pip install pandas matplotlib seaborn jupyter
```

L'environnement `ven/` est déjà présent dans le dossier. Vous pouvez donc
simplement l'activer :

```bash
source ven/bin/activate
```

## Exécuter l'analyse

Placez-vous dans le dossier `live_coding`, car le script charge le CSV avec un
chemin relatif :

```bash
cd live_coding
source ven/bin/activate
python main.py
```

Le script affiche les résultats dans le terminal et ouvre les visualisations
Matplotlib et Seaborn.

## Utiliser le notebook

Pour lancer Jupyter Notebook :

```bash
jupyter notebook presentation.ipynb
```

Le notebook présente progressivement les notions de visualisation, avec des
exemples sur les colonnes du dataset comme `Product Category`, `Net Amount`,
`Gross Amount`, `Gender` et `Purchase Method`.

Pour régénérer le notebook à partir du script Python :

```bash
python generate_notebook.py
```

## Structure du dataset

Les principales colonnes utilisées sont :

- `Purchase Date` : date et heure de la transaction
- `Product Category` : catégorie du produit
- `Gross Amount` : montant avant remise
- `Discount Amount (INR)` : montant de la remise
- `Net Amount` : montant net de la transaction
- `Purchase Method` : moyen de paiement
- `Gender` et `Age Group` : informations démographiques
- `Location` : ville de la transaction

## Technologies

- Python 3
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook
