def main():
    n = int(input())
    d1 = str(input())
    d2 = str(input())
    same = 0

    for i in range(n):
        if d1[i] == 'C' and d2[i] == 'C':
            same += 1
    print(same)


if __name__ == '__main__':
    main()
 
