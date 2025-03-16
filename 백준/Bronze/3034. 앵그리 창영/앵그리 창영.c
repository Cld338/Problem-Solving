#include <stdio.h>
#include <math.h>
int main(void) {
	int N, W, H;
	int L;
	scanf("%d %d %d", &N, &W, &H);
	for (int i = 0; i < N; i++) {
		scanf("%d", &L);
		if (L * L <= W * W + H * H) {
			printf("DA");
		}
		else {
			printf("NE");
		}
		printf("\n");
	}
}