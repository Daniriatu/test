def main():
    camel = input("camelCase: ")
    convert_snake_case(camel)


def convert_snake_case(usr_input):
    usr_input = usr_input.strip()
    for char in usr_input:
        if char.isupper():
            char = f"_{char.lower()}"
        print(char, end="")
    print("")


main()
