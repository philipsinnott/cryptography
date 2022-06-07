from shift_cipher import ShiftCipher
def main():
    SHIFT = ShiftCipher()
    # print(SHIFT.alphabet_pos("khan"))
    print(SHIFT.encrypt("khan"))

    # print(SHIFT.alphabet_to_numerical("khan"))
    # SHIFT.numerical_to_alphabet([10, 7, 0, 13])

if __name__ == "__main__":
    main()