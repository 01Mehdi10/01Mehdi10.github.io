# Présence d'un caractère

exp = "yeux verts émeraude"
ln = len(exp)
c = 0
ltr = "e"
yon = False
nc = 0
while c<ln:
    nl = exp[c]
    if nl == ltr:
       yon = True
       nc += 1
    c+=1
if yon == True:
    print ("l'expression -",exp, "- contient la\n lettre -", ltr,"-", nc, "fois")
else:
    print ("l'expression -",exp, "- ne contient\n pas la lettre -", ltr,"-")
