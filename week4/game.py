# import random

# while True:
#     try:
#         level = int(input("Level: "))
#         if level > 0:
#             answer = random.randint(1, level)
#             while True:
#                 try:
#                     usr_input = int(input("Guess: "))
#                     if usr_input >= 0:
#                         if usr_input > answer:
#                             print("Too large!")
#                         elif usr_input < answer:
#                             print("Too small")
#                         else:
#                             print("Just right!")
#                             break
#                 except ValueError:
#                     pass
#             break
#     except ValueError:
#         pass

import random


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                answer = random.randint(1, level)
                guess(answer)
                break
        except ValueError:
            pass


def guess(num):
    while True:
        try:
            usr_input = int(input("Guess: "))
            if usr_input >= 0:
                if usr_input > num:
                    print("Too large!")
                elif usr_input < num:
                    print("Too small!")
                else:
                    print("Just right!")
                    break
        except ValueError:
            pass


if __name__ == "__main__":
    main()