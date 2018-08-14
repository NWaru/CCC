def main():
    word = input()
    letter_list = []
    vowels = (ord('a'), ord('e'), ord('i'), ord('o'), ord('u'))
    nearest = 0
    after = 0
    spraken = ''

    for letter in word:
        letter_list.append(letter)
    for char in range(len(letter_list)):
        if (ord(letter_list[char]) not in vowels):
            if (abs(ord(letter_list[char]) - vowels[0]) < abs(ord(letter_list[char]) - vowels[1]) or
                    abs(ord(letter_list[char]) - vowels[0]) == abs(ord(letter_list[char]) - vowels[1])):
                nearest = vowels[0]
            else:
                nearest = vowels[1]
            if (abs(ord(letter_list[char]) - nearest) < abs(ord(letter_list[char]) - vowels[2]) or
                    abs(ord(letter_list[char]) - nearest) == abs(ord(letter_list[char]) - vowels[2])):
                pass
            else:
                nearest = vowels[2]
            if (abs(ord(letter_list[char]) - nearest) < abs(ord(letter_list[char]) - vowels[3]) or
                    abs(ord(letter_list[char]) - nearest) == abs(ord(letter_list[char]) - vowels[3])):
                pass
            else:
                nearest = vowels[3]
            if (abs(ord(letter_list[char]) - nearest) < abs(ord(letter_list[char]) - vowels[4]) or
                    abs(ord(letter_list[char]) - nearest) == abs(ord(letter_list[char]) - vowels[4])):
                pass
            else:
                nearest = vowels[4]

            if (ord(letter_list[char])+1 in vowels):
                after = ord(letter_list[char]) + 2
            elif (letter_list[char] == 'z'):
                after = ord(letter_list[char])
            else:
                after = ord(letter_list[char]) + 1
            letter_list[char] += chr(int(nearest))
            letter_list[char] += chr(after)

    for element in letter_list:
        spraken += element
    print(spraken)


if __name__ == '__main__':
    main()
