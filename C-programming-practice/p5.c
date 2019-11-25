#include <stdio.h>

int f(void);
int g(void);
int h(void);

int main(void) {
	int x1, x2, y1, y2;
	printf("x, y coordinate for point 1: \n");
	scanf("%d %d", &x1, &y1);
	printf("x, y coordinate for point 2: \n");
        scanf("%d %d", &x2, &y2);
	printf("Size of the area is %d. \n", (x2-x1)*(y2-y1));
	f();
	return 0;
}

int f(void) {
	double x, y;
	printf("Give me 2 doubles: \n");
	scanf("%lf %lf", &x, &y);
	printf("%f, %f, %f, %f\n", x+y, x-y, x*y, x/y);
	g();
	return 0;
}

int g(void) {
	int a;
	printf("Give me a digit between 0~127: \n");
	scanf("%d", &a);
	printf("%c\n", a);
	h();
	return 0;
}

int h(void) {
	char b;
	printf("Give me a random character: \n");
        scanf("%c", &b);
	printf("%d\n", b);
	return 0;
}
	
