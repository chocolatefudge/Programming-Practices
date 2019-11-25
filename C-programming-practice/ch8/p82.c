#include <stdio.h>

int main(void) {
	int num;
	printf("Digit: ");
	scanf("%d", &num);
	num/=10;
	switch(num) {
		case 0:
			printf("0~9\n");
			break;
		case 1:
			printf("10~19\n");
			break;
		default:
			printf("20~\n");
			break;
	}
	return 0;
}
