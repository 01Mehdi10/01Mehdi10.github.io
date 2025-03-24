# Année bissextile
print("Entre une année, format à 4 chiffres. 'Exemple = 2008' :", end = " ")
a = eval(input())
if a % 4 != 0: # non bissextile
    b = 0
else:
    if a % 100 == 0:  # non bissextile
        b = 0
    elif a % 400 == 0: # bissextile
        b = 1
    else:
        b = 1
if b == 0:
    print(a, "n'est pas une année bissextile.")
else:
    print(a, "est une année bissextile.")
