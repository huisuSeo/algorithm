import sys

n, k = sys.stdin.readline().split()

n = int(n)
k = int(k)

s = [i + 1 for i in range(n)] #for 루프로 배열 만드는 방법 꼭 기억하기
p = []

index = 0

while len(s) > 0:
        index = (index + k - 1) % len(s)  #인덱스에 k 더하고 -1 해준거를 길이로 나누면 계속 뺄 수 있따
        p.append(s.pop(index)) #p에 붙이기와 s에서 빼기 동시에

result = ", ".join(map(str, p)) #<> 안에 쉼표로 구분해서 넣어주려고 문자열로 만든다음에 ,으로 구분

print(f"<{result}>") #포멧 이렇게 {} 안에 넣으면 해줌
