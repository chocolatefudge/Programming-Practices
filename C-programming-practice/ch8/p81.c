#include <stdio.h>
  
int main(void) {
        int a,b,c;
        int mean;
        printf("What's your math score?: ");
        scanf("%d", &a);
        printf("What's your english score?: ");
        scanf("%d", &b);
        printf("What's your science score?: ");
        scanf("%d", &c);
        mean = (a+b+c)/3;
        printf("Your grade is ");
        if(mean>90)
                printf("A\n");
        else if(mean>80)
                printf("B\n");
        else if(mean>70)
                printf("C\n");
        else if(mean>60)
                printf("D\n");
        else
                printf("F\n");
        return 0;
}      
