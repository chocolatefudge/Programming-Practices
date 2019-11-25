#include <stdio.h>

int main(void)
{
	int arr1[2][4] = {1,2,3,4,5,6,7,8};
	int arr2[4][2];
	for(int t=0;t<4;t++)
	{
		arr2[t][0] = arr1[0][t];
		arr2[t][1] = arr1[1][t];
	}
	for(int i=0;i<2;i++)
	{
		for(int j=0;j<4;j++)
		{
			printf("%d ", arr1[i][j]);
		}
		printf("\n");
	}
	for(int k=0;k<4;k++)
       	{
        for(int l=0;l<2;l++)
		{
			printf("%d ", arr2[k][l]);
		}
		printf("\n");
	}
	return 0;
}
			
 
