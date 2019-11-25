#include <stdio.h>

int main(void)
{
	int str[6] = {1,2,3,4,5,6};
	int *p1 = str;
	int *p2 = &str[5];
	int a,b;
	for(int i=0;i<3;i++)
	{
		a = *(p1+i);
		b = *(p2-i);
		*(p1+i) = b;
		*(p2-i) = a;
	}
	for(int j=0;j<6;j++)
	{
		printf("%d ", str[j]);
	}
	printf("\n");
	return 0;
}
