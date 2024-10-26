import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&é'(-è_çà)=$^ù*!:;,@^[]#~²1234567890"
# numbers = "1234567890"
# specials = "&é'(-è_çà)=$^ù*!:;,@^[]#~²"
# password = ""
# n = input(print("enter a number"))
N = input("please enter a number of characters : ")
N = int(N)
result = []
for i in range(N):
    selected = random.choice(characters)
    #print(selected)
    result.append(selected)

print(result)
print("".join(result))

# je veux prendre n nombre de fois au hasard dans ma liste, les ajouter à une liste puis join tout 
# print("".join(password))
