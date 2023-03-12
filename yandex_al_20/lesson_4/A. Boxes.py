def count_boxes():
    n = int(input())
    boxes = {}
    for _ in range(n):
        color, val = map(int, input().split())
        if color not in boxes.keys():
            boxes[color] = 0
        boxes[color] += val

    sortkeys = sorted(boxes)
    for key in sortkeys:
        print(key, boxes[key])


count_boxes()

