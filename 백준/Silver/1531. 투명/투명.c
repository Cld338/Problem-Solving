#include <stdio.h>
int main(void) {
	int N, M;
	int pos[200];
	int count;
	int unseen = 0;

	scanf("%d", &N);
	scanf("%d", &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 4; j++) {
			scanf("%d", &pos[i * 4 + j]);
			pos[i * 4 + j]--;
		}
	}
	for (int i = 0; i < 100; i++) {
		for (int j = 0; j < 100; j++) {
			count = 0;
			for (int idx = 0; idx < N; idx++) {
				if ((pos[idx * 4] <= i) && (i <= pos[idx * 4 + 2]) &&
					(pos[idx * 4 + 1] <= j) && (j <= pos[idx * 4 + 3])) {
					count++;
				}
			}
			if (count > M) {
				unseen++;
			}
		}
	}
	printf("%d", unseen);
	
}