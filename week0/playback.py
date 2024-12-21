def main():
    message = input("Speak as fast as you want (you'll be slowed down anyway): ")
    message = message.replace(" ", "...")
    print(message)


main()