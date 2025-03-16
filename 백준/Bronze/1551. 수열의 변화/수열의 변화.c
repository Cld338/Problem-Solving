#include <stdio.h>
#include <string.h>
int main(void) {
	int N, K;
	char buffer[90];
	int nums[20];
	scanf("%d", &N);
	scanf("%d", &K);
	scanf("%s", buffer);
	char* ret_token = NULL;
	ret_token = strtok(buffer, ",");
	int idx = 0;
	while (ret_token != NULL) {
		nums[idx] = atoi(ret_token);
		idx++;
		ret_token = strtok(NULL, ",");
	}
	for (int k = 1; k <= K; k++) {
		for (int i = 0; i < N - k; i++) {
			nums[i] = nums[i + 1] - nums[i];
		}
	}
	for (int i = 0; i < N - K - 1; i++) {
		printf("%d,", nums[i]);
	}
	printf("%d", nums[N-K-1]);
	return 0;

}