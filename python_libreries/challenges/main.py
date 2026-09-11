import pandas as pd
import numpy as np
class AnalyseVentes:

    datas = []
    def __init__(self):
        pass


    @staticmethod
    def get_data_csv():
        data = pd.read_csv("vente.csv")
        AnalyseVentes.datas.append(data)
        return AnalyseVentes.datas

    
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
        max_sale = data.groupby('produit')['quantite'].sum().idxmax()
        return max_sale
    
new = AnalyseVentes()
print(new.get_data_csv())
print(new.calcul_ca())
print(new.total_quantity_sale())
print(new.calc_price_mean())
print(new.max_sale())