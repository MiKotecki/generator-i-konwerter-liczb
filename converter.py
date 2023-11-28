if __name__ == '__main__':

    with open("input.txt", "r") as input_file:
        raw_lines = input_file.readlines()


        numbers = []
        for line in raw_lines:
            numbers.append(int(line.strip()))

        print(numbers)





