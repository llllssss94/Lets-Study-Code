#include <stdio.h>

int main(void){
	int a, b, c;
	
	scanf("%d %d %d", &a, &b, &c);
	
	printf("%d", (a < b ? a:b) < c ? (a < b ? a:b):c);
	
	return 0;	
}
