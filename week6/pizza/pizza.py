import sys, csv
from tabulate import tabulate


def main():
    try:
        if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
            info_list = extract_info(sys.argv[1])
            header = info_list[0]
            table = info_list[1:]
            print(tabulate(table, header, tablefmt="grid"))
        elif len(sys.argv) < 2:
                sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
                sys.exit("Too many command-line arguments")
        elif not sys.argv[1].endswith(".csv"):
                sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")


def extract_info(file_name):
    content_list = []
    with open(file_name) as file:
        content = csv.reader(file)
        for row in content:
            content_list.append(row)
    return content_list


if __name__ == "__main__":
    main()
