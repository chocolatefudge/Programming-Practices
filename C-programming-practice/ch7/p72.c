#include <stdio.h>

int main(void) {
	int sum = 0;
	int a = 0;
	int cnt = 0;
	while(cnt<5) {
		a = 0;
		while(a<1) {
			printf("Give me a digit: ");
			scanf("%d", &a);
		}
		sum+=a;
		cnt+=1;
	}
	
	printf("%d\n", sum);
}
