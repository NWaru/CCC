def main():
    n = int(input())
    answer = 1
    if n >= 5:
        left_hand = n - 5
        right_hand = 5
    else:
        left_hand = 0
        right_hand = n
    while(left_hand < right_hand):
        right_hand -= 1
        left_hand += 1
        if left_hand < 6 and right_hand < 6 and left_hand <= right_hand:
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()
