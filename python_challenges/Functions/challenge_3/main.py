import math
from collections import Counter

def calculer_factorielle():
    n = int(input("Entrez un nombre entier pour la factorielle : "))
    print(f"La factorielle de {n} est : {math.factorial(n)}")

def table_multiplication():
    m = int(input("Entrez un nombre entier pour la table de multiplication : "))
    print(f"Table de multiplication de {m} :")
    for i in range(1, 11):
        print(f"{m} x {i} = {m * i}")

def verifier_carre_parfait():
    L = int(input("Entrez un nombre entier pour vérifier s'il est un carré parfait : "))
    if L >= 0 and math.isqrt(L) ** 2 == L:
        print(f"{L} est un carré parfait.")
    else:
        print(f"{L} n'est pas un carré parfait.")

def afficher_caracteres():
    chaine = input("Entrez une chaîne de caractères : ")
    for char in chaine:
        print(char)

def mot_le_plus_long():
    phrase = input("Entrez une phrase : ")
    mots = phrase.split()
    if mots:
        plus_long = max(mots, key=len)
        print(f"Le mot le plus long est : '{plus_long}'")

def compter_occurrences():
    Ch = input("Entrez une chaîne de caractères : ")
    occurrences = Counter(Ch)
    for char, count in occurrences.items():
        print(f'Le caractère "{char}" figure {count} fois dans la chaîne Ch.')