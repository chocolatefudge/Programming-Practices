#include <stdio.h>
#include <string.h>

int main(void)
{
	char str[20];
	int i, size;
	int sum = 0;
	fgets(str, sizeof(str), stdin);
	size = strlen(str);
	for(i=0;i<size;i++)
	{
		if(str[i]>='0' && str[i]<='9')
		{
			sum+=str[i]-48;
		}
	}
	printf("%d\n", sum);
	return 0;
}
