from plates import is_valid


# “All vanity plates must start with at least two letters.”
def test_two_letters_check():
    assert is_valid("HI") == True
    assert is_valid("96") == False
    assert is_valid("H9") == False


# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def test_plate_length():
    assert is_valid("H") == False
    assert is_valid("CS50") == True
    assert is_valid("HITHERE") == False

# “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
def test_combination():
    assert is_valid("CS50P") == False
    assert is_valid("DANI96") == True
    assert is_valid("DANI09") == False


# “No periods, spaces, or punctuation marks are allowed.”
def test_punct():
    assert is_valid("LOVEU!") == False
