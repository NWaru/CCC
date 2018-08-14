def main():
    cities = '0 ' + str(input())
    city_list = cities.split(' ')

    for i in range(len(city_list)):
        for n in range(len(city_list)):
            distance = 0
            k = i
            if k < n:
                k += 1
                while True:
                    distance += int(city_list[k])
                    k += 1
                    if k > n:
                        if n == 4:
                            print(distance)
                        else:
                            print(distance, end=' ')
                        break
            elif k > n:
                while True:
                    distance += int(city_list[k])
                    k -= 1
                    if k == n:
                        if n == 4:
                            print(distance)
                        else:
                            print(distance, end=' ')
                        break
            else:
                distance = 0
                if n == 4:
                    print(distance)
                else:
                    print(distance, end=' ')


if __name__ == '__main__':
    main()
