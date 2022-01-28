from optparse import Values


def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "David", "lastname": "Almeida"}

    super_list = [
        {"firstname": "David", "lastname": "García"},
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "García"},
        {"firstname": "Pepe", "lastname": "García"},
        {"firstname": "José", "lastname": "García"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    print("---------------------------") 

    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')


if __name__ == '__main__':
    run()