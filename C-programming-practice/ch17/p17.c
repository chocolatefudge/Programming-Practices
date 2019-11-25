#include <stdio.h>

void maxandmin(int* arr, int **max, int **min)
{
	int size = sizeof(arr)/sizeof(int);
	max = min = &arr[0];
	for(int j=0;j<size;j++);
	{
		if(arr[j]<*min)
			min = &arr[j];
		if(arr[j]>*max)
			max = &arr[j];
	}
	return;
}

int main(void)
{
	int *maxptr;
	int *minptr;
	int arr[5];
	for(int i=0;i<5;i++)
	{
		printf("Give me a digit: ");
		scanf("%d", &arr[i]);
	}
	maxandmin(arr, &maxptr, &minptr);
	printf("%d, %d", *maxptr, *minptr);
	return 0;
}
