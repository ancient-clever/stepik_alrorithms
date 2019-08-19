def huffman(n):
    letters = {}
    for letter in n:
        if letter not in letters:
            letters[letter] = n.count(letter)
    print(letters)


def main():
    n = input()
    print(huffman(n))


if __name__ == "__main__":
    main()
