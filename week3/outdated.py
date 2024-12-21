def main():
    convert_date("Date: ")


def convert_date(message):
    month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        try:
            date = input(message).strip()
            if "," in date:
                month_day, year = date.split(",")
                month, day = month_day.split(" ")
                month = month.capitalize()
                if month in month_list:
                    month = month_list.index(month) + 1
            elif "/" in date:
                month, day, year = date.split("/")

            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                print(f"{int(year)}-{int(month):02}-{int(day):02}")
                break
        except (ValueError, UnboundLocalError):
            pass


if __name__ == "__main__":
    main()
