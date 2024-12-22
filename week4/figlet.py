from pyfiglet import Figlet
import sys
import random
figlet = Figlet()

def main():
    fonts = figlet.getFonts()
    random_font = figlet.getFonts()[random.randint(0, len(fonts))]
    option_list = ["-f", "--font"]

    if len(sys.argv) == 1:
        change_font(random_font)
    elif len(sys.argv) == 3 and sys.argv[1] in option_list and sys.argv[2] in fonts:
        change_font(sys.argv[2])
    else:
        sys.exit("Invalid usage")


def change_font(font_name):
    text = input("Input: ")
    figlet.setFont(font = font_name)
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
