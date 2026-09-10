import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ÉTAPE 1 : CHARGER ET EXPLORER LES DONNÉES

# Charger le dataset
df = pd.read_csv("project1_df.csv")

# Afficher les premières lignes
print("===== PREMIÈRES LIGNES =====")
print(df.head())


# Dimensions du dataset
print("\n===== DIMENSIONS =====")
print("Nombre de lignes :", df.shape[0])
print("Nombre de colonnes :", df.shape[1])


# Informations sur les colonnes
print("\n===== INFORMATIONS =====")
print(df.info())


# Vérifier les valeurs manquantes
print("\n===== VALEURS MANQUANTES =====")
print(df.isnull().sum())



# Statistiques générales
print("\n===== STATISTIQUES =====")
print(df.describe())


# ÉTAPE 2 : ANALYSE DES CATÉGORIES

# Catégories de produits
print("\n===== CATÉGORIES =====")
print(df["Product Category"].value_counts())


# Méthodes de paiement
print("\n===== MÉTHODES DE PAIEMENT =====")
print(df["Purchase Method"].value_counts())


# ÉTAPE 3 : STATISTIQUES SUR LES TRANSACTIONS

# Montant moyen des transactions
montant_moyen = df["Net Amount"].mean()

print("\n===== MONTANT MOYEN =====")
print("Montant moyen :", montant_moyen)


# Montant total des ventes
montant_total = df["Net Amount"].sum()

print("\n===== TOTAL DES VENTES =====")
print("Total des ventes :", montant_total)


# Remise moyenne
remise_moyenne = df["Discount Amount (INR)"].mean()

print("\n===== REMISE MOYENNE =====")
print("Remise moyenne :", remise_moyenne)


# Nombre de transactions par catégorie
transactions_categorie = df["Product Category"].value_counts()

print("\n===== TRANSACTIONS PAR CATÉGORIE =====")
print(transactions_categorie)



# ÉTAPE 4 : GROUPBY


# Ventes par catégorie
ventes_categorie = df.groupby("Product Category")["Net Amount"].sum()

print("\n===== VENTES PAR CATÉGORIE =====")
print(ventes_categorie)


# Montant moyen par catégorie
moyenne_categorie = df.groupby("Product Category")["Net Amount"].mean()

print("\n===== MONTANT MOYEN PAR CATÉGORIE =====")
print(moyenne_categorie)



# ÉTAPE 5 : MATPLOTLIB



# BAR CHART
# Nombre de transactions par catégorie


plt.figure(figsize=(8, 5))

transactions_categorie.plot(kind="bar")

plt.title("Nombre de transactions par catégorie")
plt.xlabel("Catégorie de produit")
plt.ylabel("Nombre de transactions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# LINE PLOT
# Évolution des ventes dans le temps


# Vérifier le nom de la colonne Purchase Date
print("\n===== COLONNES =====")
print(df.columns)


# Transformer la colonne Purchase Date en Purchase Datetime
df["Purchase Date"] = pd.to_datetime(df["Purchase Date"])

# Trier les données par Purchase Date
df = df.sort_values("Purchase Date")

# Calculer les ventes par Purchase Date
ventes_temps = df.groupby("Purchase Date")["Net Amount"].sum()

plt.figure(figsize=(12, 5))

plt.plot(ventes_temps.index, ventes_temps.values)

plt.title("Évolution du montant des ventes dans le temps")
plt.xlabel("Purchase Date")
plt.ylabel("Montant des ventes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# HISTOGRAMME
# Distribution du Net Amount


plt.figure(figsize=(8, 5))

plt.hist(df["Net Amount"], bins=30)

plt.title("Distribution du Net Amount")
plt.xlabel("Net Amount")
plt.ylabel("Nombre de transactions")
plt.tight_layout()
plt.show()



# ÉTAPE 6 : SEABORN


# Style général
sns.set_style("whitegrid")



# COUNTPLOT
# Transactions selon le moyen de paiement


plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="Purchase Method")

plt.title("Nombre de transactions par moyen de paiement")
plt.xlabel("Moyen de paiement")
plt.ylabel("Nombre de transactions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# BOXPLOT
# Montants selon le genre


plt.figure(figsize=(8, 5))

sns.boxplot(data=df, x="Gender", y="Net Amount")

plt.title("Montants des transactions selon le genre")
plt.xlabel("Genre")
plt.ylabel("Net Amount")
plt.tight_layout()
plt.show()



# BOXPLOT
# Montants selon la catégorie


plt.figure(figsize=(10, 5))

sns.boxplot(
    data=df,
    x="Product Category",
    y="Net Amount"
)

plt.title("Montants des transactions par catégorie")
plt.xlabel("Catégorie")
plt.ylabel("Net Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# SCATTERPLOT
# Gross Amount vs Discount Amount (INR)

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Gross Amount",
    y="Discount Amount (INR)"
)

plt.title("Relation entre Gross Amount et Discount Amount (INR)")
plt.xlabel("Gross Amount")
plt.ylabel("Discount Amount (INR)")
plt.tight_layout()
plt.show()


# ÉTAPE 7 : HEATMAP

# Sélectionner uniquement les colonnes numériques
numerical_df = df.select_dtypes(include="number")

# Calculer les corrélations
correlation = numerical_df.corr()

print("\n===== CORRÉLATIONS =====")
print(correlation)


plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Matrice de corrélation")
plt.tight_layout()
plt.show()


# ÉTAPE 8 : RÉPONSES AU CAS PRATIQUE

# Catégorie avec le plus de transactions
categorie_plus_transactions = df["Product Category"].value_counts().idxmax()

print("\n===== CAS PRATIQUE =====")

print(
    "1. Catégorie ayant le plus de transactions :",
    categorie_plus_transactions
)


# Méthode de paiement la plus utilisée
paiement_plus_utilise = df["Purchase Method"].value_counts().idxmax()

print(
    "2. Méthode de paiement la plus utilisée :",
    paiement_plus_utilise
)


# Distribution des montants
print(
    "3. Montant minimum :",
    df["Net Amount"].min()
)

print(
    "   Montant maximum :",
    df["Net Amount"].max()
)

print(
    "   Montant moyen :",
    df["Net Amount"].mean()
)


# Comparaison selon le genre
moyenne_genre = df.groupby("Gender")["Net Amount"].mean()

print("\n4. Montant moyen selon le genre :")
print(moyenne_genre)


# Corrélation Gross Amount / Discount Amount (INR)
correlation_discount = df["Gross Amount"].corr(
    df["Discount Amount (INR)"]
)

print(
    "\n5. Corrélation entre Gross Amount et Discount Amount (INR) :",
    correlation_discount
)


# ============================================
# CONCLUSION
# ============================================

print("\n===== CONCLUSION =====")

print(
    "Le dataset contient",
    len(df),
    "transactions."
)

print(
    "Le montant moyen d'une transaction est de",
    round(df["Net Amount"].mean(), 2)
)

print(
    "La catégorie la plus représentée est :",
    categorie_plus_transactions
)

print(
    "Le moyen de paiement le plus utilisé est :",
    paiement_plus_utilise
)

print(
    "La remise moyenne est de",
    round(df["Discount Amount (INR)"].mean(), 2)
)