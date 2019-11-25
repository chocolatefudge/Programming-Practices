#include <stdio.h>

int main(void){
	int a, b, c, d;
	int cnt = 1;
	int sum = 0;
	int i = 9;
	printf("Give me a digit between 1~20: ");
	scanf("%d", &a);
	while(a>0) {
		printf("Hello world!\n");
		a-=1;
	}
	printf("Give me a digit between 1~20: ");
        scanf("%d", &b);
	while(cnt<b) {
		printf("%d ", cnt*3);
		cnt+=1;
		printf("\n");
	}
	printf("Give me a digit: ");
	scanf("%d", &c);
	while(c!=0) {
		sum+=c;
		printf("Give me a digit: ");
        	scanf("%d", &c);
	}
	printf("Total sum is %d\n", sum);
	printf("Give me a digit between 1~9: ");
	scanf("%d", &d);
	while (i>0) {
		printf("%d ", i*d);
		i-=1;
		printf("\n");
	}
	return 0;
}
