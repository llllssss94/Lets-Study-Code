#include <iostream>

using namespace std;

int main(void){
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int num, idx, max = 0;
		
	for(int i = 1; i < 10; i++){
		cin >> num;
		if(num > max){
			max = num;
			idx = i;
		}
	}
	
	cout << max << "\n" << idx << "\n";
	
	return 0;
	
}
