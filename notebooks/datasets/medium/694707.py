n = int(input())

for _ in range(n):
    cadena = input()
    new = ""
    cont =2
    
    for car in cadena:
        if ord(car) == 32:
            new+=car
        elif cont%2==0:
            new+=car.upper()
        else:
            new+=car.lower()
        if ord(car)!=32:
            cont+=1
    print(new)
 