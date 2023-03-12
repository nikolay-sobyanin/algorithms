def elections(file_name):
    candidates = {}
    with open(file_name, 'r') as file:
        for line in file.readlines():
            name, votes = line.strip().split()
            if name not in candidates.keys():
                candidates[name] = 0
            candidates[name] += int(votes)

    for key in sorted(candidates):
        print(key, candidates[key])


elections('input.txt')
