def main():
    word = "answer"
    numbers = [0, 0, 0, 0]
    for i in range(4):
        number = int(input())
        numbers[i] = number
    if((numbers[0] == 9 or numbers[0] == 8) and (numbers[1] == numbers[2]) and (numbers[3] == 9 or numbers[3] == 8)):
        word = "ignore"
    print(word)


if __name__ == '__main__':
    main()
