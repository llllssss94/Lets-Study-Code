#include <iostream>

int main(void){
	long long int h, b, c, s;
	double bits;
	
	scanf("%d %d %d %d", &h, &b, &c, &s);
	
	bits = h * (b/8) * c * s;
	
	printf("%.1lf MB", bits / (1024 * 1024));
	
	return 0;
}
