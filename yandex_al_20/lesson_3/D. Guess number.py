def guess_numbers(file_name: str):
    with open(file_name, 'r') as file:
        n = int(file.readline().strip())
        all_set = set(range(1, n + 1))

        while True:
            ans_b = file.readline().strip()
            if ans_b == 'HELP':
                break
            guess_set = set(map(int, ans_b.split()))
            ans_a = file.readline().strip()
            if ans_a == 'YES':
                all_set &= guess_set
            else:
                all_set -= guess_set

    print(' '.join(map(str, sorted(all_set))))


guess_numbers('input.txt')
