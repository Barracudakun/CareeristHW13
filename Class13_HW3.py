# Count Characters
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