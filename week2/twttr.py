def main():
    usr_input = input("Input: ")
    omit_vowels(usr_input)


def omit_vowels(content):
    vowels_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    content = content.strip()
    for char in content:
       for vowel in vowels_list:
           if char == vowel:
               char = ""
       print(char, end="")
    print()


main()