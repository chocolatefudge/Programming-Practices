#include <stdio.h>

int main(void)
{
	char str[50];
	char val;
	int i = 0;
	printf("give me a word: ");
	scanf("%s", str);
	val = str[0];
	while(str[i]!='\0')
	{
		if (val<str[i])
			val = str[i];
		i+=1;
	}
	printf("%c\n", val);
	return 0;
}
