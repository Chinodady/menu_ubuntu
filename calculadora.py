def suma(a,b):
    suma = a+b
    return suma

def resta(a,b):
    resta = a-b
    return resta

def divide(a,b):
    divide = a/b
    return divide

def multiplica (a,b):
    multiplica = a*b
    return multiplica

num1 = int(input("ingresa primer numero"))
num2 = int(input("ingresa segundo numero"))

print("selecciona una opcion")
print("1.- suma")
print("2.- resta")
print("3.- divide")
print("4.- multiplica")
print("5.- salir")

opcion = input()

if opcion == "1":
    print (suma(num1,num2))
elif opcion == "2":
    print (resta(num1,num2))
elif opcion == "3":
    print (divide(num1,num2))
elif opcion == "4":
    print (multiplica(num1,num2))
elif opcion == "5":
    pass
else:
    print("opciòn no valida")
