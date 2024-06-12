from collections import deque


def solution(bridge_length, weight, truck_weights):
    start = deque(truck_weights)
    bridge = deque()
    arrive = deque()
    answer = 0

    while len(arrive) != len(truck_weights):
        answer += 1

        if len(bridge) < bridge_length and sum(bridge) + (start[0] if start else 0) <= weight:
            if start:
                bridge.append(start.popleft())
                if len(bridge) == bridge_length:
                    if bridge[-1] != 0:
                        arrive.append(bridge.pop())
                        answer += 1
                    else:
                        bridge.pop()
                        answer += 1

            else:
                bridge.appendleft(0)
                if len(bridge) == bridge_length:
                    if bridge[-1] != 0:
                        arrive.append(bridge.pop())
                    else:
                        bridge.pop()

        else:
            bridge.appendleft(0)
            if len(bridge) == bridge_length:
                if bridge[-1] != 0:
                    arrive.append(bridge.pop())
                else:
                    bridge.pop()
    if bridge_length > len(truck_weights):
        answer += 1

    return answer
