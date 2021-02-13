#include <stdio.h>

int main(void){
	int num, i = 0, sum = 0;
	
	scanf("%d", &num);
	
	while(i <= num){
		if(i % 2 == 0){
			sum += i;
		}
		i++;
	}
	
	printf("%d", sum);
	
	return 0;
}
