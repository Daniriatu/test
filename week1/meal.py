def main():
    tiempo = input("What time is it? ")
    result = convert(tiempo)
    if 7 <= result <= 8:
        print("breakfast time")
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")
    else:
        print("Well, nothing to eat yet")


def convert(time):
    # 判断是am 还是 pm
    if time.endswith("p.m."):
        # 将12小时转换为24小时, 注意12:00 p.m.
        hours, minutes = time.strip(".pm").split(":")
        if hours != "12":
             return (float(hours) + 12.0) + float(minutes) / 60
        else:
            return float(hours) + float(minutes) / 60
    else:
        hours, minutes = time.strip(".am").split(":")
        return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()