# Scéance 1 : Edited by Nailec
# git on 16/12/2024
a, b = 2, 5
operations = {
    "somme": a + b,
    "différence": a - b,
    "produit": a * b,
    "quotient": a / b,
    "exposant": a ** b
}

for nom, resultat in operations.items():
    print(f"La {nom} de a et b est {resultat}")
