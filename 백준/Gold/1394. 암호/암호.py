import sys

texts = sys.stdin.readline().strip()
ans = sys.stdin.readline().strip()
num = len(texts)
mod = 900528
length = len(ans)
char_to_index = {char: idx for idx, char in enumerate(texts)}
c = 0
power = 1
for _ in range(1, length):
    power = (power * num) % mod
    c = (c + power) % mod
power = 1
for i in reversed(range(length)):
    index = char_to_index[ans[i]]
    c = (c + index * power) % mod
    power = (power * num) % mod
print((c + 1) % mod)
