from numpy import array

def saisir(min, max):
    n = int(input("Donner la taille du tableau (entre " + str(min) + " et " + str(max) + ") = "))
    while not (min <= n <= max):
        n = int(input("Donner la taille du tableau (entre " + str(min) + " et " + str(max) + ") = "))
    return n

def verif(ch):
    i = 0
    valide = True
    while i < len(ch) and valide:
        if "0" <= ch[i] <= "9":
            i = i + 1
        else:
            valide = False
    return valide

def remplir(t, n):
    for i in range(n):
        t[i] = input("t[" + str(i) + "] = ")
        while verif(t[i]) == False or len(t[i]) != 14:
            t[i] = input("t[" + str(i) + "] = ")

def inverse(ch):
    ch0 = ""
    for i in range(len(ch)):
        ch0 = ch[i] + ch0
    return ch0

def calcul(ch1):
    ch = inverse(ch1) 
    total = 0
    
    for i in range(len(ch)):
        digit = int(ch[i])
        
        if i % 2 == 0: 
            dbl = digit * 2
            if dbl > 9:
                total += (dbl // 10) + (dbl % 10)
            else:
                total = dbl + total
        else:
            total = digit + total

    controle = (10 - (total % 10)) % 10
    return controle

def former(dest, src, n):
    for i in range(n):
        ctrl = calcul(src[i])
        dest[i] = src[i] + str(ctrl)

def affichage(t, n):
    for i in range(n):
        print(t[i], end=" | ")
    print()

# PROGRAMME PRINCIPAL
n = saisir(1, 10)
t = array([str] * n)
remplir(t, n)
carte = array([str] * n)
former(carte, t, n)
print("Tableau final : ")
affichage(carte, n)

# créé par amineTNYT
# github: amineTNYT

