def solution(a, b):

    ab = []
    ba = []

    ab.append(str(a))
    ab.append(str(b))
    ba.append(str(b))
    ba.append(str(a))

    ab = int(''.join(ab))
    ba = int(''.join(ba))

    if ab >= ba:
        answer = ab
    else:
        answer = ba

    return answer