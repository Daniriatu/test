from datetime import date, timedelta
import sys
import inflect


def main():
    try:
        today = date.today()
        usr_input = input("Date of Birth: ")
        date_of_birth = date.fromisoformat(usr_input)
        days = abs(today - date_of_birth)
        print(convertor(days.days))
    except ValueError:
        sys.exit()
    
    
def convertor(time):
    p = inflect.engine()
    minutes = time * 24 * 60
    minutes_str = p.number_to_words(minutes, andword="")
    return f"{minutes_str} minutes"
    

if __name__ == "__main__":
    main()