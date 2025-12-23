# En un módulo se escriben las funciones o las clases
# En el archivo main, se importan los módulos que necesitamos usar.

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calculadora():
    while True:
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = int(input("Ingrese su opción: "))

        if opcion in [1, 2, 3, 4]:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

        match opcion:
            case 5:
                print("Saliendo de la calculadora.")
                break
            case 1:
                print("La suma es:", suma(num1, num2))
            case 2:
                print("La resta es:", resta(num1, num2))
            case 3:
                print("La multiplicación es:", multiplicar(num1, num2))
            case 4:
                print("La división es:", dividir(num1, num2))
            case _:
                print("Opción no válida, intente de nuevo.")



calculadora()