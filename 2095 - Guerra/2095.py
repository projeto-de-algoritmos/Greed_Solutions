S = int(input())
quadradonia = list(map(int, input().split()))
noglonia = list(map(int, input().split()))

quadradonia.sort()
noglonia.sort()
vencedor = 0
j = 0

# print(quadradonia)
# print(noglonia)

for i in range(S):
    while j < S and quadradonia[i] >= noglonia[j]:
        # print("a: ",quadradonia[i], noglonia[j])
        j += 1
    if j < S and quadradonia[i] < noglonia[j]:
        # print("b: ",quadradonia[i], noglonia[j])
        vencedor += 1
        j += 1

print(vencedor)