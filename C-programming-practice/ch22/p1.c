#include <stdio.h>

struct employee
{
	char name[20];
	char id[20];
	int pay;
};

int main(void)
{
	struct employee a;
	printf("name, id, payment: ");
	scanf("%s", a.name);
	scanf("%s", a.id);
	scanf("%d", &a.pay);
	printf("Name: %s, ID: %s, Pay:%d. \n", a.name, a.id, a.pay);
	return 0;
}
