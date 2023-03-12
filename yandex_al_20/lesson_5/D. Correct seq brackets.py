s = input().strip()


def check_correct_bracket_sequence(seq: str) -> bool:
    prefix_sum = [0] * (len(seq) + 1)
    for i in range(1, len(prefix_sum)):
        if seq[i - 1] == '(':
            prefix_sum[i] = prefix_sum[i - 1] + 1
        else:
            prefix_sum[i] = prefix_sum[i - 1] - 1

        if prefix_sum[i] < 0:
            return False

    if prefix_sum[-1] != 0:
        return False

    return True


print('YES' if check_correct_bracket_sequence(s) else 'NO')
