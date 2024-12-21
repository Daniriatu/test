def main():
    fuel_gauges_indicator("Fraction: ")


def fuel_gauges_indicator(prompt):
    while True:
        try:
            fraction = input(prompt)
            x, y = fraction.split("/")
            result = (int(x) / int(y)) * 100
            if 99 <= result <= 100:
                print("F")
                break
            elif 1 < result < 99:
                print(f"{round(result)}%")
                break
            elif result <= 1:
                print("E")
                break
        except ValueError:
            print("You didn't give the correct number")
        except ZeroDivisionError:
            print("No number can be divided by 0")


main()