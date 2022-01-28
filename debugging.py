def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input("Ingresa un número: "))
        if num < 0:
            raise ValueError ("Debes ingresar un número positivo")
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError as ve:
        if 'num' not in locals():
            print("Debes ingresar un nùmero")
        else:
            print(ve)

if __name__ == '__main__':
    run()