import random


def main():
    questions_num = 0
    chances = 3
    score = 0
    game_level = get_level()

    while questions_num < 3:  
        if chances == 3:
            x, y = generate_integer(game_level)
        try:
            usr_answer = int(input(f"{x} + {y} = "))
            if not usr_answer == (x + y):
                raise ValueError
            else:
                score += 1
                questions_num += 1
        except ValueError:
            print("EEE")
            chances -= 1
            if chances == 0:
                print(f"{x} + {y} = {x + y}")
                chances = 3
                questions_num += 1

    print(f"Score: {score}")

    
def get_level():
    level_list = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            if level in level_list:
                return level
            raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    elif level == 2:
        num1 = random.randint(10, 99)
        num2 = random.randint(10,99)
    elif level == 3:
        num1 = random.randint(100, 999)
        num2 = random.randint(100,999)           
    return [num1, num2]


if __name__ == "__main__":
    main()
    