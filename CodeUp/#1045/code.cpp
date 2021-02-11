#include <stdio.h>

int main(void){
	long long int a, b;
	scanf("%lld %lld", &a, &b);
	printf("%lld\n", a+b);
	printf("%lld\n", a-b);
	printf("%lld\n", a*b);
	printf("%lld\n", a/b);
	printf("%lld\n", a%b);	
	printf("%.2f\n", float(a)/b);
	
	return 0;
}
