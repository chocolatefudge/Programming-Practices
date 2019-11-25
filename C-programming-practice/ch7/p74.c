#include <stdio.h>

int main(void) {
	int a,b;
	int sum = 0;
	
	printf("Give me 2 digits: ");
	scanf("%d %d", &a, &b);
	if(a>b)
		return 1;
	for(;a<b;a++)
		sum+=a;
	sum+=b;
	printf("%d\n", sum);
	return 0;
}
