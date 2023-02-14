def car_numbers(file_name: str):
    with open(file_name, 'r') as file:
        m = int(file.readline().strip())
        witness = [file.readline().strip() for _ in range(m)]
        n = int(file.readline().strip())
        numbers = [[file.readline().strip(), 0] for _ in range(n)]

    nowm = 0
    for numb in numbers:
        for prof in witness:
            if not (set(prof) - set(numb[0])):
                numb[1] += 1
        if numb[1] > nowm:
            nowm = numb[1]

    res = [x[0] for x in numbers if x[1] == nowm]
    print(*res, sep='\n')


car_numbers('input.txt')
