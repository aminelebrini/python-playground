import numpy as np
import pandas as pd


class SurveillanceCapteurs:

    def __init__(self, chemin_fichier):
        self.chemin_fichier = chemin_fichier
        self.df = None

    def charger_donnees(self):
        self.df = pd.read_csv(self.chemin_fichier)
        return self.df

    def ajouter_alerte(self):
        self.df["alerte"] = np.where(
            self.df["temperature"] > 30, "Alerte", "Normale"
        )
        return self.df

    def calculer_mediane(self):
        return np.median(self.df["temperature"])

    def jours_superieurs_mediane(self):
        mediane = self.calculer_mediane()
        return self.df.loc[self.df["temperature"] > mediane, "jour"].tolist()

    def afficher_jours_alerte(self):
        return self.df.loc[self.df["alerte"] == "Alerte"]

    def trier_par_temperature(self):
        return self.df.sort_values(by="temperature", ascending=False)

    def calculer_ecart_temperature(self):
        temp_max = np.max(self.df["temperature"])
        temp_min = np.min(self.df["temperature"])
        return temp_max - temp_min

    def compter_alertes(self):
        return self.df["alerte"].value_counts()

    def afficher_stats_generales(self):
        return self.df.describe()

    def afficher_resultats(self):
        print("=== DONNÉES CHARGÉES ET ALERTES ===")
        print(self.df)
        print("\n=== SEMAINE / MÉDIANE ===")
        print(f"Température médiane : {self.calculer_mediane()} °C")
        print(
            f"Jours > médiane : {', '.join(self.jours_superieurs_mediane())}"
        )
        print("\n=== JOURS EN ALERTE (loc[]) ===")
        print(self.afficher_jours_alerte())
        print("\n=== TRI PAR TEMPÉRATURE ===")
        print(self.trier_par_temperature())
        print("\n=== ÉCART DE TEMPÉRATURE (Max - Min) ===")
        print(f"Écart : {self.calculer_ecart_temperature():.2f} °C")
        print("\n=== COMPTAGE DES ALERTES (value_counts) ===")
        print(self.compter_alertes())
        print("\n=== STATISTIQUES GÉNÉRALES (describe) ===")
        print(self.afficher_stats_generales())


# Test d'exécution
capteurs = SurveillanceCapteurs("capteurs.csv")
capteurs.charger_donnees()
capteurs.ajouter_alerte()
capteurs.afficher_resultats()