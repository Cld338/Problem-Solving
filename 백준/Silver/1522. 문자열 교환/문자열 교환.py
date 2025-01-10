string = input()
L = string.count("a")
S = len(string)
string = string + string[:L]
window = string[:L]
count = window.count("b")
for i in range(S-1):
    window = window[1:] + string[L+i]
    count = min(count, window.count("b"))
print(count)