#include <iostream>

int main(void){
	char hex;
	int i, dec;
	
	scanf("%c", &hex);
	
	// 10진수 변환 HARD CODE 
	switch(hex)
	{
		case 'A':
			dec = 10;
			break;
		case 'B':
			dec = 11;
			break;
		case 'C':
			dec = 12;
			break;
		case 'D':
			dec = 13;
			break;
		case 'E':
			dec = 14;
			break;
		case 'F':
			dec = 15;
			break;
		default:
			return 1;
	}
	
	for(i = 1; i < 16; i++){
		printf("%c*%X=%X\n", hex, i, (dec*i));
	}
	
	return 0;
}
