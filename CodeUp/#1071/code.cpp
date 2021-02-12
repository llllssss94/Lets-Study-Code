#include <stdio.h>

int main(void){
	int num;
	
	while(true){
		scanf("%d", &num);
		
		if(num == 0) break;
		
		printf("%d\n", num);
	}
}
