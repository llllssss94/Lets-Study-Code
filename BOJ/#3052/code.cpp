#include <iostream>

using namespace std;

int main(void){
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int count[42] = {0,};
	int num, tmp, r = 0;
	
	for(int i = 0; i < 10; i++){
		cin >> num;
		tmp = num % 42;
		count[tmp]++;
	}
	
	for(int i = 0; i < 42; i++){
		if(count[i] > 0){
			r++;
		}
	}
	
	cout << r << "\n";
	
	return 0;
	
}
