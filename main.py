df = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter:row.code for (index, row) in df.iterrows()}
converting = True
while converting:
    user_word = input("Enter a word: ").upper()
    if user_word.isalpha():
        new_word = [alpha_dict[letter] for letter in user_word]
        print(new_word)
    else:
        print("Invalid input.")
        continue
