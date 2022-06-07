from string import ascii_lowercase as ALPHABET
KEY = 19

class ShiftCipher:

    def alphabet_to_numerical(self, message):
        numerical = []
        for character in message:
            numerical.append(ALPHABET.find(character))
        return numerical

    def numerical_to_alphabet(self, message):
        alphabet = []
        for letter in message:
            alphabet.append(chr(97 + letter))
        return alphabet

    def encrypt(self, message):
        message = self.alphabet_to_numerical(list(message))
        reverse = []
        for character in message:
            y = (character + KEY) % 26
            reverse.append(y)

        str_result = ""
        reverse = self.numerical_to_alphabet(reverse)
        return str_result.join(reverse)

    def decrypt(self, cipher_text):
        cipher_text = self.alphabet_to_numerical(cipher_text)
        reverse = []
        for letter in cipher_text:
            x = (letter - KEY) % 26
            reverse.append(x)

        str_result = ""
        reverse = self.numerical_to_alphabet(reverse)
        return str_result.join(reverse)
