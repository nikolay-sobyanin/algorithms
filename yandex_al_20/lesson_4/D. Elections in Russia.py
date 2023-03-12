def rus_elections(file_name):
    plt_prt = {}
    v_sum = 0
    pos = 1
    with open(file_name, 'r') as file:
        for line in file.readlines():
            tmp = line.strip().split()
            name, votes = ' '.join(tmp[:-1]), int(tmp[-1])
            plt_prt[name] = {'p': pos, 'v': votes}
            pos += 1
            v_sum += votes

    d = v_sum / 450
    v_sum_crr = 0

    for key in plt_prt.keys():
        tmp = plt_prt[key]['v'] / d
        plt_prt[key]['s'] = int(tmp)
        plt_prt[key]['r'] = tmp % 1
        v_sum_crr += int(tmp)

    if v_sum_crr < 450:
        v_r = 450 - v_sum_crr
        s_key = sorted(plt_prt.keys(), key=lambda x: (-plt_prt[x]['r'], plt_prt[x]['v']))
        for i in range(v_r):
            plt_prt[s_key[i]]['s'] += 1

    for prt in sorted(plt_prt.keys(), key=lambda x: plt_prt[x]['p']):
        print(prt, plt_prt[prt]['s'])


rus_elections('input.txt')
