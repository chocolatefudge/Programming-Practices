#include <stdio.h>

typedef struct point
{
	int xpos;
	int ypos;
} Point;

typedef struct rectangle
{
	Point a;
	Point b;
} Rectangle;

int size(Rectangle r)
{
	int width, height;
	int val;
	width = r.a.xpos-r.b.xpos;
	height = r.a.ypos-r.b.ypos;
	val = width*height;
	if (val<0)
		return -val;
	return val;
}
void points(Rectangle r)
{
	printf("P1: (%d, %d) \n", r.a.xpos, r.a.ypos);
	printf("P2: (%d, %d) \n", r.a.xpos, r.b.ypos);
	printf("P3: (%d, %d) \n", r.b.xpos, r.a.ypos);
	printf("P4: (%d, %d) \n", r.b.xpos, r.b.ypos);
}

int main(void)
{
	Rectangle r;
	printf("p1: ");
	scanf("%d %d", &r.a.xpos, &r.a.ypos);
	printf("p2: ");
	scanf("%d %d", &r.b.xpos, &r.b.ypos);
	printf("%d\n", size(r));
	points(r);
	return 0;
}
