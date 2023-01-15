while True:
    try:
        line = input().split()
        people = int(line[0]) #n
        groups = int(line[1]) #k

        line = input().split()
        queue_ru = list(map(int, line[0:]))
        queue_ru.insert(0, 0)

        distances_ru = []
        distances_ru.append(0)
        for i in range(1, len(queue_ru)):
            distances_ru.append(queue_ru[i] - queue_ru[i-1])

        distances_ru.sort(reverse=True)

        min_sum = 0
        for i in range(groups-1, people):
            min_sum += distances_ru[i]
        print(min_sum)

    except EOFError:
        break