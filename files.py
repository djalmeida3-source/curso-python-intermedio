def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["David", "José", "Cristian", "Valeria", "Rocío"]
    with open("/home/david/projects/python/curso-python/files/names.txt","a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    # read()
    write()


if __name__ == '__main__':
    run()