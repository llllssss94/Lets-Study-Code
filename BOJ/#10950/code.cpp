#include <stdio.h>

int main(void){
	int num, A, B;
	
	scanf("%d", &num);
	
	for(int i = 0; i < num; i++){
		scanf("%d %d", &A, &B);
		printf("%d\n", A + B);
	}
	
	return 0;
}
