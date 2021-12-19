puzzle_input = open("input.txt", "r").read()

# print(puzzle_input)

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

# print(binary_input)

def decode_header(header):
    version = int(header[:3], 2)
    type_id = int(header[3:], 2)

    # print(header[:3], header[3:], version, type_id )

    return (version, type_id)

i = 0

version_counter = 0

while i < len(binary_input) - 6:

    version, type_id = decode_header(binary_input[i:i + 6])

    version_counter += version

    i += 6

    if type_id != 4:

        if binary_input[i] == "1":
            i += 12
        elif binary_input[i] == "0":
            i += 16
    
    elif type_id == 4:

        while binary_input[i] == "1":
            i += 5
        i += 5

print(version_counter)