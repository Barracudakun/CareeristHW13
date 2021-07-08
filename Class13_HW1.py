#1. Reverse a Statement
# Build an algorithm that will print the given statement in reverse.
# Example: Initial string = Everything is hard before it is easy
# Reversed string = easy is it before hard is Everything

def rev_sentence(sentence):
    # first split the string into words
    words = sentence.split(' ')

    # then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))

    # finally return the joined string
    return reverse_sentence


if __name__ == "__main__":
    input = 'everything is hard before it is easy'
    print(rev_sentence(input))


#2. Permutations
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

# 3.Count Characters
# Create a program that will count vowels and consonants in a string.
# Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}

#define all vowels in a list
vowels = ['a', 'e', 'i', 'o', 'u']

#input a string and transform it to lower case
str = input("Enter a string: ").lower()

#define counter variable for both vowels and consonants
v_ctr = 0
c_ctr = 0

#iterate through the characters of the input string
for x in str:
    #if character is in the vowel list,
    #update the vowel counter otherwise update consonant counter
    if x in vowels:
        v_ctr += 1
    else:
        c_ctr += 1

#output the values of the counters
print("Vowels: ", v_ctr)
print("Consonants: ", c_ctr)