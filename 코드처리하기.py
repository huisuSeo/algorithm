def solution(code):
    ret = []
    mode = 0
    for i in range(len(code)):
        if mode == 0:
            if code[i] == "1":
                mode = 1
            elif i % 2 == 0:
                ret.append(code[i])
        else:
            if code[i] == "1":
                mode = 0
            elif i % 2 == 1:
                ret.append(code[i])

    ret = ''.join(ret)

    answer = "EMPTY"

    if len(ret) != 0:
        answer = ret

    return answer

print(solution("1"))
