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


