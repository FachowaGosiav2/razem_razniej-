import sys

no_of_tries = 5
word = "kamila"

used_letters = []

user_word = []

def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes

def status():
    print("".join(user_word))
    print()
    print("Pozostało", no_of_tries, "prób.")
    print("Użyte litery:", used_letters)
    print()
    

for _ in word:
    user_word.append("_")

while True:
    letter = input("Podaj literę: ")  
    used_letters.append(letter)
    used_letters.sort()

    found_indexes = find_indexes(word, letter)
    # print(found_indexes, "test")

    if len(found_indexes) == 0:
        no_of_tries -= 1
        if no_of_tries == 0:
            print()
            print("Wykorzystano wszystkie próby. Koniec gry :(")
            print()
            sys.exit(0)
        print()
        print("Nie ma takiej litery.")
        print()
    
    else:
        # print("".join(user_word))
        for index in found_indexes:
            user_word[index] = letter
        

    if "".join(user_word) == word:
        print("Udało Ci się! Poszukiwane słowo to", word) 
        sys.exit(0)



    status()
