#include <iostream>
#include <cmath>

using namespace std;

int main(void){
	int a, r, n;
	
	// ���� �������� Ŀ�� 
	long long int d;
	
	scanf("%d %d %d", &a, &r, &n);
	
	d = a * pow(r, n - 1);
	
	cout << d << endl;
	
	return 0;
}
