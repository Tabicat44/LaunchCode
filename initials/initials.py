def get_initials(name):
    empty = name.split()
    new_string = ''
    for word in empty:
        new_string = new_string + word[0]
    return new_string.upper()

def main():
    initials = (input("What name would you like to test?"))
    print("The initials of the given name are:", get_initials(initials))

if __name__ == "__main__":
    main()
