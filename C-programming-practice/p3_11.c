#include <stdio.h>

int f(void);
int g(void);
int h(void);
int y(void);

int main(void) {
	int a, b;
	printf("Enter 2 digits: \n");
	scanf("%d %d", &a, &b);
	printf("%d - %d = %d\n", a, b, a-b);
	printf("%d X %d = %d\n", a, b, a*b);
	f();
	return 0;
} 

int f(void) {
	int num1, num2, num3;
	printf("Enter 3 digits: \n");
	scanf("%d %d %d", &num1, &num2, &num3);
	printf("%d X %d + %d = %d\n", num1, num2, num3, num1*num2+num3);
	g();
	return 0;
}

int g(void) {
	int n;
	printf("Enter a digit: \n");
	scanf("%d", &n);
	printf("%d\n", n*n);
	h();
	return 0;
}
	
int h(void) {
	int p, q;
	printf("Enter 2 digits: \n");
	scanf("%d %d", &p, &q);
	printf("%d, %d\n", p/q, p%q);
	y();
	return 0;
}

int y(void) {
	int num1, num2, num3;
	printf("Enter 3 digits: \n");
	scanf("%d %d %d", &num1, &num2, &num3);
	printf("%d\n", (num1-num2)*(num2+num3)*(num3%num1));
	printf("End of execution\n");
	return 0;
}
