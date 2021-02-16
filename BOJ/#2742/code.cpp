#include <iostream>

using namespace std;

int main(void){
	int n;
	
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	
	cin >> n ;
	
	for(int i = n; i > 0; i--){
		cout << i << "\n";
	}
	
	return 0;
}
