#include <stdio.h>

int main(void){
	int count;
	
	scanf("%d", &count);
	
	for(count; count > 0; count--){
		printf("%d\n", count);
	}
	
	return 0;
}
