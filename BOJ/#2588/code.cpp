#include <iostream>
#include <cmath>

using namespace std;

int main(void){
	int n, m, r, sum = 0;
	
	scanf("%d\n%d", &n, &m);
	
	for(int i = 0; i < 3; i++){
		// �ڸ��� �ϳ��� �� 
		r = m % 10;
		
		// ��� ��� 
		cout << n * r << endl;
		
		// �ڸ��� �÷��� �ջ� 
		sum += (n*r) * pow(10, i);
		
		// �� ���ڸ� ���� 
		m = m / 10;
	}
	
	// ���� ��� ��� 
	cout << sum << endl;
	
	return 0;
}
