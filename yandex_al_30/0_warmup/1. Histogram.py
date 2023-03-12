def count_symbols(file_name: str) -> list:
    collect_smb = dict()
    with open(file_name, 'r') as file:
        for line in file.readlines():
            for smb in line:
                if smb == ' ' or smb == '\n':
                    # miss this symbols
                    continue
                if smb in collect_smb:
                    collect_smb[smb] += 1
                else:
                    collect_smb[smb] = 1
    return sorted(collect_smb.items())


def print_histogram(data: list) -> None:
    height = max([x[1] for x in data])
    result = []
    for smb, count in data:
        result.append([smb] + ['#'] * count + [' '] * (height - count))

    trans_result = list(zip(*result))
    for line in trans_result[::-1]:
        print(''.join(line))


print_histogram(count_symbols('input.txt'))
