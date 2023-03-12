def check_bracket_seq():
    s = input().strip()
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    stack = []
    for smb in s:
        if smb in brackets.keys():
            stack.append(smb)
        else:
            if len(stack) == 0:
                return False

            if brackets[stack[-1]] == smb:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


print('yes' if check_bracket_seq() else 'no')
