#include <stdio.h>

int main(void){
	int arr[5][5] = {
		{1,2,3,4},
		{5,6,7,8},
		{1,2,3,4},
		{5,6,7,8},
		{0,0,0,0}
	};
	for(int i=0;i<4;i++)
	{
		for(int l=0;l<4;l++)
		{
			arr[i][4]+=arr[i][l];
			arr[4][l]+=arr[i][l];
		}
	}
	for(int j=0;j<5;j++)
	{
		for(int k=0;k<5;k++)
		{
			printf("%d ", arr[j][k]);
		}
		printf("\n");
	}
	return 0;
}
