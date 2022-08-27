# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

alphabet_dataframe = pandas.read_csv("./nato_phonetic_alphabet.csv")
# print(alphabet_dataframe)


#1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

alphabet_dic = {row.letter: row.code for (index, row) in alphabet_dataframe.iterrows()}
#print(alphabet_dic)

#2. Create a list of the phonetic code words from a word that the user inputs.

userinput = input("Insert a word to convert: ").upper()
converted_list = [alphabet_dic[char] for char in userinput]
print(converted_list)