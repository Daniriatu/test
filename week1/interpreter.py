def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)

    match y:
        case "+":
            print (x + z)
        case "-":
            print (x - z)
        case "*":
            print (x * z)
        case "/":
            if z != 0.0:
                print (x / z)
            else:
                print("0 can't be used for division")
        case _:
            print("Are you giving the correct expression?")


main()