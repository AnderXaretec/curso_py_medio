def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

def run():
    for i in range(1, 100):
        try:
            num =  int(input("Ingresa un numero: "))
            try:
                if num != abs(num):
                    raise ValueError ("No puedes ingresar numeros negativos")
                print(divisors(num))
                print("Programa terminado")
                break
            except ValueError as ve:
                print(ve)
        except ValueError:
            print("Solo puedes ingresar numeros")

if __name__ == "__main__":
    run()