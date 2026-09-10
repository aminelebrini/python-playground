import json

notebook_content = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# 📊 Matplotlib & Seaborn\n",
                "\n",
                "---"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 1 : Introduction à Matplotlib**\n\n",
                "**📌 Définition** :\n",
                "**Matplotlib** est la bibliothèque standard de visualisation de données en Python. Elle permet de créer une grande variété de graphiques (lignes, barres, nuages de points, histogrammes...) statiques, animés et interactifs. Elle sert de base à d'autres outils comme Seaborn.\n\n",
                "**🎯 Objectif** : Comprendre à quoi sert Matplotlib et créer notre premier graphique.\n\n",
                "**📚 Travail à faire** :\n",
                "* Importer Matplotlib.\n",
                "* Créer un graphique simple.\n",
                "* Afficher le graphique."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import matplotlib.pyplot as plt\n\n",
                "x = [\"A\", \"B\", \"C\"]\n",
                "y = [10, 20, 15]\n\n",
                "plt.bar(x, y)\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**💡 Fonction à utiliser** :\n",
                "* `plt.bar()` : créer un graphique en barres.\n",
                "* `plt.show()` : afficher le graphique.\n\n",
                "---"
            ]
        },
        # Chapter 2
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 2 : Bar Chart**\n\n",
                "**🎯 Objectif** : Comparer plusieurs catégories avec un graphique en barres.\n\n",
                "**📚 Travail à faire** :\n",
                "* Compter les produits par catégorie.\n",
                "* Afficher le résultat avec `bar()`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "categories = df[\"Product Category\"].value_counts()\n\n",
                "plt.bar(categories.index, categories.values)\n\n",
                "plt.title(\"Produits par catégorie\")\n",
                "plt.xlabel(\"Catégorie\")\n",
                "plt.ylabel(\"Nombre\")\n\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**💡 Fonction à utiliser** :\n",
                "* `plt.bar()` : graphique en barres.\n\n",
                "---"
            ]
        },
        # Chapter 3
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 3 : Personnaliser un graphique**\n\n",
                "**🎯 Objectif** : Rendre un graphique plus clair et lisible.\n\n",
                "**📚 Travail à faire** :\n",
                "* Ajouter un titre.\n",
                "* Ajouter les noms des axes.\n",
                "* Modifier la taille du graphique.\n",
                "* Faire pivoter les labels."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "plt.figure(figsize=(10, 5))\n\n",
                "plt.bar(categories.index, categories.values)\n\n",
                "plt.title(\"Produits par catégorie\")\n",
                "plt.xlabel(\"Catégorie\")\n",
                "plt.ylabel(\"Nombre\")\n\n",
                "plt.xticks(rotation=45)\n\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**💡 Fonctions à utiliser** :\n",
                "* `plt.figure()` : taille du graphique.\n",
                "* `plt.title()` : titre.\n",
                "* `plt.xlabel()` : axe X.\n",
                "* `plt.ylabel()` : axe Y.\n",
                "* `plt.xticks()` : labels de X.\n\n",
                "---"
            ]
        },
        # Chapter 4
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 4 : Line Chart**\n\n",
                "**🎯 Objectif** : Visualiser une évolution, surtout dans le temps.\n\n",
                "**📚 Travail à faire** :\n",
                "* Créer des données.\n",
                "* Utiliser `plot()`.\n",
                "* Observer l'évolution."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "months = [\"Jan\", \"Feb\", \"Mar\", \"Apr\"]\n",
                "sales = [100, 150, 130, 180]\n\n",
                "plt.plot(months, sales, marker=\"o\")\n\n",
                "plt.title(\"Évolution des ventes\")\n",
                "plt.xlabel(\"Mois\")\n",
                "plt.ylabel(\"Ventes\")\n\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**💡 Fonction à utiliser** :\n",
                "* `plt.plot()` : graphique linéaire.\n\n",
                "---"
            ]
        },
        # Chapter 5
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 5 : Histogramme**\n\n",
                "**🎯 Objectif** : Observer la distribution d'une variable numérique.\n\n",
                "**📚 Travail à faire** :\n",
                "Afficher la distribution de `Net Amount`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "plt.hist(df[\"Net Amount\"], bins=20)\n\n",
                "plt.title(\"Distribution du Net Amount\")\n",
                "plt.xlabel(\"Net Amount\")\n",
                "plt.ylabel(\"Fréquence\")\n\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**💡 Fonction à utiliser** :\n",
                "* `plt.hist()` : créer un histogramme.\n",
                "* `bins` : nombre d'intervalles.\n\n",
                "---"
            ]
        },
        # Chapter 6
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 6 : Scatter Plot**\n\n",
                "**🎯 Objectif** : Observer la relation entre deux variables numériques.\n\n",
                "**📚 Travail à faire** :\n",
                "Comparer `Gross Amount` et `Net Amount`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "plt.scatter(\n",
                "    df[\"Gross Amount\"],\n",
                "    df[\"Net Amount\"]\n",
                ")\n\n",
                "plt.title(\"Gross Amount vs Net Amount\")\n",
                "plt.xlabel(\"Gross Amount\")\n",
                "plt.ylabel(\"Net Amount\")\n\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**💡 Fonction à utiliser** :\n",
                "* `plt.scatter()` : comparer deux variables numériques.\n\n",
                "---"
            ]
        },
        # Section Seaborn Header
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# 🎨 Seaborn\n\n",
                "---"
            ]
        },
        # Chapter 7
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 7 : Introduction à Seaborn**\n\n",
                "**📌 Définition** :\n",
                "**Seaborn** est une bibliothèque de visualisation basée sur Matplotlib. Elle facilite la création de graphiques statistiques complexes et attrayants en s'intégrant directement avec les DataFrames Pandas.\n\n",
                "**🎯 Objectif** : Découvrir Seaborn et comprendre comment l'utiliser avec Pandas.\n\n",
                "**📚 Travail à faire** :\n",
                "* Importer Seaborn.\n",
                "* Donner le DataFrame avec `data=df`.\n",
                "* Choisir une colonne avec `x`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import seaborn as sns\n\n",
                "sns.countplot(\n",
                "    data=df,\n",
                "    x=\"Gender\"\n",
                ")\n\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**💡 À retenir :**\n\n",
                "```python\n",
                "data=df\n",
                "```\n",
                "→ indique le DataFrame.\n\n",
                "```python\n",
                "x=\"Gender\"\n",
                "```\n",
                "→ indique la colonne utilisée.\n\n",
                "---"
            ]
        },
        # Chapter 8
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 8 : Countplot**\n\n",
                "**🎯 Objectif** : Compter automatiquement le nombre de lignes dans chaque catégorie.\n\n",
                "**📚 Travail à faire** :\n",
                "Afficher le nombre de transactions par genre."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "sns.countplot(\n",
                "    data=df,\n",
                "    x=\"Gender\"\n",
                ")\n\n",
                "plt.title(\"Transactions par genre\")\n\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**💡 Fonction à utiliser** :\n",
                "* `sns.countplot()` : compter les observations par catégorie.\n\n",
                "---"
            ]
        },
        # Chapter 9
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 9 : Barplot**\n\n",
                "**🎯 Objectif** : Comparer une valeur numérique entre plusieurs catégories.\n\n",
                "**📚 Travail à faire** :\n",
                "Comparer le `Net Amount` moyen pour chaque catégorie."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "sns.barplot(\n",
                "    data=df,\n",
                "    x=\"Product Category\",\n",
                "    y=\"Net Amount\"\n",
                ")\n\n",
                "plt.title(\"Net Amount moyen par catégorie\")\n\n",
                "plt.xticks(rotation=45)\n\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**💡 À retenir :**\n\n",
                "`barplot()` calcule la **moyenne par défaut**.\n\n",
                "---"
            ]
        },
        # Chapter 10
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 10 : Histplot**\n\n",
                "**🎯 Objectif** : Créer facilement un histogramme avec Seaborn.\n\n",
                "**📚 Travail à faire** :\n",
                "Afficher la distribution de `Net Amount`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "sns.histplot(\n",
                "    data=df,\n",
                "    x=\"Net Amount\",\n",
                "    bins=20\n",
                ")\n\n",
                "plt.title(\"Distribution du Net Amount\")\n\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**💡 Fonction à utiliser** :\n",
                "* `sns.histplot()` : distribution d'une variable numérique.\n\n",
                "---"
            ]
        },
        # Chapter 11
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 11 : Scatterplot**\n\n",
                "**🎯 Objectif** : Visualiser la relation entre deux variables numériques.\n\n",
                "**📚 Travail à faire** :\n",
                "Comparer `Gross Amount` et `Net Amount`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "sns.scatterplot(\n",
                "    data=df,\n",
                "    x=\"Gross Amount\",\n",
                "    y=\"Net Amount\"\n",
                ")\n\n",
                "plt.title(\"Gross Amount vs Net Amount\")\n\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**💡 Fonction à utiliser** :\n",
                "* `sns.scatterplot()` : relation entre deux variables.\n\n",
                "---"
            ]
        },
        # Chapter 12
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 12 : Boxplot**\n\n",
                "**🎯 Objectif** : Observer la distribution et détecter les valeurs extrêmes (**outliers**).\n\n",
                "**📚 Travail à faire** :\n",
                "Analyser la distribution de `Net Amount`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "sns.boxplot(\n",
                "    data=df,\n",
                "    y=\"Net Amount\"\n",
                ")\n\n",
                "plt.title(\"Distribution du Net Amount\")\n\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**💡 Fonction à utiliser** :\n",
                "* `sns.boxplot()` : distribution + outliers.\n\n",
                "---"
            ]
        },
        # Chapter 13
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 13 : Heatmap**\n\n",
                "**🎯 Objectif** : Visualiser les corrélations entre les variables numériques.\n\n",
                "**📚 Travail à faire** :\n",
                "* Calculer la corrélation.\n",
                "* Afficher la matrice avec une heatmap."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "correlation = df.corr(numeric_only=True)\n\n",
                "sns.heatmap(\n",
                "    correlation,\n",
                "    annot=True\n",
                ")\n\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**💡 Fonctions à utiliser** :\n",
                "* `corr()` : calculer les corrélations.\n",
                "* `sns.heatmap()` : visualiser les corrélations.\n",
                "* `annot=True` : afficher les valeurs.\n\n",
                "---"
            ]
        },
        # Chapter 14
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 14 : Pandas + Matplotlib + Seaborn**\n\n",
                "**🎯 Objectif** : Comprendre comment les trois bibliothèques travaillent ensemble.\n\n",
                "**📚 Travail à faire** :\n",
                "* Utiliser Pandas pour analyser les données.\n",
                "* Utiliser Matplotlib ou Seaborn pour les visualiser."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "average = (\n",
                "    df.groupby(\"Product Category\")[\"Net Amount\"]\n",
                "    .mean()\n",
                ")\n\n",
                "average"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "sns.barplot(\n",
                "    x=average.index,\n",
                "    y=average.values\n",
                ")\n\n",
                "plt.title(\"Dépense moyenne par catégorie\")\n\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**💡 À retenir :**\n\n",
                "```text\n",
                "Pandas\n",
                "→ Analyse\n\n",
                "Matplotlib / Seaborn\n",
                "→ Visualisation\n",
                "```\n\n",
                "---"
            ]
        },
        # Chapter 15
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 15 : Choisir le bon graphique**\n\n",
                "**🎯 Objectif** : Choisir le graphique adapté à la question.\n\n",
                "**📚 Travail à faire** :\n\n",
                "Utiliser :\n",
                "* `bar` → comparer des catégories.\n",
                "* `plot` → évolution dans le temps.\n",
                "* `hist` → distribution.\n",
                "* `scatter` → relation entre deux variables.\n",
                "* `countplot` → compter des catégories.\n",
                "* `boxplot` → détecter les outliers.\n",
                "* `heatmap` → corrélations.\n\n",
                "**💡 Exemple :**\n\n",
                "```text\n",
                "Combien ?               → Countplot\n",
                "Comparer ?              → Barplot\n",
                "Évolution ?             → Line plot\n",
                "Distribution ?          → Histogram\n",
                "Relation ?              → Scatterplot\n",
                "Outliers ?              → Boxplot\n",
                "Corrélation ?           → Heatmap\n",
                "```\n\n",
                "---"
            ]
        },
        # Chapter 16
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### **Chapter 16 : Live Coding — Customer Transactions Analysis**\n\n",
                "**⏱️ Durée** : 1H\n\n",
                "**🎯 Objectif** : Analyser un dataset de 55 000 transactions clients (`project1_df.csv`) afin d'identifier des tendances sur les achats, les catégories de produits, les réductions et les montants en utilisant **Pandas**, **Matplotlib** et **Seaborn**.\n\n",
                "**🧠 Explication / Concept** : \n",
                "Mise en pratique de l'analyse exploratoire de données (EDA) et de la dataviz sur des données de ventes réelles comprenant les colonnes `Product Category`, `Net Amount`, `Gross Amount`, `Discount Amount (INR)`, `Purchase Method`, `Purchase Date` et `Gender`.\n\n",
                "**📚 Travail à faire** :\n",
                "* **Étape 1 : Préparation et analyse des données**\n",
                "  * Charger le dataset dans un DataFrame Pandas.\n",
                "  * Vérifier les dimensions, les types de données et les valeurs manquantes.\n",
                "  * Analyser la répartition des catégories de produits et des méthodes de paiement.\n",
                "  * Calculer le montant moyen des transactions, le montant total des ventes, la remise moyenne et le nombre de transactions par catégorie.\n",
                "  * Utiliser `groupby()` pour analyser les ventes par catégorie.\n",
                "* **Étape 2 : Visualisation avec Matplotlib**\n",
                "  * Créer un **Bar chart** du nombre de transactions par catégorie.\n",
                "  * Créer un **Line plot** de l'évolution du montant des ventes dans le temps.\n",
                "  * Créer un **Histogramme** de la distribution du `Net Amount`.\n",
                "  * Ajouter aux graphiques les titres, labels, légendes et axes adaptés.\n",
                "* **Étape 3 : Visualisation avec Seaborn**\n",
                "  * Utiliser `countplot()` pour comparer le nombre de transactions selon le moyen de paiement.\n",
                "  * Utiliser `boxplot()` pour comparer les montants des transactions selon le genre.\n",
                "  * Utiliser `boxplot()` pour analyser les montants selon la catégorie de produit.\n",
                "  * Utiliser `scatterplot()` pour étudier la relation entre `Gross Amount` et `Discount Amount`.\n",
                "  * Utiliser `heatmap()` pour visualiser les corrélations entre les variables numériques.\n",
                "* **Étape 4 : Cas pratique & Interprétation**\n",
                "  * Identifier la catégorie ayant le plus de transactions.\n",
                "  * Identifier la méthode de paiement la plus utilisée.\n",
                "  * Déterminer comment les montants des transactions sont distribués.\n",
                "  * Comparer les montants des transactions selon le genre.\n",
                "  * Identifier les relations entre les montants et les réductions.\n",
                "  * Formuler des conclusions stratégiques à partir des graphiques."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
            ]
        }
    ],
    "metadata": {
        "language_info": {
            "name": "python"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}

with open("presentation.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook_content, f, ensure_ascii=False, indent=2)

print("✅ Fichier presentation.ipynb créé avec succès !")