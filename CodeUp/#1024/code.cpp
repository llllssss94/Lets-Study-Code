#include <stdio.h>


int main(void){
	char str[21], i;
	
	scanf("%s", &str);
	
	for(i = 0; str[i] != 0; i++){
		printf("\'%c\'\n", str[i]);
	}
	
	return 0;
}
