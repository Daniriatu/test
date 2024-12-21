def main():
    grocery_dict = {}
    while True:
        try:
            food = input()
            food = food.strip().upper()
            if food in grocery_dict:
                grocery_dict[food] = grocery_dict[food] + 1
            else:
                grocery_dict[food] = 1
        except EOFError:
            print("\n")
            grocery_list = sorted(grocery_dict)
            for grocery in grocery_list:
                print(f"{grocery_dict[grocery]} {grocery}")
            break
        except KeyError:
            pass


main()
