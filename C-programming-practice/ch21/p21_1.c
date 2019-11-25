#include <stdio.h>

int conv(char ch)
{
	int diff = 'A'-'a';
	if(ch<='z' && ch>='a')
		ch-=diff;
	else if(ch<='Z' && ch>='A')
		ch+=diff;
	else
		return -1;
	return ch;
}

int main(void)
{
	int ch;
	ch = getchar();
	ch = conv(ch);
	if(ch==-1)
	{
		printf("Error\n");
		return -1;
	}
	else
	{
		putchar(ch);
		return 0;
	}
}
