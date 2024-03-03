def caesar(offset, input_str):
    result = ""

    for char in input_str:
        if char.isalpha():
            # Determine the case (uppercase or lowercase)
            is_upper = char.isupper()
            char_code = ord(char.lower())

            # Shift the character by the offset
            shifted_char_code = (char_code - ord('a') + offset) % 26 + ord('a')

            # Convert the character code back to the original case
            shifted_char = chr(shifted_char_code).upper() if is_upper else chr(shifted_char_code)

            result += shifted_char
        else:
            result += char

    return result

if __name__ == '__main__':
    # Test cases
    print(caesar(3, "abc"))                    # Output: def
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz"))  # Output: bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # Output: mnopqrstuvwxyzabcdefghijkl
