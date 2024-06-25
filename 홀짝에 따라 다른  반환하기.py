def solution(n):
    answer_list = []
    if n % 2 == 0:
        even = True
        for number in range(n + 1):
            if number % 2 == 0:
                answer_list.append(number)
    else:
        even = False
        for number in range(n + 1):
            if number % 2 == 1:
                answer_list.append(number)

    if even:
        for i in range(len(answer_list)):
            answer_list[i] = answer_list[i] * answer_list[i]

    answer = 0

    for i in answer_list:
        answer = answer + int(i)

    return answer

print(solution(10))