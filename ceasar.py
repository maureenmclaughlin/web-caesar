def alphabet_position(letter):
    dict = {"a": 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6,
    "h" : 7, "i" : 8, "j" : 9, "k" : 10, "l" : 11, "m" : 12, "n" : 13, "o" : 14,
    "p" : 15, "q" : 16, "r" : 17, "s" : 18, "t" : 19, "u" : 20, "v" : 21,
    "w" : 22, "x" : 23, "y" : 24, "z" : 25}
    letter = letter.lower()
    return dict[letter]

def rotate_character(char, rot):
    d2 = { 0 : "a", 1 : "b", 2 : "c", 3 : "d", 4 : "e", 5 : "f", 6 : "g",
    7 : "h", 8 : "i", 9 : "j", 10 : "k", 11 : "l", 12 : "m", 13 : "n", 14 : "o",
    15 : "p", 16 : "q", 17 : "r", 18 : "s", 19 : "t", 20 : "u", 21 : "v",
    22 : "w", 23 : "x", 24 : "y", 25 :"z"}
    index = alphabet_position(char)
    newindex = (index + int(rot)) % 26
    newletter = str(d2.get(int(newindex)))
    if char.islower():
        newletter = newletter.lower()
    if char.isupper():
        newletter = newletter.upper()
    return newletter

def encrypt(text, rot):

    newLetter = ""
    word = ""

    for i in text:
        i = str(i)
        if i.isalpha():
            newLetter = rotate_character(i, rot)
        else:
            newLetter = i
        word = word + newLetter

    return word
