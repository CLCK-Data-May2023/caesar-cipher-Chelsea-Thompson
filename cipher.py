# add your code here
dict_calpha = {
    "a": "f",
    "b": "g",
    "c": "h",
    "d": "i",
    "e": "j",
    "f": "k",
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r",
    "n": "s",
    "o": "t",
    "p": "u",
    "q": "v",
    "r": "w",
    "s": "x",
    "t": "y",
    "u": "z",
    "v": "a",
    "w": "b",
    "x": "c",
    "y": "d",
    "z": "e"
}

sentence = input("Please enter a sentence: ") 
sentence = sentence.lower()

encrypted_sentence = ""
for letter in sentence:
    if letter in dict_calpha:
        encrypted_sentence += dict_calpha[letter]
    else: 
        encrypted_sentence += letter
print("The encrypted sentence is:", encrypted_sentence)