def solution(a, b):
    ab = []
    ab.append(str(a))
    ab.append(str(b))

    ab = int(''.join(ab))


    if ab >= 2 * a * b:
        answer = ab
    else:
        answer = 2 * a * b

    return answer