# Permutations
# 	Write a solution that will print all permutations of a string.
# A permutation is an act of changing the arrangement of characters.
# Example: String = ABC, Return {ABC, ACB, BAC, BCA, CBA, CAB}

# Initialising string
ini_str = "ABC"

# Printing initial string
print("Initial string", ini_str)

# Finding all permutation
result = []


def permute(data, i, length):
    if i == length:
        result.append(''.join(data))
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]


permute(list(ini_str), 0, len(ini_str))

# Printing result
print("Resultant permutations", str(result))