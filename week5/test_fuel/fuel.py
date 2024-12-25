def main():
    while True:
        try:
            usr_input = input("Fraction: ")
            percentage = convert(usr_input)
            if percentage:
                print(gauge(percentage))
                break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = fraction.split("/")
    if int(y) == 0:
        raise ZeroDivisionError
    elif int(x) > int(y):
        raise ValueError
    return round((int(x) / int(y)) * 100)


def gauge(percentage):
    if 99 <= percentage <= 100:
        return "F"
    elif 1 < percentage < 99:
        return f"{percentage}%"
    elif percentage <= 1:
        return "E"

if __name__ == "__main__":
    main()
