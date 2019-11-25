#include <stdio.h>

typedef struct point
{
	int xpos;
	int ypos;
} Point;

void conve(Point * p1, Point *p2)
{
	int xt, yt;
	xt = p1->xpos;
	yt = p1->ypos;
	p1->xpos = p2->xpos;
	p1->ypos = p2->ypos;
	p2->xpos = xt;
	p2->ypos = yt;
	return;
}

int main(void)
{
	Point pos1 = {2,4};
	Point pos2 = {3,6};
	conve(&pos1, &pos2);
	printf("P1: (%d, %d), P2: (%d, %d) \n", pos1.xpos, pos1.ypos, pos2.xpos, pos2.ypos);
	return 0;
}
