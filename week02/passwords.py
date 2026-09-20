
LOWER = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i","j", "k", "l","m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]

UPPER = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]

DIGITS = ["0","1","2","3","4","5","6","7","8","9"]

SPECIAL = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
    "-", "_","=", "+","[", "]", "{", "}", "|", ";", ":", "'",
    "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"
    ]

def word_in_file(word, filename, case_sensitive):
    """
    Search a file for a word and return True if found,
    otherwise return False.
    """
    if not case_sensitive:
        word = word.lower()

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not case_sensitive:
                line = line.lower()
            if line == word:
                return True
    return False
 
def word_has_character(word, character_list):
    """
    Return True if word contains a character 
    from character_list. Otherwise return False.
    """
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    """
    Calculate and return the complexity score
    for a word based on character types used.
    """
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    """
    Determine and return the strength of
    a password from 0 to 5.
    """
    if word_in_file(password, "wordlist.txt", False):
        print("Password is a dictionary word and is not secure.")
        return 0
    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    return word_complexity(password) + 1

def main():
    """
    Prompt the user for passwords and display
    password strength information.
    """
    new_password = input("\nPlease input your password: ")
    while new_password not in ["q", "Q"]:
        strength = password_strength(new_password)
        print(f"\nPassword strength: {strength}\n")
        new_password = input("\nPlease input your password:")

if __name__ == "__main__":
    main()