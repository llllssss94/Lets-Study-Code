#include <iostream>

using namespace std;

int main(void){
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	
	int A, B;
	
	while(true){
		cin >> A >> B;
		if(cin.fail()) break;
		
		cout << A + B << "\n";
	}
	
	return 0;
}
