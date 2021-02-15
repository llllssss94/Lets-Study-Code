#include <iostream>

using namespace std;

int main(void){
	int a, b;
	
	scanf("%d %d", &a, &b);
	
	if(a > b){
		cout << '>' << endl;
	}
	else if(a < b){
		cout << '<' << endl;
	}
	else{
		cout << "==" << endl;
	}
	
	return 0;
}
