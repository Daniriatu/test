def main():
    usr_input = input("Input: ")
    result = shorten(usr_input)
    print(result)


def shorten(word):
    vowels_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    word = word.strip().lower()
    for char in word:
       if char in vowels_list:
           word = word.replace(char, "")
    return word


if __name__ == "__main__":
    main()