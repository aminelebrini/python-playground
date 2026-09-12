import numpy as np
import pandas as pd


class AnalyseVentes:

    datas = []

    def __init__(self):
        pass

    @staticmethod
    def get_data_csv():
        data = pd.read_csv("ventes.csv")
        AnalyseVentes.datas.clear()
        AnalyseVentes.datas.append(data)
        return AnalyseVentes.datas[0]

    @staticmethod
    def calcul_ca():
        data = AnalyseVentes.datas[0]
        ca = data["prix"] * data["quantite"]
        return ca

    @staticmethod
    def total_quantity_sale():
        data = AnalyseVentes.datas[0]
        total_vendu = data["quantite"].sum()
        return total_vendu

    @staticmethod
    def calc_price_mean():
        data = AnalyseVentes.datas[0]
        mean = np.mean(data["prix"])
        return mean

    @staticmethod
    def max_sale():
        data = AnalyseVentes.datas[0]
        max_sale = data.groupby("produit")["quantite"].sum().idxmax()
        return max_sale

    @staticmethod
    def best_seller():
        data = AnalyseVentes.datas[0].copy()
        data["ca"] = data["prix"] * data["quantite"]
        best_vendeur = data.groupby("vendeur")["ca"].sum().idxmax()
        return best_vendeur

    @staticmethod
    def display_summary():
        data = AnalyseVentes.datas[0].copy()
        data["ca"] = AnalyseVentes.calcul_ca()
        print("=== RESUME DES VENTES ===")
        print(data)
        print(f"\nQuantite totale vendue : {AnalyseVentes.total_quantity_sale()}")
        print(f"Prix moyen des produits : {AnalyseVentes.calc_price_mean():.2f}")
        print(f"Produit le plus vendu : {AnalyseVentes.max_sale()}")
        print(f"Meilleur vendeur (CA) : {AnalyseVentes.best_seller()}")


new = AnalyseVentes()
print(new.get_data_csv())
print(new.calcul_ca())
print(new.total_quantity_sale())
print(new.calc_price_mean())
print(new.max_sale())
print(new.best_seller())
new.display_summary()