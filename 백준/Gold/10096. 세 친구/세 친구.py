def solve(U):
    N = len(U)
    if N % 2 == 0:
        return "NOT POSSIBLE"

    mid = N // 2
    answers = set()
    left, right = U[:mid+1], U[mid+1:]
    idx_l, idx_r, mismatch = 0, 0, 0
    S1 = []
    while idx_r < len(right) and idx_l < len(left):
        if left[idx_l] == right[idx_r]:
            S1.append(left[idx_l])
            idx_l += 1
            idx_r += 1
        else:
            if mismatch == 0:
                mismatch += 1
                idx_l += 1
            else:
                S1 = None
                break
    if mismatch == 0: 
        S1 = left[:-1]
    if S1 and len(S1) == mid:
        answers.add(''.join(S1))

    left, right = U[:mid], U[mid:]
    idx_l, idx_r, mismatch = 0, 0, 0
    S2 = []
    while idx_l < len(left) and idx_r < len(right):
        if left[idx_l] == right[idx_r]:
            S2.append(left[idx_l])
            idx_l += 1
            idx_r += 1
        else:
            if mismatch == 0:
                mismatch += 1
                idx_r += 1
            else:
                S2 = None
                break
    if mismatch == 0: 
        S2 = right[:-1]
    if S2 and len(S2) == mid:
        answers.add(''.join(S2))

    if len(answers) == 0:
        return "NOT POSSIBLE"
    elif len(answers) > 1:
        return "NOT UNIQUE"
    else:
        return answers.pop()

N = int(input())
U = input().strip()
print(solve(U))
