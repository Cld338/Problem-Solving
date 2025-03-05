# 학생수 N, 과목수 M이 주어진다.
# 각 줄에는 학생의 수강바구니 내역이 주어진다.
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
limit = list(map(int, input().split()))
subject_student_dict = [[] for _ in range(M)] # 과목별 신청 학생
success = {i:set() for i in range(N)} # 각 학생이 성공한 강의
for _ in range(2):
    for student in range(N):
        for subject in list(map(int, input().replace("-1", "").split())):
            subject_student_dict[subject-1].append(student)
    for subject in range(M):
        if len(subject_student_dict[subject]) <= limit[subject]:
            for student in subject_student_dict[subject]:
                success[student].add(subject)
for i in success.values():
    if i:
        print(" ".join([str(j+1) for j in sorted(i)]))
    else:
        print("망했어요")