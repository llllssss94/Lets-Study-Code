#include <stdio.h>

int main(void){
	char c, i = 'a';
	
	scanf("%c", &c);
	
	while(i <= c)
	{
		printf("%c ", i);
		i++;
	}
	
	return 0;
}
