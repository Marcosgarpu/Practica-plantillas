from calculadora import Calculadora


def mostrar_menu():
    print()
    print("=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Resto")
    print("6. Salir")


def main():
    calc = Calculadora()
    opcion = 0

    while opcion != 5:
        mostrar_menu()
        opcion = int(input("Elige una opción: "))

        if opcion >= 1 and opcion <= 4:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))

            if opcion == 1:
                resultado = calc.sumar(a, b)
            elif opcion == 2:
                resultado = calc.restar(a, b)
            elif opcion == 3:
                resultado = calc.multiplicar(a, b)
            elif opcion == 5: 
                resultado == calc.resto(a,b)
            else:
                resultado = calc.dividir(a, b)

            print("Resultado:", resultado)
        elif opcion != 5:
            print("Opción no válida")

    print("Hasta pronto")


main()