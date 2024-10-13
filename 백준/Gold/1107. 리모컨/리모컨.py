N = input()
n = int(input())
broken = list(map(int, input().split())) if n else []
not_broken = [i for i in range(10) if i not in broken]
not_broken.sort()

# 고장난 버튼이 모두 고장난 경우 예외 처리
if not not_broken:
    print(abs(int(N) - 100))
    exit()

# lower_bound 함수 수정
def lower_bound(ls, value):
    left, right = 0, len(ls)
    while left < right:
        mid = (left + right) // 2
        if ls[mid] < value:
            left = mid + 1
        else:
            right = mid
    if left < len(ls):
        return ls[left]
    else:
        return ls[-1]  # 범위를 벗어나면 가장 큰 값 반환

# upper_bound 함수 수정
def upper_bound(ls, value):
    left, right = 0, len(ls)
    while left < right:
        mid = (left + right) // 2
        if ls[mid] <= value:
            left = mid + 1
        else:
            right = mid
    if left > 0:
        return ls[left - 1]
    else:
        return ls[0]  # 범위를 벗어나면 가장 작은 값 반환

from itertools import product

min_press = abs(int(N) - 100)  # +,- 버튼만 사용하는 경우

for length in range(1, 7):  # 채널 번호는 최대 6자리까지 가능
    # 모든 가능한 숫자 조합 생성
    for nums in product(not_broken, repeat=length):
        channel = int(''.join(map(str, nums)))
        press = abs(channel - int(N)) + length  # 숫자 버튼 누른 횟수 + 이동 횟수
        if press < min_press:
            min_press = press

print(min_press)
