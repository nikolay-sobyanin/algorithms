def text_analysis(file_name):
    words = {}

    with open(file_name, 'r') as file:
        for line in file.readlines():
            for word in line.strip().split():
                if word not in words:
                    words[word] = 0
                words[word] += 1

    for word, _ in sorted(words.items(), key=lambda x: (-x[1], x[0])):
        print(word)


text_analysis('input.txt')
