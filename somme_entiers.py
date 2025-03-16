"""
Le but de l'exercice est de calculer la somme des 100 premiers entiers naturels !

Pour information : 
vous êtes sur les pas du célèbre mathématicien Gauss
https://fr.wikipedia.org/wiki/Somme_(arithm%C3%A9tique)
"""

# 1) Utilisez une boucle et la fonction "range" pour calculer la somme.
# Testez et récupérez le résultat en faisant tourner le code (> "Run")
i=1
n=0
for i in range(100):
    i+=1
    n=i+n
print(n)
# 2) Assignez le résultat obtenu dans la variable "solution" pour vérification
solution = n

# Ne touchez pas le print ci-dessous :)
print(f"{solution} est la bonne valeur de la somme !" if solution == (100 * 101) / 2 else "Raté")

i=1
n=0
for i in range(100):
   i+=1
   n=n+i
print(n)