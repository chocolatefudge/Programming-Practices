#include <stdio.h>

int AddToTotal(int num)
{
	static int total;
	total+=num;
	return total;
}

int main(void)
{
	int num,i;
	for(i=0;i<3;i++)
	{
		printf("Input %d: ", i+1);
		scanf("%d", &num);
		printf("Accumulate: %d \n", AddToTotal(num));
	}
	return 0;
} 
