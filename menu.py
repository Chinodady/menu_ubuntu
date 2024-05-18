import subprocess
def ejecutar(comando):
    subprocess.run(comando, shell = True)

def menu():
    print("menu")
    print("1. crea promedio.txt")
    print("2. crea carpeta calificaciones")
    print("3. crea carpeta primer parcial")
    print("4. mueve promedio.txt dentro de primer parcial")
    print("5. dentro de la carpeta calificaciones crea comandos.py")
    print("6. enlista todas las carpetas")
    print("7. abre calcuadora")
    print("8. salir")

while True:
    menu()
    opcion = input("selecciona una opcion: ")
    if opcion == "1":
        ejecutar("touch promedio.txt")
    elif opcion == "2":
        ejecutar("mkdir calificaciones")
    elif opcion == "3":
        ejecutar("mkdir primer_parcial")
    elif opcion == "4":
        ejecutar("mv promedio.txt primer_parcial")
    elif opcion == "5":
        ejecutar("touch calificaciones/comandos.py")
    elif opcion == "6":
        ejecutar("ls -d */")
    elif opcion == "7":
        ejecutar("python calculadora.py")
    elif opcion == "8":
        break
    else:
        print("opcion no valida")
