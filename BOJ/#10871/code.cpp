#include <iostream>

using namespace std;

int main(void){
	int n, x, a;
	
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	
	cin >> n >> x;
	
	for(int i = 1; i <= n; i++){
		cin >> a;
		if(a < x){
			cout << a << " ";
		}
	}
	cout << "\n";
	
	return 0;
}
