#include <stdio.h>

int main(void){
	int a;
	
	scanf("%d", &a);
	
	if(a > 89){
		printf("A");
	}
	else if(a > 69){
		printf("B");
	}
	else if(a > 39){
		printf("C");
	}
	else{
		printf("D");
	}
	
	return 0;
}
