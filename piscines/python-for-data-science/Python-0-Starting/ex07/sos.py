def encode_morse(s):
    assert isinstance(s, str), "Argument should be a string"

    morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                       'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                       'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                       'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                       'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
                       '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                       ', ': '--..--', '.': '.-.-.-', '?': '..--..',
                       '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-', ' ': '/'}

    morse_code = ''
    for char in s.upper():
        morse_code += morse_code_dict[char] + ' '

    return morse_code.strip()


if __name__ == "__main__":
    import sys
    assert len(sys.argv) == 2, "The number of arguments should be 1"
    print(encode_morse(sys.argv[1]))
