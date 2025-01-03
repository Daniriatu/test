import random


def main():
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    questions_num = 0
    chances = 3
    score = 0
    game_level , game_mode = get_level()

    while questions_num < 10:  
        if chances == 3:
            n1, n2 = generate_integer(game_level, game_mode)
        try:
            usr_answer = float(input(f"{n1} {game_mode} {n2} = "))
            operator = operators[game_mode]
            result = round(operator(n1, n2), 2)
            if not result == usr_answer:
                raise ValueError
            else:
                chances = 3
                score += 1
                questions_num += 1
        except ValueError:
            print("EEE")
            chances -= 1
            if chances == 0:
                print(f"{n1} {game_mode} {n2} = {result}")
                chances = 3
                questions_num += 1

    print(f"Score: {score}")

    
def get_level():
    level_list = [1, 2, 3]
    mode_list = ["+", "-", "*", "/"]
    while True:
        try:
            level = int(input("Level: "))
            mode = input("Mode(+, -, * or /): ")
            if level in level_list and mode in mode_list:
                return [level, mode]
            raise ValueError
        except ValueError:
            pass


def generate_integer(level, mode):
    if level == 1:
        num1 = random.randint(0, 9)
        if mode != "/":
            num2 = random.randint(0, 9)
        else:
            num2 = random.randint(1, 9)
    elif level == 2:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    elif level == 3:
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)         
    return [num1, num2]
    

    
if __name__ == "__main__":
    main()
    