test_cases = int(input())

while test_cases != 0:
    line = input().split()
    houses = []

    for i in line:
        amount_of_wine = int(i)
        houses.append(amount_of_wine)

    aux = 0
    work_units = 0
    for i in houses:
        aux += i
        work_units += abs(aux)

    print(work_units)

    test_cases = int(input())
