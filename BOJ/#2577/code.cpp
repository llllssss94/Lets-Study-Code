#include <iostream>

using namespace std;

int main(void){
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int count[10] = {0,};
	int A, B, C, num, tmp;
	
	cin >> A >> B >> C;
	
	num = A * B * C;
	
	while(num != 0){
		tmp = num % 10;
		count[tmp]++;
		num = num / 10;
	}
	
	for(int i = 0; i < 10; i++){
		cout << count[i] << "\n";
	}
	
	return 0;
	
}
