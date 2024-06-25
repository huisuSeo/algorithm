def solution(friends, gifts):
    jisu = {}
    present = {}
    gift_array = []

    for gift in gifts:
        gift_array.append(gift.split())

    for friend in friends:
        jisu[friend] = 0
        present[friend] = 0

    for gift in gift_array:
        jisu[gift[0]] = jisu[gift[0]] + 1
        jisu[gift[1]] = jisu[gift[1]] - 1

    for friend_F in friends:
        for friend_T in friends:
            give = 0
            receive = 0
            for gift in gift_array:
                if gift[0] == friend_F and gift[1] == friend_T:
                    give = give + 1
                elif gift[0] == friend_T and gift[1] == friend_F:
                    receive = receive + 1
            if give > receive:
                present[friend_F] = present[friend_F] + 1
            elif receive > give:
                present[friend_T] = present[friend_T] + 1
            else:
                if jisu[friend_F] > jisu[friend_T]:
                    present[friend_F] = present[friend_F] + 1
                elif jisu[friend_T] > jisu[friend_F]:
                    present[friend_T] = present[friend_T] + 1
        friends.remove(friend_F)

    return max(present.values())

print(solution(["muzi", "ryan", "frodo", "neo"],["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))