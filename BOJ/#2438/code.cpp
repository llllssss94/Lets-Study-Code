#include <iostream>

using namespace std;

int main(void){
	int n;
	
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	
	cin >> n ;
	
	for(int i = 1; i <= n; i++){
		for(int j = 0; j < i; j++) cout << "*";
		cout << "\n";
	}
	
	return 0;
}
