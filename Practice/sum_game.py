def main():
    n = int(input())  # number of days
    swifts = input()
    semaphores = input()
    swifts_total = 0
    semaphores_total = 0
    k = 0
    days = 0

    for i in range(0, n+3, 2):
        days += 1
        swifts_total += int(swifts[i])
        # print('swifts:' + str(swifts_total))
        semaphores_total += int(semaphores[i])
        # print('semaphores:' + str(semaphores_total))
        # print('days:' + str(days))
        if swifts_total == semaphores_total:
            k = days
    print(k)


if __name__ == '__main__':
    main()
