# 1) Comprenez le code ci-dessous
a = True
b = False
c = True

if a and b:
    x = 5
elif not c:
    x = 4
elif a:
    x = 8
else:
    x = 7

# 2) Déduisez-en la valeur de x et assignez la dans la variable nommée "solution"
solution = 8

# 3) Vérifiez votre intuition en faisant tourner le code (> "Run")
print(f"{solution} est la bonne valeur de x !" if solution == x else "Raté")
