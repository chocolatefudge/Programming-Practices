#include <stdio.h>

int main(void) {
	int cnt = 0;
	int sum = 0;
	do {
		if(cnt%2==0)
			sum+=cnt;
		cnt+=1;
	} while (cnt<=100);
	printf("%d\n", sum);
	return 0;
}
