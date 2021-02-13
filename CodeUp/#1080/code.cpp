#include <iostream>

int main(void){
	int num, i = 0, sum = 0;
	
	scanf("%d", &num);
	
	while(sum < num){
		i++;
		sum += i;
	}
	
	printf("%d", i);
	
	return 0;
}
