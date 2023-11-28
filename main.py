if __name__ == '__main__':
    max_value = 10
    min_value = 2
    step = 3
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




