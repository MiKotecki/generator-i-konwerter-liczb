def dec_to_bin(value):
    return value

if __name__ == '__main__':

    with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
        raw_lines = input_file.readlines()
        numbers = []
        for line in raw_lines:
            numbers.append(int(line.strip()))

        print(numbers)
        for number in numbers:
            output_file.write(f"{dec_to_bin(number)})





