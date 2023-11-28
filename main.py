if __name__ == '__main__':
    print("Generator liczb calkowitych")
    min_value = int(input("Wprowadz wartosc minimalna: "))
    max_value = int(input("Wprowadz wartosc maksymalna: "))
    step = int(input("Wprowadz krok: "))
    values = []
    current = min_value

    while current <= max_value:
        values.append(current)
        current += step

    # print(values)
    with open("input.txt", "w") as file:
        for value in values:
            file.write(f"{value}\n")
        # file.write(str(value))
        # file.write("\n")




