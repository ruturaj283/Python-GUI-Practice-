import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# for (index,row) in data.iterrows():
#     print(index,row)

phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

word = input("Enter your word:").upper()

phonatic_list = [phonetic_dict[x] for x in word]

print(phonatic_list)
