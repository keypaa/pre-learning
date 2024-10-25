longueur = 0
largeur = 0

longueur = input("Please enter the lengh of the biggest sides of your shape: " )
largeur = input("Please enter the lengh of the smalles sides of your shape: " )

print(longueur, largeur)

if int(longueur) and int(largeur) <= 5:
    print("true")
else:
    print("false")

if int(longueur) and int(largeur) <= 0:
    print("Side's lengh must be greate than 0")
else:
    pass



