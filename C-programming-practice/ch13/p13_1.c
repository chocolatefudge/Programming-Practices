#include <stdio.h>

int main(void)
{
	int str[5] = {1,2,3,4,5};
	int *ptr = str;
	for(int i=0;i<5;i++)
	{
		*(ptr+i)+=1;
	}
	printf("%d %d %d %d %d", str[0], str[1], str[2], str[3], str[4]);
	return 0;
}
