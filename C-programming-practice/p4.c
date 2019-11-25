#include <stdio.h>

int f(void);
int main(void){
	int n;
	printf("Enter a digit: \n");
	scanf("%d", &n);
	printf("%d\n", ~n+1);
	f();
	return 0;
}

int f(void){
	int n;
	printf("Enter a digit between 1~100: \n");
	scanf("%d", &n);
	printf("%d\n", (n<<3)>>2);
	printf("End of execution\n");
	return 0;
	
}
