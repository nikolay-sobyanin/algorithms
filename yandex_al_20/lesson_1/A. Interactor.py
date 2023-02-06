# Links: https://contest.yandex.ru/contest/28730/problems/

def read_input(file_name='input.txt') -> list or None:
    """
    Read input file

    :param file_name: file name
    :return: list of params [r, i, c]
    """
    results = []
    with open(file_name, 'r') as file:
        for line in file:
            try:
                results.append(int(line.strip()))
            except ValueError:
                return None
    return results


def interactor(r: int, i: int, c: int) -> int:
    """
    Count final verdict

    :param r: Task completion code
    :param i: interactor's verdict
    :param c: Checker's Verdict
    :return: final verdict
    """

    if i == 0:
        return 3 if r != 0 else c
    elif i == 1:
        return c
    elif i == 4:
        return 3 if r != 0 else 4
    elif i == 6:
        return 0
    elif i == 7:
        return 1
    else:
        return i


def main():
    params = read_input('input.txt')
    final_verdict = interactor(*params)

    with open('output.txt', 'w') as file:
        file.write(str(final_verdict))


if __name__ == "__main__":
    main()
