#include <stdio.h>

int main(void){
	int a, b;
	
	scanf("%d %d", &a, &b);
	
	if(a == 1 || b == 1){
		printf("1");
	}		
	else{
		printf("0");
	}
		
	return 0;
}
