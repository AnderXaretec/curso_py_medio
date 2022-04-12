def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    # return "Tu numero tiene: ", len(divisors), """divisores y son los siguientes
    # """, divisors
    return len(divisors), divisors

def run():
    # for i in range(1, 100):
    num = input("Ingresa un numero: ")
    assert num.isnumeric(), "Solo puedes ingresar numeros"
        # assert num != abs(int(num)), "No puedes ingresar numeros negativos"
    list_1 = divisors(int(num))
    print("Tu numero tiene ", list_1[0], """ divisores y son los siguientes:
    """, list_1[1])
    print("Programa terminado")
        # break

        

if __name__ == "__main__":
    run()