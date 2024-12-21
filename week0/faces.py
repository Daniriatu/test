def main():
    message = input("Say something with :) or :( to me. ")
    message = convert(message)
    print(message)


def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")


main()