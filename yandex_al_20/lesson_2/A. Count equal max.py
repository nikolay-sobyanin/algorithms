def count_max(file_name: str) -> int:
    with open(file_name, 'r') as file:
        now_max = int(file.readline().strip())
        i = 1

        for line in file:
            crrn_n = int(line.strip())
            if crrn_n == 0:
                return i
            if crrn_n > now_max:
                now_max = crrn_n
                i = 1
            elif crrn_n == now_max:
                i += 1


with open('output.txt', 'w') as file:
    file.write(str(count_max('input.txt')))
