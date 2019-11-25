#include <stdio.h>

int main(void)
{
	char str[50];
	int i = 0;
	printf("Give me a word: ");
	scanf("%s", str);
	while(str[i]!='\0')
	{
		i+=1;
	}
	printf("Length is %d. \n", i);
	return 0;
}
