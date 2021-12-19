puzzle_input = open("test.txt", "r").read()

print(puzzle_input)

def hex_to_binary(hex_string):

    binary_string = ''

    for i in hex_string:
        if i == "0":
            binary_string += "0000"
        if i == "1":
            binary_string += "0001"
        if i == "2":
            binary_string += "0010"
        if i == "3":
            binary_string += "0011"
        if i == "4":
            binary_string += "0100"
        if i == "5":
            binary_string += "0101"
        if i == "6":
            binary_string += "0110"
        if i == "7":
            binary_string += "0111"
        if i == "8":
            binary_string += "1000"
        if i == "9":
            binary_string += "1001"
        if i == "A":
            binary_string += "1010"
        if i == "B":
            binary_string += "1011"
        if i == "C":
            binary_string += "1100"
        if i == "D":
            binary_string += "1101"
        if i == "E":
            binary_string += "1110"
        if i == "F":
            binary_string += "1111"

    return binary_string

binary_input = hex_to_binary(puzzle_input)

print(binary_input)

def decode_header(header):
    version = int(header[:3], 2)
    type_id = int(header[3:], 2)
    return type_id

def find_end_string(substring, length):
    # TODO
    pass

def evaluate_expression(substring):

    type_id = decode_header(substring[:6])

    result = []

    if type_id != 4:
        length_type_id = substring[6]

        if length_type_id == "1":
            number_sub_packets = int(substring[7:18], 2)
            # print(number_sub_packets)
            substring = substring[18:]
        else:
            length_sub_packets = int(substring[7:22], 2)
            # print(length_sub_packets)
            substring = substring[22:]

    if type_id == 4:

        i = 6
        while substring[i] != "0":
            i += 5
        i += 5

        temp = []
        temp.append(int(substring[6:i], 2)) # lit
        more_literals = evaluate_expression(substring[i:])
        if more_literals:
            for j in more_literals:
                temp.append(j)
        return temp

    if type_id == 0:
        temp = 0
        for i in evaluate_expression(substring):
            temp += i
        result.append(temp)
    if type_id == 1:
        temp = 1
        for i in evaluate_expression(substring):
            temp *= i
        result.append(temp)
    if type_id == 2:
        result.append(min(evaluate_expression(substring)))
    if type_id == 3:
        result.append(max(evaluate_expression(substring)))

    if type_id == 5:
        temp = evaluate_expression(substring)
        if temp[0] > temp[1]:
            result.append(1)
        else:
            result.append(0)
    if type_id == 6:
        temp = evaluate_expression(substring)
        if temp[0] < temp[1]:
            result.append(1)
        else:
            result.append(0)
    if type_id == 7:
        temp = evaluate_expression(substring)
        if temp[0] == temp[1]:
            result.append(1)
        else:
            result.append(0)

    return result

print(*evaluate_expression(binary_input))