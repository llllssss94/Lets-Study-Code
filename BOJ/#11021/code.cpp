#include <iostream>

using namespace std;

int main(void){
	int n, A, B;
	
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	
	cin >> n ;
	
	for(int i = 1; i <= n; i++){
		cin >> A >> B;
		cout << "Case #"<< i << ": " << A+B << "\n";
	}
	
	return 0;
}
