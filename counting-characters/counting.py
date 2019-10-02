import string

def figure_it_out(sentence):
    alphy = string.ascii_letters

    letter_counter = {}
    for character in given_sentence:
        if character in alphy:
            if character in letter_counter:
                letter_counter[character] = letter_counter[character] + 1
            else:
                letter_counter = 1

    keys = letter_counter.keys()
    keys.sort()
    for character in keys:
        print(character, letter_counter[character])

def main():
    given_sentence = input("What would you like to say?")
    figure_it_out(given_sentence)

if __name__ == "__main__":
    main()