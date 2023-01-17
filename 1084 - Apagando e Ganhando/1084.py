from collections import deque

a, b = map(int, input().split())

while a != 0 and b != 0:
    d = b
    linha = input()
    s = deque()
    for i in range(len(linha)):
        while d > 0 and len(s) > 0 and s[0] < linha[i]:
            s.popleft()
            d -= 1
        s.appendleft(linha[i])
    # s.pop()
    s = list(s)
    s = s[d:]
    print("".join(s[::-1]))
    # print("".join(s)[::-1])
    a, b = map(int, input().split())
