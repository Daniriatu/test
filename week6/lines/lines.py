import sys

def main():
    try:
        if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
            print(count_lines(sys.argv[1]))
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
    except FileNotFoundError:
        sys.exit("File does not exist")


def count_lines(file_name):
    line_count = 0
    with open(file_name) as file:
        for line in file:
            if not line.lstrip().startswith("#") and not line.isspace():
                line_count += 1
    return line_count


if __name__ == "__main__":
    main()
