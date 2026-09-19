from pathlib import Path

LOWER = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

UPPER = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

SPECIAL = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
    "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'",
    "\"", ",", ".", "<", ">", "?", "/", "\\", "`", "~"
]


def word_in_file(word, filename, case_sensitive):
    """Return True if word appears on a line in the file."""
    target = word if case_sensitive else word.lower()

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            text = line.strip()
            if not case_sensitive:
                text = text.lower()
            if text == target:
                return True
    return False


def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False


def word_complexity(word):
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


def password_strength(password, min_length, strong_length):
    """Return the password strength category."""
    if len(password) < min_length:
        return "weak"

    if len(password) >= strong_length and word_complexity(password) == 4:
        return "strong"

    if word_complexity(password) >= 3:
        return "moderate"

    return "weak"


def main():
    password = input("Enter a password: ")
    common_file = Path(__file__).resolve().parent / "toppasswords.txt"

    if word_in_file(password, str(common_file), False):
        print("That password is too common. Please choose another one.")
        return

    complexity = word_complexity(password)
    strength = password_strength(password, 8, 12)

    print(f"Your password complexity is: {complexity}")
    print(f"Your password strength is: {strength}")


if __name__ == "__main__":
    main()