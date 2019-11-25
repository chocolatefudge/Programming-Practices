#include <stdio.h>

int main(void)
{
	int arr[5];
	int max, min, sum;
	printf("Give me 5 digits: ");
	scanf("%d %d %d %d %d", &arr[0], &arr[1], &arr[2], &arr[3], &arr[4]);
	max = arr[0];
	min = arr[0];
	sum = 0;
	for (int i=0 ; i<5 ; i++)
	{
		if (arr[i]<min)
			min = arr[i];
		if (arr[i]>max)
			max = arr[i];
		sum+=arr[i];
	}
	printf("min: %d, max = %d, sum = %d. \n", min, max, sum);
	return 0;
}
