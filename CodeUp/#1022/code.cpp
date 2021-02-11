#include <stdio.h>


int main(void){
	char word[2001];
	
	fgets(word, 2000, stdin);
	
	printf("%s", word);
	
	return 0;
}
