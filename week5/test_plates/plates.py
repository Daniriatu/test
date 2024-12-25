def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    flag = False
    # 检查string长度, 是否含有特殊符号
    if 2 <= len(s) <= 6 and s.isalnum():
        # plates全是字母的情况
        if s.isalpha():
            flag = True
        # 如果plates存在数字，必须至少以两个字母开头，并以数字结尾
        elif s[0:2].isalpha():
            for i in range(len(s)):
                if s[i].isdigit():
                    # 如果数字以0开头，立刻返回False，如果后续字符不全是数字字符，也返回False
                    if s[i:].startswith("0") or not s[i:].isdigit():
                        return flag
                    else:
                        flag = True
    return flag

if __name__ == "__main__":
    main()
