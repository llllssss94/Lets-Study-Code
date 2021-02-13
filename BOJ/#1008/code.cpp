#include <iostream>

int main(void){
	int a, b;
	
	scanf("%d %d", &a, &b);
	
	// 오차 범위 10^-9까지 맞춰야 함 ^^ 
	printf("%.10lf", (double(a)/b)); // 계산하기 전에 하나라도 플로팅 포인트로 해야 결과도 
	
	return 0;
}
