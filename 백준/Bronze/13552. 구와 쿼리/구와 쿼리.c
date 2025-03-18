#include <stdio.h>

#define MAX_N 100000  // 점의 최대 개수
#define MAX_M 100000  // 쿼리의 최대 개수

typedef struct {
    int x, y, z;
} Point;

Point points[MAX_N];  // 점 저장 배열

// 거리의 제곱 계산 함수
long long getPowOfDistance(Point p, int x, int y, int z) {
    long long a = (long long)(p.x - x);
    long long b = (long long)(p.y - y);
    long long c = (long long)(p.z - z);
    return a * a + b * b + c * c;
}

int main() {
    int N, M;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d %d %d", &points[i].x, &points[i].y, &points[i].z);
    }
    scanf("%d", &M);
    char output[MAX_M * 12];
    int offset = 0;

    for (int i = 0; i < M; i++) {
        int x, y, z, r, count = 0;
        long long rPow;
        scanf("%d %d %d %d", &x, &y, &z, &r);
        rPow = (long long)r * r;
        for (int j = 0; j < N; j++) {
            if (getPowOfDistance(points[j], x, y, z) <= rPow) {
                count++;
            }
        }

        offset += sprintf(output + offset, "%d\n", count);
    }
    printf("%s", output);

    return 0;
}
