# Link: https://contest.yandex.ru/contest/28730/problems/B/

def read_input(file_name='input.txt') -> list:
    with open(file_name, 'r') as file:
        text = file.read().strip()
        return [int(x) for x in text.split()]


def cont_stations(n: int, i: int, j: int) -> int:
    """
    Count stations amount two stations of ring line of metro
    :param n: number stations
    :param i: station in
    :param j: station out
    :return: count stations
    """
    way_a = abs(i - j) - 1
    way_b = n - way_a - 2
    return min(way_a, way_b)


def main():
    params = read_input()
    with open('output.txt', 'w') as file:
        file.write(str(cont_stations(*params)))


if __name__ == "__main__":
    main()
