#include <iostream>

int main(void){
	int a, b;
	
	scanf("%d %d", &a, &b);
	
	// ���� ���� 10^-9���� ����� �� ^^ 
	printf("%.10lf", (double(a)/b)); // ����ϱ� ���� �ϳ��� �÷��� ����Ʈ�� �ؾ� ����� 
	
	return 0;
}
