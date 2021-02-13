#include <iostream>
#include <cmath>

using namespace std;

int main(void){
	int w, h, b;
	double bits;
	
	scanf("%d %d %d", &w, &h, &b);
	
	bits = w * h * b;
	
	printf("%.2lf MB", bits / pow(2, 23));
	
	return 0;
}
