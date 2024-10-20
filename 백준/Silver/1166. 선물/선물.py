N, L, W, H = map(int, input().split())
s, e = 0, 1_000_000_000
answer = 0
for i in range(100):
    m = (s+e) / 2

    if (L//m)*(W//m)*(H//m) >= N:
        answer = m
        s = m
    else:
        e = m

print(answer)