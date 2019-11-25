#include <stdio.h>

void fib(int num) {
	int a = 0;
	int b = 1;
	int temp;
	int cnt = 2;
	while(cnt<num) {
		temp = b;
		b = a+temp;
		a = temp;
		cnt+=1;
		printf("%d ", b);
	}
	printf("\n");
	return;
}

int main(void) {
	int a;
	printf("Give me a digit: ");
	scanf("%d", &a);
	printf("0 ");
	if(a==1)
		return 1;
	printf("1 ");
	if(a==2)
		return 1;
	fib(a);
	return 0;
}
