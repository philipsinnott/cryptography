from string import ascii_lowercase as ALPHABET
LETTERS = {letter: index for index, letter in enumerate(ALPHABET)}

class ShiftCipher:

    def alphabet_pos(self, message):
        message = message.lower()

        numbers = [LETTERS[character] for character in message if character in LETTERS]
        return numbers

    def encrypt(self, message):
        pass

    def decrypt(self, message):
        pass
