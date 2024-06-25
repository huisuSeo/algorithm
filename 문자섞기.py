def solution(str1, str2):
    answer = []
    for a in range(len(str1)):
        answer.append(str1[a])
        answer.append(str2[a])

    return ''.join(answer)

print(solution("aaaaa","bbbbb"))
