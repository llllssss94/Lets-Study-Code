#include <stdio.h>
#include <math.h>

int main(void){
	int y, m, d;
	
	scanf("%4d.%2d.%2d", &y, &m, &d);
	
	printf("%02d-%02d-%04d", d, m, y);
	
	
	return 0;
}
