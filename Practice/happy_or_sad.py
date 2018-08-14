def main():
    characters = input()
    if ':-)' not in characters and ':-(' not in characters:
        print("none")
    elif characters.count(':-)') == characters.count(':-('):
        print("unsure")
    elif characters.count(':-)') > characters.count(':-('):
        print("happy")
    else:
        print("sad")


if __name__ == '__main__':
    main()
