print("2- Calcule de puissance d'un nombre\n")

n = input("Entre le nombre pour calculer le résultat de son exposant :")   

# contrôle n contient uniquement des chiffres
success = False
while not success:
    try : n = int(n)
    except ValueError:
        n = input("N'utilise que des chiffres :")
    else:
        n = int(n)
        success = True

p = input("\nEntre le nombre qui sert d'exposant:")

# contrôle p contient uniquement des chiffres
success = False
while not success:
    try : p = int(p)
    except ValueError:
        p = input("N'utilise que des chiffres :")
    else:
        p = int(p)
        success = True

# calcule et affiche le résultat        
r=1
i=0
for i in range(1, p+1):
    r=r*n
print("\nLe résultat de ",n ,"^",p,"est :", r)