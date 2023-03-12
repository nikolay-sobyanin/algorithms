def forum_optimal():
    n = int(input())
    reply = [0] * n
    topics = [''] * n
    for i in range(n):
        back_msg = int(input())
        if back_msg == 0:
            reply[i] = i
            topics[i] = input()
            input()
        else:
            reply[i] = reply[back_msg - 1]
            input()

    cnt_msg = {}
    for msg in reply:
        cnt_msg[msg] = cnt_msg.get(msg, 0) + 1
    ans = []
    for topic, val in cnt_msg.items():
        ans.append((-val, topic))

    print(topics[min(ans)[1]])


forum_optimal()
