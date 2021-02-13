#include <iostream>

using namespace std;

int main(void){
	int A, B, C;
	
	scanf("%d %d %d", &A, &B, &C);
	
	cout << (A+B)%C << endl;
	cout << ((A%C) + (B%C))%C << endl;
	cout << (A*B)%C << endl;
	cout << ((A%C) * (B%C))%C << endl;
	
	return 0;
} 
