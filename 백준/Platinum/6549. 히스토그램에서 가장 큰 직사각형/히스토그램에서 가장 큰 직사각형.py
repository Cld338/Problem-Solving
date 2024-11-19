import sys

input = sys.stdin.readline


def divide_and_conquer(histogram, start, end):
    if start == end:
        return histogram[start]
    if end - start == 1:
        return max(2 * min(histogram[start], histogram[end]), histogram[start], histogram[end])

    mid = (start + end) // 2
    left_area = divide_and_conquer(histogram, start, mid)
    right_area = divide_and_conquer(histogram, mid + 1, end)

    left = mid
    right = mid + 1
    current_height = min(histogram[left], histogram[right])
    mid_area = current_height * 2

    while start <= left or right <= end:
        if right > end or (left >= start and histogram[left] >= histogram[right]):
            current_height = min(current_height, histogram[left])
            left -= 1
        else:
            current_height = min(current_height, histogram[right])
            right += 1
        mid_area = max(mid_area, current_height * (right - left - 1))
    return max(left_area, right_area, mid_area)


def main():
    results = []
    while True:
        histogram = list(map(int, input().split()))
        if histogram[0] == 0:
            break
        n = histogram[0]
        results.append(divide_and_conquer(histogram, 1, n))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
