#include <iostream>
#include <cmath>

using namespace std;

int main(void){
	int n, m, r, sum = 0;
	
	scanf("%d\n%d", &n, &m);
	
	for(int i = 0; i < 3; i++){
		// 자릿수 하나씩 띠어서 
		r = m % 10;
		
		// 결과 출력 
		cout << n * r << endl;
		
		// 자릿수 올려서 합산 
		sum += (n*r) * pow(10, i);
		
		// 맨 뒷자리 삭제 
		m = m / 10;
	}
	
	// 최종 결과 출력 
	cout << sum << endl;
	
	return 0;
}
