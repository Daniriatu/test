import sys, csv


def main():
    try:
        if len(sys.argv) == 3 and sys.argv[1].endswith(".csv"):
            convert_content(sys.argv[1], sys.argv[2])
        elif len(sys.argv) < 3:
                sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
                sys.exit("Too many command-line arguments")
        elif not sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
                sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")


def convert_content(file_before, file_after):
    content_list = []
    with open(file_before) as old_file:
        reader = csv.DictReader(old_file)
        for row in reader:
            last, first = row["name"].split(",")
            house = row["house"]
            content_dict = {
                "first": first.strip(),
                "last": last.strip(),
                "house": house.strip()
            }
            content_list.append(content_dict)

    with open(file_after, "w") as new_file:
        filed_names = ["first", "last", "house"]
        writer = csv.DictWriter(new_file, fieldnames=filed_names)
        writer.writeheader()
        for content in content_list:
            writer.writerow(content)


if __name__ == "__main__":
    main()
