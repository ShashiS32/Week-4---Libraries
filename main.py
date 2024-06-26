name = []

while True:
    try:
        inp = input("Name")
        name.append(inp)
    except:
        break

print("Adieu, adieu, to" , end=" ")
if len(name) >2:
    for n in name[:-1]:
        print(n, end=", ")
    
    print('and', name[-1])

else:
    print(name[0], end="")
    if len(name) == 2:
        print(' and', name[1])