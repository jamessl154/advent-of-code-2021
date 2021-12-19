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

# Help from: https://topaz.github.io/paste/#XQAAAQCJBwAAAAAAAAA0m0pnuFI8c/fBNAn8jP/zLliB/yhToWUPCpV3XwLoiWO/Iydt72UAi6NORl6kmkUlbT/LGStT2k/xurbI9AfeQZFahn1+QSXxWA0MO1ejOTDhxVVdHYLPZ+k4weVvhxtL9ho8hx2+Swc78M1yqPwrbDFeUwTyK1cAgVny/p9R9GStEIQ1lSvWdS1wnK6px2oKVcWYhQNT68aFVg5QkkuVgxOYSuF9hYwofJ64oRefQ9p3Y0pRgxtNsUd7nUAi7s5Z7xtSCQqAi5WvFUd1xiDaq+htmFcr/O+gFoU9Z0+VKHZP6Zp6uxwrm9eEwBY4a1sMQyaf5eH7yIe6Otkbqvya1P/rLWML5vz0VG7pCFFfQ3uwBmH4BwjzYcjmRzpu946xUpHiQZBrkd6riMt12l6Sb+F1FkMBE7T+/gJdzdXtAnyJA30EDtlfTAB3VII6qovoGnBnHfbccGH98Fr2aHvK/gAThnW3qc3JZb+a6/eMv9wfKnVwXx4iAuMrRcgVPHOFcx284lAV9B2MT1EDchcT11DqhDAZxfy8qjI0dLvqG8W02A6qGsh/wapdErcQ9xdaALvISpL4io3Bn/HDL4pQhEzCPZjT1wcghYfAJ5zCQqEq3bxzBHotB/oVfHGc2ciycOBD7csjsKV3apeZrF5ZIJlGaP4+A5QYJzi1RTmuy0Fo+YJ+1mPdh0/zLM0rLhpoNrJP21AmdpAV0YJBzULjlRlj3yvi1e7Gn7n9nOyhfQUG4PfHE0YfjC+MCiq/bOgJRVKbZEgrrEIM/6WqxHYOSan62prIVAkg+6as0uwKuzAQ/+wXGf4s2PY=
def parse_packet(data):

    type_id = int(data[3:6], 2)

    data = data[6:]

    result = []

    if type_id != 4:
        length_type_id = data[0]
        data = data[1:]

        if length_type_id == "1":
            num_subpackets = int(data[:11], 2)
            data = data[11:]
            # Similar to len_subpackets by recursively calling with a shrinking subpacket
            # but we can just stop once found correct num of evaluated subpackets
            for i in range(num_subpackets):
                s, x = parse_packet(data)
                data = s
                result.append(x)
        else:
            len_subpackets = int(data[:15], 2)
            data = data[15:]
            subpackets = data[:len_subpackets]
            data = data[len_subpackets:]
            # Recursively calling this function with a shrinking subpacket
            # until the subpacket is ''
            while subpackets:
                s, x = parse_packet(subpackets)
                subpackets = s
                result.append(x)

    if type_id == 4:

        lit_string = ''

        while True:
            lit_string += data[1:5]
            prefix = data[0]
            data = data[5:]
            if prefix == '0':
                break

        return (data, int(lit_string, 2))

    if type_id == 0:
        return (data, sum(result))

    if type_id == 1:
        prod = 1
        for i in result:
            prod *= i
        return (data, prod)

    if type_id == 2:
        return (data, min(result))

    if type_id == 3:
        return (data, max(result))

    if type_id == 5:
        return (data, 1 if result[0] > result[1] else 0)

    if type_id == 6:
        return (data, 1 if result[0] < result[1] else 0)

    if type_id == 7:
        return (data, 1 if result[0] == result[1] else 0)

print(parse_packet(binary_input)[1])