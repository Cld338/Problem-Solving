from collections import Counter

def check_even_char_count(s):
    length = len(s)
    if length % 2 == 1:
        middle_index = length // 2
        s = s[:middle_index] + s[middle_index+1:]
    char_count = Counter(s)
    for count in char_count.values():
        if count % 2 == 1:
            return "No"
    
    return "Yes"
N = int(input())
test_string = input()
result = check_even_char_count(test_string)
print(result)
